import FWCore.ParameterSet.Config as cms
from MyAnalysis.DisplacedJetAnlzr.listAllFiles import *
import sys,os

# config options (u,q,d)
try:
    nEvents = int(sys.argv[-1])
    dataType = sys.argv[-2]
except ValueError:
    nEvents = -1
    dataType = sys.argv[-1]
    
process = cms.Process('hltreco')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('RecoTracker.Configuration.RecoTracker_cff')
#process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#build transient tracks
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

# Input source
readFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",fileNames = readFiles)

if dataType == "u" or dataType == "b":
   listAllFilesDBS(readFiles, "/HTo2LongLivedTo4F_MH-400_MFF-150_CTau-400_7TeV-pythia6/Fall11-DEBUG-PU_S6_START44_V9B-v4/GEN-SIM-RECODEBUG",10,1)
elif dataType == "q120":
   listAllFilesDBS(readFiles, "/QCD_Pt-120to170_TuneZ2_7TeV_pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",10)
elif dataType == "q170":
   listAllFilesDBS(readFiles, "/QCD_Pt-170to300_TuneZ2_7TeV_pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",10)
elif dataType == "q300":
   listAllFilesDBS(readFiles, "/QCD_Pt-300to470_TuneZ2_7TeV_pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",10)
elif dataType == "d":
   listAllFilesDBS(readFiles, "/HT/Run2011B-19Nov2011-v1/RECO",100)

if dataType=="d":
   process.GlobalTag.globaltag = 'FT_R_44_V11::All'
   process.load('MyAnalysis.DisplacedJetAnlzr.run177782_cff')
   import PhysicsTools.PythonAnalysis.LumiList as LumiList
   import FWCore.ParameterSet.Types as CfgTypes
   myLumis = LumiList.LumiList(filename = 'goodList.json').getCMSSWString().split(',')
   process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
   process.source.lumisToProcess.extend(myLumis)
else:
   process.GlobalTag.globaltag = 'START44_V9B::All'

process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(nEvents)
)

htHLTpath = [ 'HLT_HT250_DoubleDisplacedJet60_v*', 'HLT_HT250_DoubleDisplacedJet60_PromptTrack_v*','HLT_HT250_v*']
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.skimUsingHLT = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
   andOr = True, # accept OR of triggers.
   throw = False, # Don't crash if trigger missing
   HLTPaths = cms.vstring(htHLTpath),
   TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)

# run simple ntupler
process.djtuple = cms.EDAnalyzer('DisplacedJetAnlzr',
    hlttag = cms.InputTag("TriggerResults","","HLT"),
    debugoutput = cms.bool(False),
    useTP = cms.bool(True),
    vertexfitter = cms.PSet(
        finder = cms.string('avf')
        #sigmacut = cms.double(10.0),
        #Tini = cms.double(256.0),
        #ratio = cms.double(0.25),
        #maxDistance = cms.double(0.001),
        #maxNbrOfIteration = cms.int32(30)
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('ntuple'+dataType+'.root')
)

#options
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)


### Signal MC filter for displaced jets
execfile("../python/SignalMCFilter_cfg.py")

### Clean up filters (scraping, HBHE noise, good PV)
execfile("../python/CleanUpFilters_cfg.py")

### jet energy corrections as recommended by JEC group ###
if dataType == "d":
    execfile("../python/JetCorrectionsData_cfg.py")
else:
    execfile("../python/JetCorrectionsMC_cfg.py")
##########################################################

### Jet ID selections ###
execfile("../python/JetID_cfg.py")
#########################

### Jet selectors ###
execfile("../python/JetSelectors_cfg.py")

process.tuple = cms.Path()

if dataType == "u" or dataType == "b":
	process.tuple*=process.filterSignalMCSeq

if dataType == "d":
	process.tuple*=process.skimUsingHLT
	process.tuple*=process.CleanUpDataSeq
else:
	process.tuple*=process.CleanUpMCSeq


process.tuple*=process.JetIDSeq
process.tuple*=process.JetCorrectionsSeq
process.tuple*=process.JetSelectorsSeq
process.tuple*=process.djtuple

