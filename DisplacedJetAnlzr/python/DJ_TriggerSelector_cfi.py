import FWCore.ParameterSet.Config as cms

paths = [ 
         'HLT_HT250_DoubleDisplacedJet60_v*', 
         'HLT_HT250_DoubleDisplacedJet60_PromptTrack_v*',
         'HLT_HT250_v*',
        ]

import HLTrigger.HLTfilters.hltHighLevel_cfi
djtriggerselector = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
   andOr = True, # accept OR of triggers.
   throw = False, # Don't crash if trigger missing
   HLTPaths = cms.vstring(paths),
   TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
)
