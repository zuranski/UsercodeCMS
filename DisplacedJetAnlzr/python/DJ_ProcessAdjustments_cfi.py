import FWCore.ParameterSet.Config as cms

def loadAndConfigureHcalSeverityLevelProducer(process, isData) :
    process.load("RecoLocalCalo.HcalRecAlgos.hcalRecAlgoESProd_cfi")
    if isData :
        process.hcalRecAlgos.SeverityLevels[3].RecHitFlags.remove("HFDigiTime")
        process.hcalRecAlgos.SeverityLevels[4].RecHitFlags.append("HFDigiTime")

def loadAndConfigureEcalSeverityLevelProducer(process) :
    process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

def loadAndConfigureRecoTracker(process):
    process.load('RecoTracker.Configuration.RecoTracker_cff')

def loadAndConfigureTrackAssociation(process, isData):
    if not isData:
        process.load('SimTracker.TrackAssociation.TrackAssociatorByHits_cfi')   

def messageLogger(process,quiet) :
    if quiet :
        process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
        for item in [process.MessageLogger.cerr.getParameter(name) for name in process.MessageLogger.cerr.parameterNames_()] :
            if type(item) is cms.PSet :
                item.reportEvery = cms.untracked.int32(1000)
    else :
	process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
	process.MessageLogger.cerr.FwkReport.reportEvery = 1
	process.MessageLogger.cerr.default.limit = 100

