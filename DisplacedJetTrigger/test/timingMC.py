import FWCore.ParameterSet.Config as cms
from MyAnalysis.DisplacedJetTrigger.myhlt_timing_mcV40 import *

# input source
process.load('MyAnalysis.DisplacedJetTrigger.l1htt150_cff')

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 )
)
