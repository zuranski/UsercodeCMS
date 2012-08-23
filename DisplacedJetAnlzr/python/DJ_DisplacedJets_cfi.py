import FWCore.ParameterSet.Config as cms

djdisplacedjets = cms.EDProducer('DJ_DisplacedJets',
    patJetCollectionTag = cms.InputTag("selectedPatJets"),
    useTrackingParticles = cms.bool(True),
    PromptTrackDxyCut = cms.double(0.05), # 500 microns
    TrackPtCut = cms.double(1.),
    vertexfitter = cms.PSet(
        fitter = cms.string('avf')
    )
)
