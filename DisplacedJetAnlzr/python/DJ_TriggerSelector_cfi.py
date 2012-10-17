import FWCore.ParameterSet.Config as cms

paths = [ 
         'HLT_HT250_DoubleDisplacedJet60_v*', #2011 Run A
         'HLT_HT250_DoubleDisplacedJet60_PromptTrack_v*',#2011 Run B
         'HLT_HT200_v*',#2011
         'HLT_HT250_v*',#2011
         #'HLT_HT250_v*',#2012
         #'HLT_HT300_v*',#2012
         #'HLT_HT300_DoubleDisplacedPFJet60_v*',#2012 7e33
	 #'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v*', #2012 7e33
	 #'HLT_HT300_SingleDisplacedPFJet60_v*', #2012 7e33
	 #'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v*', #2012 7e33
	 #'HLT_HT250_DoubleDisplacedPFJet60_v*', #2012 5e33
	 #'HLT_HT250_DoubleDisplacedPFJet60_ChgFraction10_v*', #2012 5e33
	 #'HLT_HT250_SingleDisplacedPFJet60_v*', #2012 5e33
	 #'HLT_HT250_SingleDisplacedPFJet60_ChgFraction10_v*', #2012 5e33
        ]

import HLTrigger.HLTfilters.hltHighLevel_cfi
djtriggerselector = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
   andOr = True, # accept OR of triggers.
   throw = False, # Don't crash if trigger missing
   HLTPaths = cms.vstring(paths),
   TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)
