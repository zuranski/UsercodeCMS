#ifndef DJ_EVENTFILTERS
#define DJ_EVENTFILTERS

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GtFdlWord.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/METReco/interface/HcalNoiseSummary.h"
#include "DataFormats/METReco/interface/BeamHaloSummary.h"

class DJ_EventFilters : public edm::EDProducer {
 public:
  explicit DJ_EventFilters(const edm::ParameterSet&);

 private:
  void produce( edm::Event &, const edm::EventSetup & );
  const edm::InputTag   l1InputTag,vtxInputTag;
  const unsigned int    vtxMinNDOF;
  const double          vtxMaxAbsZ, vtxMaxd0;
  const edm::InputTag   trkInputTag;
  const unsigned int    numTracks;
  const double          hpTrackThreshold;
  const edm::InputTag   hcalNoiseInputTag;
  const edm::InputTag   beamHaloInputTag;

  const edm::InputTag trackingFilterJetInputTag   ;
  const double trackingFilterDzTrVtxMax    ;
  const double trackingFilterDxyTrVtxMax   ;
  const double trackingFilterMinSumPtOverHT;

  const edm::InputTag   ecalMaskedCellDRFilterInputTag , caloBoundaryDRFilterInputTag;
  //
  const edm::InputTag   hcalLaserEventFilterInputTag , ecalDeadCellTriggerPrimitiveFilterInputTag , ecalDeadCellBoundaryEnergyFilterInputTag;
  const edm::InputTag   trackingFailureFilterInputTag , badEESupercrystalFilterInputTag, ecalLaserCorrFilterInputTag;
};

#endif
