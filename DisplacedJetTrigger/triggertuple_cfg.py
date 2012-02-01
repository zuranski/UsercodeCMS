import FWCore.ParameterSet.Config as cms

process = cms.Process("Trig")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.options = cms.untracked.PSet(
	SkipEvent = cms.untracked.vstring('ProductNotFound')	
)

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/uscms_data/d2/zuranski/DispJetTrigger/S11hlt.root'
    )
)


process.load( "SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.genParticles = cms.EDProducer("GenParticleProducer",src = cms.InputTag("generator"))

process.trigtuple = cms.EDAnalyzer('TriggerTuple',
    jets = cms.InputTag("hltCaloJetCorrected"),
    l1jets = cms.InputTag("hltCaloJetL1FastJetCorrected"),
    tracks = cms.InputTag("hltDisplacedHT250RegionalCtfWithMaterialTracks"),
    l1tracks = cms.InputTag("hltDisplacedHT250L1FastJetRegionalCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltPixelVertices"),
    pfjets = cms.InputTag("hltAntiKT5PFJetsTrk4IterNoMu"),
    pftracks = cms.InputTag("hltIter3Merged")
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('TrigTuple.root')
)

process.p = cms.Path(process.genParticles + process.trigtuple)
