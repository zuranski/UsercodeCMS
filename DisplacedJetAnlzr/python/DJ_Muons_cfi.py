import FWCore.ParameterSet.Config as cms

djmuons = cms.EDProducer("DJ_Muons",
    InputTag = cms.InputTag('selectedPatMuons'),
    Prefix = cms.string('muon'),
    Suffix = cms.string(''),
    MaxSize = cms.uint32(10),
    MuonIso = cms.double(0.05),
    MuonID = cms.string('GlobalMuonPromptTight'),
    BeamSpotCorr = cms.bool(True),
    VertexInputTag = cms.InputTag('offlinePrimaryVertices'),
)
