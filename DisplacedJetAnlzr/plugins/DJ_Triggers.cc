#include "UsercodeCMS/DisplacedJetAnlzr/interface/DJ_Triggers.h"

DJ_Triggers::DJ_Triggers(const edm::ParameterSet& iConfig)
    : inputTag  (iConfig.getParameter<edm::InputTag>("InputTag"))
    , tag_( iConfig.getParameter<edm::InputTag>("TriggerEventInputTag"))
    , hltpaths_( iConfig.getParameter<std::vector<std::string> >("HLTPaths") )
    , run_(-1) {

    produces <bool> ( "hltHandleValid");
    produces <std::string> ( "hltKey");
    produces <std::map<std::string,bool> >("triggered");
    produces <std::map<std::string,int> > ("prescaled");
    produces <std::map<std::string,std::string> >("hltL1Seeds");

}

void DJ_Triggers::printNames(const std::vector<std::string>& names) {
  for (unsigned int i = 0; i < names.size(); ++i)
    edm::LogProblem( "DJ_Triggers" ) << "  " << names[i] << std::endl;
}

void DJ_Triggers::produce( edm::Event& event, const edm::EventSetup& setup) {

  if ( int(event.getRun().run()) != run_ ) {
    // Set process name using method here: https://hypernews.cern.ch/HyperNews/CMS/get/physTools/1791/1/1/1/1/1/2.html
    if ( inputTag.process().empty() ) { 
      edm::Handle<trigger::TriggerEvent> temp;
      event.getByLabel( tag_, temp );
      if( temp.isValid() ) { inputTag = edm::InputTag( inputTag.label(), inputTag.instance(), temp.provenance()->processName() ); }
      else { edm::LogError( "DJ_Triggers" ) << "[DJ::produce] Cannot retrieve TriggerEvent product for " << tag_; }
    }
    // Initialise HLTConfigProvider
    bool  hltChanged = false;
    if (!hltConfig.init(event.getRun(), setup, inputTag.process(), hltChanged) ) {
      edm::LogError( "DJ_Triggers" ) << "HLT config initialization error with process name \"" << inputTag.process() << "\".";
    } else if ( hltConfig.size() < 1 ) {
      edm::LogError( "DJ_Triggers" ) << "HLT config has zero size.";
    }
  }

  // Retrieve TriggerResults with appropriate InputTag
  edm::Handle<edm::TriggerResults> results;
  event.getByLabel( inputTag, results ); 

  std::auto_ptr<std::map<std::string,bool> > triggered(new std::map<std::string,bool>());
  std::auto_ptr<std::map<std::string,int> >  prescaled(new std::map<std::string,int>());
  std::auto_ptr<std::map<std::string,std::string> > hltL1Seeds(new std::map<std::string,std::string>());

  if(results.isValid()) {
    const edm::TriggerNames& names = event.triggerNames(*results);
    for(unsigned i=0; i < results->size(); i++) {

      // is it an interesting trigga
      bool interestingTrigger = false;
      for (unsigned int j=0; j<hltpaths_.size(); j++){
        // match with the triggerName, remove last character which is a wildcard *
        if(names.triggerName(i).find(hltpaths_[j].substr(0,hltpaths_[j].size()-1)) != std::string::npos) {
          interestingTrigger = true;
          break;
        }
      }
      if (!interestingTrigger) continue;

      unsigned int prescale = hltConfig.prescaleValue(event,setup,names.triggerName(i));
      bool accept = results->accept(i);
      // check if triggered failed on a prescaler
      if (prescale>1 && !accept){
        const std::string& moduleLabel = hltConfig.moduleLabel(i,results->index(i));
        const std::string& moduleType = hltConfig.moduleType(moduleLabel);
        if (moduleType=="HLTPrescaler" || moduleType=="TriggerResultsFilter") continue;
      }
      
      (*prescaled)[names.triggerName(i)] = hltConfig.prescaleValue(event,setup,names.triggerName(i));
      (*triggered)[names.triggerName(i)] = results->accept(i) ;
      const std::vector<std::pair<bool,std::string> >&  l1Seeds = hltConfig.hltL1GTSeeds(i);
      if (l1Seeds.size() == 1) {
        (*hltL1Seeds)[names.triggerName(i)]  = l1Seeds.front().second;
      }
      else if (l1Seeds.size() > 1) {
        std::string   combined;
        for (unsigned iSeed = 0; iSeed < l1Seeds.size(); ++iSeed) {
          if (combined.length())  combined += " OR ";
          combined   += "("+l1Seeds[iSeed].second+")";
        } // end loop over L1 seeds
        (*hltL1Seeds)[names.triggerName(i)]  = combined;
      }
    }
  } else { edm::LogError( "DJ_Triggers" ) << "[DJ::produce] Cannot retrieve TriggerResults product for " << inputTag; }

  event.put( std::auto_ptr<bool>(new bool(results.isValid())), "hltHandleValid");
  event.put( std::auto_ptr<std::string>(new std::string(hltConfig.tableName())), "hltKey");
  event.put( triggered,"triggered");
  event.put( prescaled,"prescaled");
  event.put( hltL1Seeds,"hltL1Seeds");
}
