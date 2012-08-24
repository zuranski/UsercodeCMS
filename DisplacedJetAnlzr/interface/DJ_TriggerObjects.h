#ifndef DJ_TRIGGEROBJECTS
#define DJ_TRIGGEROBJECTS

#include <string> 

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"

#include "MyAnalysis/DisplacedJetAnlzr/interface/trgobj.h"

class DJ_TriggerObjects : public edm::EDProducer {
 public:
  explicit DJ_TriggerObjects(const edm::ParameterSet&);

 private:
  void produce( edm::Event &, const edm::EventSetup & );
  const edm::InputTag   inputTag;
  std::vector<std::string> ObjectsToStore;

};

#endif

