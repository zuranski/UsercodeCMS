# As documented in https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCollisionsDataAnalysis

# This requires Tracker voltage on.
process.load('HLTrigger.special.hltPhysicsDeclared_cfi')
process.hltPhysicsDeclared.L1GtReadoutRecordTag = 'gtDigis'

# Good P.V.
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(15), 
                                           maxd0 = cms.double(2) 
                                           )


# beam scraping
process.noscraping = cms.EDFilter("FilterOutScraping",
                                applyfilter = cms.untracked.bool(True),
                                debugOn = cms.untracked.bool(False),
                                numtrack = cms.untracked.uint32(10),
                                thresh = cms.untracked.double(0.25)
                                )

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

process.CleanUpDataSeq = cms.Sequence(process.hltPhysicsDeclared *
                                       process.primaryVertexFilter * process.noscraping * process.HBHENoiseFilter)
process.CleanUpMCSeq = cms.Sequence(process.primaryVertexFilter * process.noscraping * process.HBHENoiseFilter)
