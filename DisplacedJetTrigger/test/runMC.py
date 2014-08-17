import FWCore.ParameterSet.Config as cms
from UsercodeCMS.DisplacedJetTrigger.myhlt_mcV9 import *

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
process.load('UsercodeCMS.DisplacedJetTrigger.MH_400_MFF_150_CTau400_cff')

# genParticles
process.load( "SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.genParticles = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    abortOnUnknownPDGCode = cms.untracked.bool(False))

# TriggerTuple
process.trigtuple = cms.EDAnalyzer('TriggerTuple',
    jets = cms.InputTag("hltCaloJetCorrected"),
    l1jets = cms.InputTag("hltCaloJetL1FastJetCorrected"),
    tracks = cms.InputTag("hltDisplacedHT300RegionalCtfWithMaterialTracks"),
    l1tracks = cms.InputTag("hltDisplacedHT300L1FastJetRegionalCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltPixelVertices"),
    pfjets = cms.InputTag("hltAntiKT5PFJetsPromptTracks"),
    pftracks = cms.InputTag("hltPFMuonMergingPromptTracks")
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('output1.root')
)

process.out = cms.EndPath(process.genParticles + process.trigtuple)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 200 )
)

