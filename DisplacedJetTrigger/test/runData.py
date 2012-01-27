import FWCore.ParameterSet.Config as cms
from MyAnalysis.DisplacedJetTrigger.myhlt_open_dataV47 import *

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# input source

process.source = cms.Source('PoolSource',fileNames = cms.untracked.vstring(
	'/store/user/zuranski/HT/HT250Skim_Run2011B_RAW/37284a6f8e88b94c1b9794dc7bef9083/RAW_10_1_R16.root',
       	'/store/user/zuranski/HT/HT250Skim_Run2011B_RAW/37284a6f8e88b94c1b9794dc7bef9083/RAW_11_1_lH4.root')
	)

process.trigtuple = cms.EDAnalyzer('TriggerTuple',
    jets = cms.InputTag("hltCaloJetCorrected"),
    l1jets = cms.InputTag("hltCaloJetL1FastJetCorrected"),
    tracks = cms.InputTag("unused"),
    vertices = cms.InputTag("unused"),
    pfjets4 = cms.InputTag("hltAntiKT5PFJetsTrk4IterNoMu"),
    pfjets1 = cms.InputTag("hltAntiKT5PFJetsTrk1IterNoMu")
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('output.root')
)

process.out = cms.EndPath(process.trigtuple)

# limit the number of events to be processed
#process.source.skipEvents = cms.untracked.uint32(10000)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 10 )
)
