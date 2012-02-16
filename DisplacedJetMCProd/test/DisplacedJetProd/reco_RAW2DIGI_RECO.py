# Auto generated configuration file
# using: 
# Revision: 1.357 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,RECO --filein /store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_100_1_LxF.root --fileout reco.root --conditions START52_V1::All -n 5 --no_exec --eventcontent FEVTDEBUG --datatier GEN-SIM-RECOEBUG
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_100_1_LxF.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.357 $'),
    annotation = cms.untracked.string('reco nevts:5'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    fileName = cms.untracked.string('reco.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECOEBUG')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START52_V1::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.FEVTDEBUGoutput_step)

