import FWCore.ParameterSet.Config as cms

# module to select Jets
# See https://twiki.cern.ch/twiki/bin/view/CMS/SWGuidePhysicsCutParser
# on how to use the cut-string
#
trackerPatJets = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("selectedPatJets"),
    cut = cms.string("abs(eta)<2.")
)
