import FWCore.ParameterSet.Config as cms

process=cms.Process("SKIM")

process.maxEvents = cms.untracked.PSet(
    output = cms.untracked.int32(-1)
    )

process.source = cms.Source('PoolSource',
    fileNames = cms.untracked.vstring(
    '/store/data/Run2011B/MinimumBias/RAW/v1/000/179/563/FCF2D907-BDFD-E011-A5DE-485B3977172C.root')
    )

#skim on HLT path
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
process.filter = hlt.hltHighLevel.clone(
    HLTPaths = ['HLT_Physics_v*'],
    throw = False
    )

process.skim = cms.Path(process.filter)

process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('RAW.root'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('skim')
        )
    )

process.out = cms.EndPath(process.output)
