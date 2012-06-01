### Jet ID ###
# https://twiki.cern.ch/twiki/bin/view/CMS/JetID

import FWCore.ParameterSet.Config as cms

process.CaloJetsTightId = cms.EDProducer("CaloJetIdSelector",
    src     = cms.InputTag( "ak5CaloJets" ),                                             
    idLevel = cms.string("TIGHT"),                            
    jetIDMap = cms.untracked.InputTag("ak5JetID")
)

process.PFJetsTightId = cms.EDProducer("PFJetIdSelector",
    src     = cms.InputTag( "ak5PFJets" ),                                             
    idLevel = cms.string("TIGHT")
)

process.JetIDSeq = cms.Sequence(process.CaloJetsTightId * process.PFJetsTightId)
