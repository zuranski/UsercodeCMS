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

def djPat(process,options) :

    from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching,removeCleaning,restrictInputToAOD,removeAllPATObjectsBut
    from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection 

    if options.isData: removeMCMatching(process, ['All'])
    restrictInputToAOD(process)
    removeCleaning(process)
    removeAllPATObjectsBut(process, ['Jets','METs'])
    switchJetCollection(process,
			cms.InputTag('ak5PFJets'),
			doJTA = True,
			doBTagging = True,
			doJetID = True,
			jetCorrLabel = ('AK5PF',options.jetCorrections),
			genJetCollection = cms.InputTag('ak5GenJets'),
			doType1MET = False,
			jetIdLabel = 'ak5pf'
                       )

    process.selectedPatJets.cut = cms.string("pt > 40 & abs(eta) < 2.0 && neutralHadronEnergyFraction < 0.9 && neutralEmEnergyFraction < 0.90 && chargedHadronEnergyFraction>0 && chargedHadronMultiplicity > 0 && chargedEmEnergyFraction < 0.99 && nConstituents > 2")

    del process.out
    del process.outpath
    return cms.Path(process.patDefaultSequence)

def addHbheNoiseFilterResult(process, options) :
    process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')
    process.HBHENoiseFilterResultProducerNoIso = process.HBHENoiseFilterResultProducer.clone( minIsolatedNoiseSumE = 999999.0,
                                                                                              minNumIsolatedNoiseChannels = 999999,
                                                                                              minIsolatedNoiseSumEt = 999999.0  )
    process.hcalNoiseSummaryExists = cms.EDFilter('DJ_HcalNoiseSummaryExists')
    return cms.Path(process.hcalNoiseSummaryExists + process.HBHENoiseFilterResultProducer + process.HBHENoiseFilterResultProducerNoIso )

def addMetFilterFlags(process, options) :
    # https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
    from RecoMET.METFilters.trackingFailureFilter_cfi import trackingFailureFilter
    from RecoMET.METFilters.hcalLaserEventFilter_cfi import hcalLaserEventFilter
    from RecoMET.METFilters.inconsistentMuonPFCandidateFilter_cfi import inconsistentMuonPFCandidateFilter
    from RecoMET.METFilters.greedyMuonPFCandidateFilter_cfi import greedyMuonPFCandidateFilter
    from RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi import EcalDeadCellTriggerPrimitiveFilter
    from RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi import EcalDeadCellBoundaryEnergyFilter

    process.trackingFailureFilterFlag = trackingFailureFilter.clone(taggingMode = True)#, quiet = True)
    process.hcalLaserEventFilterFlag = hcalLaserEventFilter.clone(taggingMode = True)
    process.greedyMuonPFCandidateFilterFlag = greedyMuonPFCandidateFilter.clone(taggingMode = True)
    process.inconsistentMuonPFCandidateFilterFlag = inconsistentMuonPFCandidateFilter.clone(taggingMode = True)
    process.ecalDeadCellTPFilterFlag = EcalDeadCellTriggerPrimitiveFilter.clone(taggingMode = True)
    process.ecalDeadCellBEFilterFlag = EcalDeadCellBoundaryEnergyFilter.clone(taggingMode = True,
                                                                              cutBoundEnergyDeadCellsEB = 10.0,
                                                                              cutBoundEnergyDeadCellsEE = 10.0,
                                                                              cutBoundEnergyGapEB = 100.0,
                                                                              cutBoundEnergyGapEE = 100.0,
                                                                              enableGap = False,
                                                                              limitDeadCellToChannelStatusEB = cms.vint32(12,14),
                                                                              limitDeadCellToChannelStatusEE = cms.vint32(12,14))

    return cms.Path( process.trackingFailureFilterFlag *
                     process.hcalLaserEventFilterFlag *
                     process.greedyMuonPFCandidateFilterFlag *
                     process.inconsistentMuonPFCandidateFilterFlag *
                     process.ecalDeadCellTPFilterFlag
                     # * process.ecalDeadCellBEFilterFlag # product not found : EcalRecHitsEB
                     )

