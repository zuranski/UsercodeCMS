import FWCore.ParameterSet.Config as cms

process = cms.Process("djtuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.load('HLTrigger.Configuration.HLT_FULL_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V1::All'
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/uscms_data/d2/zuranski/DispJetTrigger/reco.root'
    )
)

process.djtuple = cms.EDAnalyzer('DisplacedJetAnlzr'
)
process.tuple = cms.Path(process.djtuple)

process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.tuple])

