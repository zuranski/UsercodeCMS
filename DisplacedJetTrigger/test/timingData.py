import FWCore.ParameterSet.Config as cms
from UsercodeCMS.DisplacedJetTrigger.myhlt_timing_dataV40 import *

# input source
process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring('file:/uscms/home/zuranski/nobackup/DispJetTrigger/HLT_Physics_179563.root'))

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 )
)
