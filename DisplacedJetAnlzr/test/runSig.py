import FWCore.ParameterSet.Config as cms
from MyAnalysis.DisplacedJetAnlzr.myhlt_open_mcV18 import *

process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')

#build transient tracks
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

# Input source
process.load('MyAnalysis.DisplacedJetAnlzr.MH_400_MFF_150_CTau400_cff')

# Track MC match
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")
process.TrackAssociatorByHits.Cut_RecoToSim = cms.double(0.5)

#process.source = cms.Source('PoolSource',fileNames = cms.untracked.vstring(
#    'file:/uscms_data/d2/zuranski/DispJetTrigger/reco.root'
#    )
#)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(15)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
)

process.djtuple = cms.EDAnalyzer('DisplacedJetAnlzr',
    debugoutput = cms.bool(False),
    useTP = cms.bool(True),
    hlttag = cms.InputTag("TriggerResults","","hltreco"),
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

process.tuple = cms.EndPath(process.djtuple)
