import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V1::All'
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/uscms_data/d2/zuranski/DispJetTrigger/reco.root'
    )
)

process.demo = cms.EDAnalyzer('DisplacedJetAnlzr'
)


process.p = cms.Path(process.demo)
