#ifndef DJ_GENEVENT
#define DJ_GENEVENT

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/Candidate/interface/Candidate.h"

class DJ_GenEvent : public edm::EDProducer {
 public: 
  explicit DJ_GenEvent(const edm::ParameterSet&);
 private: 
  void produce( edm::Event &, const edm::EventSetup & );
};

#endif

