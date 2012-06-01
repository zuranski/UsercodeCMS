### Jet Corections  ###

process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak5CaloJetsCorrected = process.ak5CaloJetsL1L2L3Residual.clone( src = "CaloJetsTightId" )
process.ak5PFJetsCorrected = process.ak5PFJetsL1L2L3Residual.clone( src = "PFJetsTightId" )

process.JetCorrectionsSeq = cms.Sequence(process.ak5CaloJetsCorrected * process.ak5PFJetsCorrected)
