import FWCore.ParameterSet.Config as cms
from UsercodeCMS.DisplacedJetTrigger.myhlt_dataV9 import *

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
    tracks = cms.InputTag("hltDisplacedHT250RegionalCtfWithMaterialTracks"),
    l1tracks = cms.InputTag("hltDisplacedHT250L1FastJetRegionalCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltPixelVertices"),
    pfjets = cms.InputTag("hltAntiKT5PFJetsPromptTracks"),
    pftracks = cms.InputTag("hltPFMuonMergingPromptTracks")
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('output.root')
)

process.out = cms.EndPath(process.trigtuple)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 2000 )
)

