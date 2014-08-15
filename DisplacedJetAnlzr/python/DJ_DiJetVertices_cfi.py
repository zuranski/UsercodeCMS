import FWCore.ParameterSet.Config as cms
from UsercodeCMS.DisplacedJetAnlzr.DJ_Jets_cfi import jetColl

djdijetvertices = cms.EDProducer('DJ_DiJetVertices',
    patJetCollectionTag = cms.InputTag(jetColl),
    useTrackingParticles = cms.bool(True),
    PromptTrackDxyCut = cms.double(0.05), # 500 microns
    TrackPtCut = cms.double(1.),
    PV = cms.uint32(0),
    TrackingEfficiencyFactor = cms.double(1.),
    vtxWeight = cms.double(0.5),
    vertexfitter = cms.PSet(
        fitter = cms.string('avf')
    )
)
