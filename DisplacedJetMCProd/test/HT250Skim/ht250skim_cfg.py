import FWCore.ParameterSet.Config as cms

process=cms.Process("SKIM")

process.maxEvents = cms.untracked.PSet(
    output = cms.untracked.int32(-1)
    )

process.source = cms.Source('PoolSource',
    fileNames = cms.untracked.vstring(
    '/store/data/Run2011B/HT/RAW/v1/000/180/250/F69F7EDF-FD02-E111-979A-BCAEC5329724.root',
    '/store/data/Run2011B/HT/RAW/v1/000/180/250/EE15A15C-F502-E111-9553-003048D373F6.root',
    '/store/data/Run2011B/HT/RAW/v1/000/180/250/DC459082-FE02-E111-8847-BCAEC532970A.root')
    )

#skim on HLT path
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
process.filter = hlt.hltHighLevel.clone(
    HLTPaths = ['HLT_HT250_v*'],
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
