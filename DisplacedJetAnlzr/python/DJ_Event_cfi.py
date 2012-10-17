import FWCore.ParameterSet.Config as cms

djevent = cms.EDProducer("DJ_Event",
    patJetCollectionTag = cms.InputTag("selectedPatJets")
)
