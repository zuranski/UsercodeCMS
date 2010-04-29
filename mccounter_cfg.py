import FWCore.ParameterSet.Config as cms
                                                                                                                                                             
process = cms.Process("counter")
                                                                                                                                                             
process.load("FWCore.MessageService.MessageLogger_cfi")
                                                                                                                                                             
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
                                                                                                                                                             
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/tigress-hsm/zuranski/work/cms/releases/CMSSW_3_5_6/src/Analysis/DSD0analyzer/MinBias.root'
    )
)
                                                                                                                                                             
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('MCCounter.root')
)
                                                                                                                                                             
process.counter = cms.EDAnalyzer('MCCounter'
)
                                                                                                                                                             
                                                                                                                                                             
process.p = cms.Path(process.counter)
