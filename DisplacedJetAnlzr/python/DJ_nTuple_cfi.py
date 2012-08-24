import FWCore.ParameterSet.Config as cms

class DJ(object) :
    def __init__(self,process,options) :
        self.process = process
        self.options = options
        self.empty = process.empty = cms.Sequence()

    def path(self) :
        return cms.Path(  self.initialFilters()
                         *self.HbheNoiseFilterResult()
			 #*self.MetFilterFlags()
                         *self.Pat()
                         *self.common() 
                         * self.tree() )
    
    def tree(self) :
        self.process.djTree = cms.EDAnalyzer("DJTree", outputCommands = cms.untracked.vstring(
            'drop *',
            'keep *_dj*_*_*',
            'keep *_*FilterFlag__*'))
        return self.process.djTree
    
    def evalSequence(self, pattern, names) :
        return sum([getattr(self.process, pattern%name) for name in names], self.empty)


    def common(self) :
        for module in ((['PileupSummary','GenEvent'] if not self.options.isData else [])+
		       ['Triggers','EventFilters','Event','DisplacedJets']) :
	    print module
            self.process.load('MyAnalysis.DisplacedJetAnlzr.DJ_%s_cfi'%module)

        return (  self.evalSequence('dj%s',((['pileupsummary','genevent'] if not self.options.isData else []) +
					   ['triggers','eventfilters','event','displacedjets']  )
                                   )
               )

    def initialFilters(self):
        for module in ((['SignalFilterUDS'] if self.options.signal=='u' else []) +
                       (['SignalFilterB'] if self.options.signal=='b' else []) +
                       (['TriggerSelector'] if self.options.isData else [])):
            self.process.load('MyAnalysis.DisplacedJetAnlzr.DJ_%s_cfi'%module)
        return ( self.evalSequence('dj%s',((['signalfilteruds'] if self.options.signal=='u' else []) +
                                           (['signalfilterb'] if self.options.signal=='b' else []) +
                                           (['triggerselector'] if self.options.isData else []) )
                                    )
                   )


    def Pat(self) :

        from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching,removeCleaning,restrictInputToAOD,removeAllPATObjectsBut
        from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection 

        if self.options.isData: removeMCMatching(self.process, ['All'])
        restrictInputToAOD(self.process)
        removeCleaning(self.process)
        removeAllPATObjectsBut(self.process, ['Jets','METs'])
        switchJetCollection(self.process,
	    		    cms.InputTag('ak5PFJets'),
			    doJTA = True,
		  	    doBTagging = True,
			    doJetID = True,
			    jetCorrLabel = ('AK5PF',self.options.jetCorrections),
			    genJetCollection = cms.InputTag('ak5GenJets'),
			    doType1MET = False,
			    jetIdLabel = 'ak5pf'
                       )

        self.process.selectedPatJets.cut = cms.string("pt > 40 & abs(eta) < 2.0 && neutralHadronEnergyFraction < 0.9 && neutralEmEnergyFraction < 0.90 && chargedHadronEnergyFraction>0 && chargedHadronMultiplicity > 0 && chargedEmEnergyFraction < 0.99 && nConstituents > 2")

        del self.process.out
        del self.process.outpath
	return self.process.patDefaultSequence

    def HbheNoiseFilterResult(self) :
        self.process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')
        self.process.HBHENoiseFilterResultProducerNoIso = self.process.HBHENoiseFilterResultProducer.clone( minIsolatedNoiseSumE = 999999.0,
                                                                                              minNumIsolatedNoiseChannels = 999999,
                                                                                              minIsolatedNoiseSumEt = 999999.0  )
        self.process.hcalNoiseSummaryExists = cms.EDFilter('DJ_HcalNoiseSummaryExists')
        return (cms.Sequence(self.process.hcalNoiseSummaryExists + self.process.HBHENoiseFilterResultProducer + self.process.HBHENoiseFilterResultProducerNoIso))

    def MetFilterFlags(self) :
        # https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
        from RecoMET.METFilters.trackingFailureFilter_cfi import trackingFailureFilter
        from RecoMET.METFilters.hcalLaserEventFilter_cfi import hcalLaserEventFilter
        from RecoMET.METFilters.inconsistentMuonPFCandidateFilter_cfi import inconsistentMuonPFCandidateFilter
        from RecoMET.METFilters.greedyMuonPFCandidateFilter_cfi import greedyMuonPFCandidateFilter
        from RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi import EcalDeadCellTriggerPrimitiveFilter
        from RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi import EcalDeadCellBoundaryEnergyFilter

        self.process.trackingFailureFilterFlag = trackingFailureFilter.clone(taggingMode = True)#, quiet = True)
        self.process.hcalLaserEventFilterFlag = hcalLaserEventFilter.clone(taggingMode = True)
        self.process.greedyMuonPFCandidateFilterFlag = greedyMuonPFCandidateFilter.clone(taggingMode = True)
        self.process.inconsistentMuonPFCandidateFilterFlag = inconsistentMuonPFCandidateFilter.clone(taggingMode = True)
        self.process.ecalDeadCellTPFilterFlag = EcalDeadCellTriggerPrimitiveFilter.clone(taggingMode = True)
        self.process.ecalDeadCellBEFilterFlag = EcalDeadCellBoundaryEnergyFilter.clone(taggingMode = True,
                                                                              cutBoundEnergyDeadCellsEB = 10.0,
                                                                              cutBoundEnergyDeadCellsEE = 10.0,
                                                                              cutBoundEnergyGapEB = 100.0,
                                                                              cutBoundEnergyGapEE = 100.0,
                                                                              enableGap = False,
                                                                              limitDeadCellToChannelStatusEB = cms.vint32(12,14),
                                                                              limitDeadCellToChannelStatusEE = cms.vint32(12,14))

        return (cms.Sequence( self.process.trackingFailureFilterFlag *
                     self.process.hcalLaserEventFilterFlag *
                     self.process.greedyMuonPFCandidateFilterFlag *
                     self.process.inconsistentMuonPFCandidateFilterFlag *
                     self.process.ecalDeadCellTPFilterFlag
                     # * self.process.ecalDeadCellBEFilterFlag # product not found : EcalRecHitsEB
                     ))

