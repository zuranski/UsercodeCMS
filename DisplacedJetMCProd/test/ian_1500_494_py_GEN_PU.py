# Auto generated configuration file
# using: 
# Revision: 1.381.2.2 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: UsercodeCMS/DisplacedJetMCProd/python/ian_1500_494.py -s GEN --conditions START53_V7A::All --pileup 2012_Summer_50ns_PoissonOOTPU --datamix NODATAMIXER --eventcontent AODSIM --datatier AODSIM --no_exec -n 1000
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2012_Summer_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.2 $'),
    annotation = cms.untracked.string('UsercodeCMS/DisplacedJetMCProd/python/ian_1500_494.py nevts:1000'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('ian_1500_494_py_GEN_PU.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AODSIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START53_V7A::All'

process.genParticles = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)


process.printTree = cms.EDAnalyzer("ParticleListDrawer",
    printVertex = cms.untracked.bool(False),
    src = cms.InputTag("genParticlesForFilter"),
    maxEventsToPrint = cms.untracked.int32(10)
)


process.XtoFFbarFilter = cms.EDFilter("XtoFFbarFilter",
    src = cms.InputTag("genParticlesForFilter"),
    idMotherY = cms.vint32(1000022),
    idMotherX = cms.vint32(1000022),
    idDaughterF = cms.vint32(1, 2, 3, 4, 5, 
        6, 11, 13, 15),
    idDaughterG = cms.vint32(1, 2, 3, 4, 5, 
        6, 11, 13, 15)
)


process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(0.0001388),
    UseExternalGenerators = cms.untracked.bool(False),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'pythiaParameters'),
        pythiaParameters = cms.vstring('MSTJ(22)=1             ! Decay all unstable particles', 
            'MSTP(95)=0            ! Disable colour reconnection, since it can put colour strings between widely separated partons', 
            'MSEL=0', 
            'MSUB(271)=1            ! Squark pair production', 
            'MSUB(272)=1', 
            'MSUB(273)=1', 
            'MSUB(274)=1', 
            'MSUB(275)=1', 
            'MSUB(276)=1', 
            'MSUB(277)=1', 
            'MSUB(278)=1', 
            'MSUB(279)=1', 
            'MSUB(280)=1', 
            'IMSS(1)=1                ! General MSSM simultaion', 
            'RMSS(2)=5000.                ! M2 mass', 
            'RMSS(3)=5000.                ! M3 mass', 
            'RMSS(4)=800.                 ! mu parameter', 
            'RMSS(5)=2.                   ! tan Beta', 
            'RMSS(6)=5000.                ! Left slepton mass', 
            'RMSS(7)=5000.                ! Right slepton mass', 
            'RMSS(10)=5000.               ! Left squark mass for third generation', 
            'RMSS(11)=5000.               ! Right sbottom mass', 
            'RMSS(12)=5000.               ! Right stop mass', 
            'RMSS(13)=5000.               ! Left stau mass', 
            'RMSS(14)=5000.               ! Right stau mass', 
            'IMSS(52)=3               ! Turn on Lepton number violating LQD decay channels with all couplings set to zero', 
            'RVLAMP(2,1,1)=0.000075  ! Set lambda Prime(2,1,1)', 
            'MDME(2241,1)=0           ! Turn off LQD decays to neutrinos', 
            'MDME(2242,1)=0           ! Turn off LQD decays to neutrinos', 
            'RMSS(1)=150              ! M1 mass', 
            'RMSS(8)=700              ! Left squark mass', 
            'RMSS(9)=700              ! Right squark mass')
    )
)


process.genParticlesForFilter = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.genParticlesForFilter+process.XtoFFbarFilter+process.printTree)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.AODSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

