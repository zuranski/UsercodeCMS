import FWCore.ParameterSet.Config as cms

class DJ(object) :
    def __init__(self,process,options) :
        self.process = process
        self.options = options
        self.empty = process.empty = cms.Sequence()

    def path(self) :
        return cms.Path(  self.common() 
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
        for module in ((['SignalFilterUDS'] if self.options.signal=='u' else []) +
		       (['SignalFilterB'] if self.options.signal=='b' else []) +
		       [['PileupSummary','GenEvent'],['TriggerSelector']][self.options.isData]+
		       ['Triggers','EventFilters','Event','DisplacedJets']) :
	    print module
            self.process.load('MyAnalysis.DisplacedJetAnlzr.DJ_%s_cfi'%module)

        return (  self.evalSequence('dj%s',((['signalfilteruds'] if self.options.signal=='u' else []) +
					   (['signalfilterb'] if self.options.signal=='b' else []) +
					   ['pileupsummary','genevent'] if not self.options.isData else ['triggerselector']) +
					   ['triggers','eventfilters','event','displacedjets']  )
                 )

