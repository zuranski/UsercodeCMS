import FWCore.ParameterSet.Config as cms

jetColl = "trackerPatJets"

djjets = cms.EDProducer('DJ_Jets',
    patJetCollectionTag = cms.InputTag(jetColl)
)
