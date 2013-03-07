import FWCore.ParameterSet.Config as cms

djpileupsummary = cms.EDProducer("DJ_PileupSummary",
                                      InputTag = cms.InputTag('addPileupInfo'),
                                      PDFCTEQWeightsInputTag   = cms.InputTag('pdfWeights','CT10'),
                                      PDFMSTWWeightsInputTag   = cms.InputTag('pdfWeights','MSTW2008nlo68cl'),
                                      PDFNNPDFWeightsInputTag   = cms.InputTag('pdfWeights','NNPDF20'),
                                      Prefix = cms.string('pileup'),
                                      Suffix = cms.string(''),
                                      )

