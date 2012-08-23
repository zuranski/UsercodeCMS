#ifndef DJ_TRIGGERS
#define DJ_TRIGGERS

#include <algorithm>

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

class DJ_Triggers : public edm::EDProducer 
{
public: 
  explicit DJ_Triggers(const edm::ParameterSet& conf);

private: 
  edm::InputTag         inputTag;
  HLTConfigProvider     hltConfig;
  edm::InputTag         tag_;
  std::vector<std::string> hltpaths_;
  int                   run_;
  
  void printNames(const std::vector<std::string>& names); 
  void produce( edm::Event& event, const edm::EventSetup& setup);

};

#endif
