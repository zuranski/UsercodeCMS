import FWCore.ParameterSet.Config as cms

process = cms.Process("Analysis")

process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#build transient tracks
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

process.GlobalTag.globaltag = 'START3X_V26A::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/tigress-hsm/zuranski/work/cms/data/FullSim/MinBias_Dstar_7TeV/K3pi/reco2data-1.root'
        #'file:/tigress-hsm/zuranski/work/cms/releases/CMSSW_3_5_6/src/Analysis/DSD0analyzer/MinBias.root'
        #'/store/mc/Spring10/MinBias/GEN-SIM-RECO/START3X_V25_356ReReco-v2/0123/C86FED5C-AC3B-DF11-A1BC-002618943898.root',
        #'/store/mc/Spring10/MinBias/GEN-SIM-RECO/START3X_V25_356ReReco-v2/0123/C4A5C01A-AD3B-DF11-A37A-001A92971B7E.root'
        #'file:/tigress-hsm/phedex/store/data/BeamCommissioning09/MinimumBias/RAW-RECO/BSCNOBEAMHALO-Dec19thSkim_336p3_v1/0006/7CA100C2-D7EE-DE11-BCC3-001D0967D643.root'
    )
)

process.analysis = cms.EDAnalyzer('DSD0Analyzer',
    doGen=cms.bool(True),
    doKpi=cms.bool(True),
    doK3pi=cms.bool(True)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('Dtracks.root')
)

process.p = cms.Path(
  process.analysis
)

