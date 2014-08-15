import FWCore.ParameterSet.Config as cms
from UsercodeCMS.DisplacedJetAnlzr.DJ_TriggerSelector_cfi import paths

djtriggers = cms.EDProducer("DJ_Triggers",
                                 InputTag = cms.InputTag('TriggerResults'),
                                 TriggerEventInputTag = cms.InputTag('hltTriggerSummaryAOD'),
				 HLTPaths = cms.vstring(paths),
                                 )

