// -*- C++ -*-
//
// Package:    DisplacedJetAnlzr
// Class:      DisplacedJetAnlzr
// 
/**\class DisplacedJetAnlzr DisplacedJetAnlzr.cc MyAnalysis/DisplacedJetAnlzr/src/DisplacedJetAnlzr.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andrzej Zuranski
//         Created:  Thu Feb 16 09:43:08 CST 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

//
// class declaration
//

class DisplacedJetAnlzr : public edm::EDAnalyzer {
   public:
      explicit DisplacedJetAnlzr(const edm::ParameterSet&);
      ~DisplacedJetAnlzr();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DisplacedJetAnlzr::DisplacedJetAnlzr(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

}


DisplacedJetAnlzr::~DisplacedJetAnlzr()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DisplacedJetAnlzr::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   std::vector<std::string> triggers;

   HLTConfigProvider hltConfig;
   bool changed;
   hltConfig.init(iEvent.getRun(),iSetup,"hltreco",changed);

   edm::Handle<edm::TriggerResults> hltResults;
   iEvent.getByLabel(edm::InputTag("TriggerResults","","hltreco"),hltResults);
   const std::vector< std::string > &trgNames = hltConfig.triggerNames();

   for (size_t i=0;i<hltResults->size();i++)
	if (hltResults->accept(i))
	 triggers.push_back(trgNames.at(i));

   for (size_t i=0;i<triggers.size();i++)
     std::cout << triggers.at(i) << std::endl;

}


// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedJetAnlzr::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DisplacedJetAnlzr::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
DisplacedJetAnlzr::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DisplacedJetAnlzr::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
DisplacedJetAnlzr::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
DisplacedJetAnlzr::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DisplacedJetAnlzr::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedJetAnlzr);
