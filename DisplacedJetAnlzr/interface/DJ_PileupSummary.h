#ifndef DJ_PILEUPSUMMARY
#define DJ_PILEUPSUMMARY

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

class DJ_PileupSummary : public edm::EDProducer {
 public: 
  explicit DJ_PileupSummary(const edm::ParameterSet&);
 private: 
  void produce( edm::Event &, const edm::EventSetup & );
  const edm::InputTag inputTag,pdfCTEQWeightsInputTag,pdfMSTWWeightsInputTag,pdfNNPDFWeightsInputTag;
  const std::string Prefix,Suffix;
};

#endif
