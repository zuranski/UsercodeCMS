#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_TriggerObjects.h"

DJ_TriggerObjects::DJ_TriggerObjects(const edm::ParameterSet& iConfig) :
    inputTag   (iConfig.getParameter<edm::InputTag>("InputTag")),
    ObjectsToStore (iConfig.getParameter<std::vector<std::string> >("ObjectsToStore"))
{
  
  produces <std::vector<trgobj> >           ( "trgobjs");

}

void DJ_TriggerObjects::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  
  std::auto_ptr<std::vector<trgobj> > trgobjs ( new std::vector<trgobj> );
  
  edm::Handle<trigger::TriggerEvent> triggerEvent;
  iEvent.getByLabel( inputTag , triggerEvent);
  
  if ( triggerEvent.isValid() ){

    //------------------------------------------------------------------------
    // Get the trigger objects in the event
    //------------------------------------------------------------------------

    const trigger::TriggerObjectCollection & triggerObjects = triggerEvent -> getObjects();
    
    //------------------------------------------------------------------------
    // Loop over the filters in the trigger event
    // e.g.: hltEle27WP80TrackIsoFilter
    //------------------------------------------------------------------------
    
    size_t nFilters       = triggerEvent -> sizeFilters();
    size_t iFilter        = 0;

    for (; iFilter < nFilters; ++iFilter) {

      //------------------------------------------------------------------------
      // Find information for each filter:
      // -  Name  : name of the filter, e.g. hltEle27WP80TrackIsoFilter
      // - "Keys" : std::vector<uint16_t> storing indices of trigger objects that pass the filter
      //------------------------------------------------------------------------
     
      // get name and check if it's in the list 
      std::string name = triggerEvent -> filterTag ( iFilter ).label();
      bool interestingObject = false;
      for(size_t i=0;i<ObjectsToStore.size();i++){
        if (name.find(ObjectsToStore[i]) != std::string::npos){
          interestingObject = true;
          break; 
        }
      }
      if (!interestingObject) continue;

      const trigger::Keys& keys = triggerEvent -> filterKeys( iFilter );
      const trigger::Vids& vids = triggerEvent -> filterIds ( iFilter );
      
      //------------------------------------------------------------------------
      // Loop over the keys to get to the trigger objects that pass the filter
      //------------------------------------------------------------------------
      
      int nKeys = (int) keys.size();
      int nVids = (int) vids.size();
      assert ( nKeys == nVids ) ;

      for (int iTriggerObject = 0; iTriggerObject < nKeys; ++iTriggerObject ) { 

        trgobj tobj;

	// Get the object ID and key
	int                id  = vids[iTriggerObject];
	trigger::size_type key = keys[iTriggerObject];

	// Get the trigger object from the key

	const trigger::TriggerObject & triggerObject = triggerObjects [key];
	
	// Store the trigger object as a TLorentzVector (borrowed from S. Harper)
        tobj.tag = name;
        tobj.id = id;
        tobj.pt = triggerObject.pt();
        tobj.eta = triggerObject.eta();
        tobj.phi = triggerObject.phi();
        tobj.mass = triggerObject.mass();

        trgobjs->push_back(tobj);

      } // end loop over keys/trigger objects passing filters

    } // end loop over filters 
  } else { 
    edm::LogError("DJ_TriggerObjects") << "Error! Can't get the product " << inputTag;
  }

  //------------------------------------------------------------------------
  // Push the information into the event
  //------------------------------------------------------------------------

  iEvent.put ( trgobjs, "trgobjs" ) ;
	      

}

