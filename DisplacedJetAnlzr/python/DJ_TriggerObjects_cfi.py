import FWCore.ParameterSet.Config as cms

objects = [
	   'hlt2DisplacedHT250L3Filter',#2011 Run A
           'hlt2DisplacedHT2501PTrkL3Filter',#2011 Run B
           'hlt2DisplacedHT250L1FastJetL3Filter',#2012
           'hlt1DisplacedHT250L1FastJetL3Filter',#2012
           'hlt2DisplacedHT300L1FastJetL3Filter',#2012
           'hlt1DisplacedHT300L1FastJetL3Filter',#2012
	   'hlt2PFDisplacedJetsPt50', #2012
	   'hlt1PFDisplacedJetsPt50', #2012
	   'hlt2PFDisplacedJetsPt60ChgFraction10', #2012
	   'hlt1PFDisplacedJetsPt60ChgFraction10', #2012
]

djtriggerobjects= cms.EDProducer("DJ_TriggerObjects",
    InputTag = cms.InputTag('hltTriggerSummaryAOD',"","HLT"),
    ObjectsToStore = cms.vstring(objects)
)
