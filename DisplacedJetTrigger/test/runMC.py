import FWCore.ParameterSet.Config as cms
from MyAnalysis.DisplacedJetTrigger.myhlt_open_mcV47 import *

# Select exotics decaying to qq or bb.
process.filterMC = cms.EDFilter('MCParticlePairFilter',
    ParticleID1 = cms.untracked.vint32(6000111,6000112),
    ParticleID2 = cms.untracked.vint32(6000111,6000112)
)
#process.p = cms.Path(process.filterMC)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# input source
process.load('MyAnalysis.DisplacedJetTrigger.MH_400_MFF_150_CTau400_cff')

# genParticles
process.load( "SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.genParticles = cms.EDProducer("GenParticleProducer",src = cms.InputTag("generator"))

# TriggerTuple
process.trigtuple = cms.EDAnalyzer('TriggerTuple',
    jets = cms.InputTag("hltCaloJetCorrected"),
    l1jets = cms.InputTag("hltCaloJetL1FastJetCorrected"),
    tracks = cms.InputTag("unused"),
    vertices = cms.InputTag("unused"),
    pfjets4 = cms.InputTag("hltAntiKT5PFJetsTrk4IterNoMu"),
    pfjets1 = cms.InputTag("hltAntiKT5PFJetsTrk1IterNoMu")
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('output1.root')
)

process.out = cms.EndPath(process.genParticles + process.trigtuple)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 20 )
)
