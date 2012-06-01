import FWCore.ParameterSet.Config as cms

process.CaloJetSelected = cms.EDFilter( "CaloJetSelector",
    src = cms.InputTag( "ak5CaloJetsCorrected" ),
    filter = cms.bool( False ),
    cut = cms.string( "pt>40. && abs(eta)<2." )
)

process.PFJetSelected = cms.EDFilter( "PFJetSelector",
    src = cms.InputTag( "ak5PFJetsCorrected" ),
    filter = cms.bool( False ),
    cut = cms.string( "pt > 40. & abs(eta) < 2.")
)

process.JetSelectorsSeq = cms.Sequence(process.CaloJetSelected * process.PFJetSelected)
