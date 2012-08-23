#ifndef DJ_HCALNOISESUMMARYEXISTS
#define DJ_HCALNOISESUMMARYEXISTS

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/METReco/interface/HcalNoiseSummary.h"

class DJ_HcalNoiseSummaryExists : public edm::EDFilter {
 public: 
  explicit DJ_HcalNoiseSummaryExists(const edm::ParameterSet&) {}
 private: 
  bool filter( edm::Event & iEvent, const edm::EventSetup & ) { 
    edm::Handle<HcalNoiseSummary> summary_h;
    iEvent.getByType(summary_h);
    return summary_h.isValid();
  }
};

#endif
