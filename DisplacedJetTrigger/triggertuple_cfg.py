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
    hltcorjets = cms.InputTag("hltCaloJetCorrected"),
    selectedjets = cms.InputTag("hltAntiKT5L2L3CorrCaloJetsPt60Eta2"),
    tracks = cms.InputTag("hltDisplacedHT250RegionalCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltPixelVertices"),
    pfjets = cms.InputTag("hltAntiKT5PFJets")
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('TrigTuple.root')
)

process.p = cms.Path(process.genParticles + process.trigtuple)
