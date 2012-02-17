import FWCore.ParameterSet.Config as cms

process = cms.Process('hltreco')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# Input source
process.load('MyAnalysis.DisplacedJetAnlzr.MH_400_MFF_150_CTau400_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Other statements
process.GlobalTag.globaltag = 'START52_V1::All'

process.djtuple = cms.EDAnalyzer('DisplacedJetAnlzr')

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('ntuple.root')
)

process.tuple = cms.EndPath(process.djtuple)
# Schedule definition
process.schedule = cms.Schedule(process.HLTSchedule)
process.schedule.extend([process.tuple])
