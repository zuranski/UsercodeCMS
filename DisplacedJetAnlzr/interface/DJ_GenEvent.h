#ifndef DJ_GENEVENT
#define DJ_GENEVENT

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
//#include "DataFormats/JetReco/src/Jet.cc"

class DJ_GenEvent : public edm::EDProducer {
 public: 
  explicit DJ_GenEvent(const edm::ParameterSet&);
 private: 
  void produce( edm::Event &, const edm::EventSetup & );
  const reco::Candidate* deepMother(const reco::Candidate* p);
  void assignStableDaughters(const reco::Candidate* p, std::vector<int> & pids);
  void FindBDaughter(const reco::Candidate* p, std::vector<const reco::Candidate*> & Bs);
  std::vector<const reco::Candidate*> FindB(std::vector<const reco::Candidate*> Bs, int pdgId);
};

#endif

