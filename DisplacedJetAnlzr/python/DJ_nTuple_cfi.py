import FWCore.ParameterSet.Config as cms

class DJ(object) :
    def __init__(self,process,options) :
        self.process = process
        self.options = options
        self.empty = process.empty = cms.Sequence()

    def path(self) :
        return cms.Path( self.MCWeights()
                         *self.initialFilters()
                         *self.HbheNoiseFilterResult()
			 *self.MetFilterFlags()
                         *self.Pat()
                         *self.JetSelector()
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
		       ['Triggers','TriggerObjects','EventFilters','Event','Jets','DiJets']+
		       ['JetVertices','DiJetVertices','Muons']) :
	    print module
            self.process.load('MyAnalysis.DisplacedJetAnlzr.DJ_%s_cfi'%module)

        return (  self.evalSequence('dj%s',((['pileupsummary','genevent'] if not self.options.isData else []) +
					   ['triggers','triggerobjects','eventfilters','event','jets','dijets']+
                                           ['jetvertices','dijetvertices','muons'])
                                   )
               )

    def initialFilters(self):
        for module in ((['SignalFilter'] if self.options.signal else []) +
                       (['TriggerSelector'] if self.options.isData else [])):
	    print module
            self.process.load('MyAnalysis.DisplacedJetAnlzr.DJ_%s_cfi'%module)
        return ( self.evalSequence('dj%s',((['signalfilter'] if self.options.signal else []) +
                                           (['triggerselector'] if self.options.isData else []) )
                                    )
                   )


    def Pat(self) :

        from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching,removeCleaning,restrictInputToAOD,removeAllPATObjectsBut
        from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection 
        from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection 

        if self.options.isData: removeMCMatching(self.process, ['All'])
        restrictInputToAOD(self.process)
        removeCleaning(self.process)
        removeAllPATObjectsBut(self.process, ['Jets','METs','Muons'])
        addJetCollection(self.process,
	    		    cms.InputTag('ak5CaloJets'),
			    'AK5',
			    'Calo',
			    jetCorrLabel = ('AK5Calo',self.options.jetCorrections),
			    genJetCollection = cms.InputTag('ak5GenJets'),
			    doType1MET = False,
                       )
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

        self.process.selectedPatJets.cut = cms.string("pt > 30 && \
                                                       abs(eta) < 3.0 && \
                                                       neutralHadronEnergyFraction < 0.9 && \
                                                       neutralEmEnergyFraction < 0.90 && \
                                                       nConstituents > 1 && \
                                                       (? abs(eta)<2.4 ? chargedHadronEnergyFraction : 1) > 0 && \
                                                       (? abs(eta)<2.4 ? chargedHadronMultiplicity : 1) > 0 && \
                                                       (? abs(eta)<2.4 ? chargedEmEnergyFraction : 0) < 0.99")

        del self.process.out
        del self.process.outpath
	return self.process.patDefaultSequence

    def JetSelector(self):
        self.process.load("MyAnalysis/DisplacedJetAnlzr/JetSelector_cfi")
        return (cms.Sequence(self.process.trackerPatJets))

    def MCWeights(self):
        if self.options.signal:
            self.process.load("MyAnalysis/DisplacedJetAnlzr/PdfWeightProducer_cfi")
            return (cms.Sequence(self.process.pdfWeights))  
        else: return (self.empty)

    def HbheNoiseFilterResult(self) :
        self.process.load('CommonTools/RecoAlgos/HBHENoiseFilterResultProducer_cfi')
        return (cms.Sequence(self.process.HBHENoiseFilterResultProducer))

    def MetFilterFlags(self) :
        # https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
        from RecoMET.METFilters.trackingFailureFilter_cfi import trackingFailureFilter
        from RecoMET.METFilters.hcalLaserEventFilter_cfi import hcalLaserEventFilter
        from RecoMET.METFilters.inconsistentMuonPFCandidateFilter_cfi import inconsistentMuonPFCandidateFilter
        from RecoMET.METFilters.greedyMuonPFCandidateFilter_cfi import greedyMuonPFCandidateFilter
        from RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi import EcalDeadCellTriggerPrimitiveFilter
        from RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi import EcalDeadCellBoundaryEnergyFilter
        from RecoMET.METFilters.eeBadScFilter_cfi import eeBadScFilter
        from RecoMET.METFilters.ecalLaserCorrFilter_cfi import ecalLaserCorrFilter

        self.process.goodVertices = cms.EDFilter("VertexSelector",
                                                 filter = cms.bool(False),
                                                 src = cms.InputTag("offlinePrimaryVertices"),
                                                 cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
        )

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
        self.process.eeBadScFilterFlag = eeBadScFilter.clone(taggingMode = True)
        self.process.ecalLaserCorrFilterFlag = ecalLaserCorrFilter.clone(taggingMode = True)

        return (cms.Sequence( self.process.goodVertices *
                     self.process.trackingFailureFilterFlag *
                     self.process.hcalLaserEventFilterFlag *
                     self.process.greedyMuonPFCandidateFilterFlag *
                     self.process.inconsistentMuonPFCandidateFilterFlag *
                     self.process.ecalDeadCellTPFilterFlag *
                     self.process.ecalDeadCellBEFilterFlag *
                     self.process.eeBadScFilterFlag *
                     self.process.ecalLaserCorrFilterFlag
                     ))

