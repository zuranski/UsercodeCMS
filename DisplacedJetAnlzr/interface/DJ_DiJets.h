#ifndef DJ_DIJETS
#define DJ_DIJETS

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"

//Data Formats and Tools 
#include "DataFormats/PatCandidates/interface/Jet.h"

class DJ_DiJets : public edm::EDProducer {
   public:
      explicit DJ_DiJets(const edm::ParameterSet&);

   private:
      virtual void produce(edm::Event&, const edm::EventSetup&);

      // configurables
      const edm::InputTag patJetCollectionTag_;

};

#endif
