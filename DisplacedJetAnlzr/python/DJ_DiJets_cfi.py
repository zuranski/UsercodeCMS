import FWCore.ParameterSet.Config as cms
from UsercodeCMS.DisplacedJetAnlzr.DJ_Jets_cfi import jetColl

djdijets = cms.EDProducer('DJ_DiJets',
    patJetCollectionTag = cms.InputTag(jetColl)
)
