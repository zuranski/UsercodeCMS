import FWCore.ParameterSet.Config as cms

djpileupsummary = cms.EDProducer("DJ_PileupSummary",
                                      InputTag = cms.InputTag('addPileupInfo'),
                                      Prefix = cms.string('pileup'),
                                      Suffix = cms.string(''),
                                      )

