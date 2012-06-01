### Jet Corections  ### as recommended by JEC group
# https://twiki.cern.ch/twiki/bin/view/CMS/IntroToJEC#Mandatory_Jet_Energy_Corrections
 
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.ak5CaloJetsCorrected = process.ak5CaloJetsL1L2L3.clone( src = "CaloJetsTightId" )
process.ak5PFJetsCorrected = process.ak5PFJetsL1L2L3.clone( src = "PFJetsTightId" )

process.JetCorrectionsSeq = cms.Sequence(process.ak5CaloJetsCorrected * process.ak5PFJetsCorrected)
