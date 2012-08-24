import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.patTemplate_cfg import process
process.setName_("DJ")
from MyAnalysis.DisplacedJetAnlzr.DJ_options_cff import options
options = options()
print options

process.maxEvents.input = options.maxEvents
process.GlobalTag.globaltag = options.GlobalTag
process.source = cms.Source('PoolSource', fileNames = cms.untracked.vstring(options.files) )
process.add_( cms.Service( "TFileService", fileName = cms.string( options.output ), closeFileFast = cms.untracked.bool(True) ) )

from MyAnalysis.DisplacedJetAnlzr.DJ_nTuple_cfi import DJ
import MyAnalysis.DisplacedJetAnlzr.DJ_ProcessAdjustments_cfi as adjust
adjust.messageLogger(process,options.quiet)
adjust.loadAndConfigureHcalSeverityLevelProducer(process, options.isData)
adjust.loadAndConfigureEcalSeverityLevelProducer(process)
adjust.loadAndConfigureRecoTracker(process)
adjust.loadAndConfigureTrackAssociation(process, options.isData)

#process.p = cms.Path()
#process.p_djPat  = adjust.djPat(process,options)
#process.p_hbheFlag = adjust.addHbheNoiseFilterResult(process,options)
#print process.p
#process.p_fltrFlgs = adjust.addMetFilterFlags(process,options)
process.p_DJ  = DJ(process,options).path()

#dummy = None
#print process.p_djFilters.moduleNames()
#print process.p_djPat.dumpConfig(dummy)

#process.p = process.p_djFilters*process.p_djPat
            #*process.p_hbheFlag
            #*process.p_fltrFlgs
            #*process.p_DJ

# write this config as a single file
file = open(options.output.replace('.root','_cfg.py'),'w')
file.write(str(process.dumpPython()))
file.close()
