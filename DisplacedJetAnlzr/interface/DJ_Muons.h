#ifndef DJMuons
#define DJMuons

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

class DJ_Muons : public edm::EDProducer {
 public:
  explicit DJ_Muons(const edm::ParameterSet&);

 private:
  void produce( edm::Event &, const edm::EventSetup & );
  const edm::InputTag   inputTag;
  const std::string     prefix,suffix;
  const unsigned int    maxSize;
  const double          muonIso;
  const std::string     muonID;
  const bool            beamSpotCorr;
  const edm::InputTag   vtxInputTag;
};

#endif

