#ifndef DJ_EVENT
#define DJ_EVENT

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

class DJ_Event : public edm::EDProducer {
 public: 
  explicit DJ_Event(const edm::ParameterSet&);
 private: 
  void produce( edm::Event &, const edm::EventSetup & );
};

#endif

