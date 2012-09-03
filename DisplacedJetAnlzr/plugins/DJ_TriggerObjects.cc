#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_TriggerObjects.h"

DJ_TriggerObjects::DJ_TriggerObjects(const edm::ParameterSet& iConfig) :
    inputTag   (iConfig.getParameter<edm::InputTag>("InputTag")),
    ObjectsToStore (iConfig.getParameter<std::vector<std::string> >("ObjectsToStore"))
{
  
  produces <std::vector<float> >           ( "trgobjPt");
  produces <std::vector<float> >           ( "trgobjEta");
  produces <std::vector<float> >           ( "trgobjPhi");
  produces <std::vector<float> >           ( "trgobjMass");
  produces <std::vector<std::string> >           ( "trgobjTag");

}

void DJ_TriggerObjects::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  
  std::auto_ptr<std::vector<float> > trgobjPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > trgobjEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > trgobjPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > trgobjMass ( new std::vector<float> );
  std::auto_ptr<std::vector<std::string> > trgobjTag ( new std::vector<std::string> );
  
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


	// Get the object ID and key
	trigger::size_type key = keys[iTriggerObject];

	// Get the trigger object from the key

	const trigger::TriggerObject & triggerObject = triggerObjects [key];
	
	// Store the trigger object as a TLorentzVector (borrowed from S. Harper)
        trgobjTag->push_back(name);
        trgobjPt->push_back(triggerObject.pt());
        trgobjEta->push_back(triggerObject.eta());
        trgobjPhi->push_back(triggerObject.phi());
        trgobjMass->push_back(triggerObject.mass());

      } // end loop over keys/trigger objects passing filters

    } // end loop over filters 
  } else { 
    edm::LogError("DJ_TriggerObjects") << "Error! Can't get the product " << inputTag;
  }

  //------------------------------------------------------------------------
  // Push the information into the event
  //------------------------------------------------------------------------

  iEvent.put ( trgobjPt, "trgobjPt" ) ;
  iEvent.put ( trgobjEta, "trgobjEta" ) ;
  iEvent.put ( trgobjPhi, "trgobjPhi" ) ;
  iEvent.put ( trgobjMass, "trgobjMass" ) ;
  iEvent.put ( trgobjTag, "trgobjTag" ) ;
	      

}

