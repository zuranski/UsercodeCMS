#ifndef DJ_EVENT
#define DJ_EVENT

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
//#include "FWCore/Framework/interface/Frameworkfwd.h"
//#include "FWCore/Framework/interface/Framework.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"

class DJ_Event : public edm::EDProducer {
 public: 
  explicit DJ_Event(const edm::ParameterSet&);
 private: 
  void produce( edm::Event &, const edm::EventSetup & );

  // configurables
  const edm::InputTag patJetCollectionTag_;

  edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
};

#endif

