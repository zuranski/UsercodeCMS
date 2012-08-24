import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.patTemplate_cfg import process
process.setName_("DJ")
from MyAnalysis.DisplacedJetAnlzr.DJ_options_cff import options
options = options()

process.maxEvents.input = options.maxEvents
process.GlobalTag.globaltag = options.GlobalTag
process.source = cms.Source('PoolSource', fileNames = cms.untracked.vstring(options.files) )
process.add_( cms.Service( "TFileService", fileName = cms.string( options.output ), closeFileFast = cms.untracked.bool(True) ) )

from MyAnalysis.DisplacedJetAnlzr.DJ_nTuple_cfi import DJ
import MyAnalysis.DisplacedJetAnlzr.DJ_ProcessAdjustments_cfi as adjust
adjust.messageLogger(process,options.quiet)
adjust.loadAndConfigureHcalSeverityLevelProducer(process, options.isData)
adjust.loadAndConfigureEcalSeverityLevelProducer(process)
adjust.loadAndConfigureRecoTracker(process) # needed for CheckHitPattern
adjust.loadAndConfigureTrackAssociation(process, options.isData) # needed for TrackAssociators

process.p_DJ  = DJ(process,options).path()

# write this config as a single file
file = open(options.output.replace('.root','_cfg.py'),'w')
file.write(str(process.dumpPython()))
file.close()
