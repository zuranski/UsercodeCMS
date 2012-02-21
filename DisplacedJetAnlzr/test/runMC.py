import FWCore.ParameterSet.Config as cms

process = cms.Process('hltreco')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.EventContent.EventContent_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
#process.load('HLTrigger.Configuration.HLT_GRun_cff')
#process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#build transient tracks
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

# Input source
process.load('MyAnalysis.DisplacedJetAnlzr.MH_400_MFF_50_CTau80_cff')

# Track MC match
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")
process.TrackAssociatorByHits.Cut_RecoToSim = cms.double(0.5)

#process.source = cms.Source('PoolSource',fileNames = cms.untracked.vstring(
#    'file:/uscms_data/d2/zuranski/DispJetTrigger/reco.root'
#    )
#)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Other statements
process.GlobalTag.globaltag = 'START52_V1::All'

process.djtuple = cms.EDAnalyzer('DisplacedJetAnlzr',
    debugoutput = cms.bool(True),
    hlttag = cms.InputTag("TriggerResults","","HLT"),
    vertexreco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(15.0),
        primT = cms.double(256.0),
        primr = cms.double(0.25),
        seccut = cms.double(15.0),
        secT = cms.double(256.0),
        secr = cms.double(0.25),
        minweight = cms.double(0.5),
        weightthreshold = cms.double(0.1 ),
        smoothing = cms.bool(True)

    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('ntuple.root')
)

process.tuple = cms.Path(process.djtuple)
# Schedule definition
#process.schedule = cms.Schedule(process.HLTSchedule)
#process.schedule.extend([process.tuple])
