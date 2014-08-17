import FWCore.ParameterSet.Config as cms
from UsercodeCMS.DisplacedJetTrigger.myhlt_timing_mcV40 import *

# input source
process.load('UsercodeCMS.DisplacedJetTrigger.l1htt150_cff')

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 )
)
