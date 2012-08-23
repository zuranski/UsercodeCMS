def __hack_ListVarparsingBug__(options,item) :
    val = getattr(options,item)
    if len(val) and type(val[0]) is list :
        tmp = val[0]
        options.clearList(item)
        setattr(options,item, tmp)

def options() :
    from FWCore.ParameterSet.VarParsing import VarParsing as VP
    options = VP('standard')
    options.output = "DJ_Tree.root"
    options.maxEvents = 100

    options.register('GlobalTag', mytype = VP.varType.string)
    options.register('quiet', default = True )
    options.register('isData', default = True )
    options.register('signal', default = '', info = "signal type u (UDS) or b (B)", mytype = VP.varType.string)
    options.register('jetCorrections', default = ['L1FastJet','L2Relative','L3Absolute','L2L3Residual'], #L2L3Residual removed from options for simulation (below)
                     info = "jet correction levels to apply", mult = VP.multiplicity.list, mytype = VP.varType.string)
    
    __hack_ListVarparsingBug__( options, 'jetCorrections')
    options.parseArguments()
    options._tagOrder =[] # weird, but something to do with options.output

    defaultGT,defaultFile = {
        "44X" : [('START44_V9B::All','/store/mc/Fall11/QCD_Pt-170to300_TuneZ2_7TeV_pythia6/AODSIM/PU_S6_START42_V14B-v1/0000/FCD9F545-A506-E111-AA8F-003048D477BA.root'),
                 ('START44_V9B::All','/store/mc/Fall11/HTo2LongLivedTo4F_MH-400_MFF-150_CTau-400_7TeV-pythia6/GEN-SIM-RECODEBUG/DEBUG-PU_S6_START44_V9B-v4/0000/F604103E-168B-E111-B732-00266CFFC7E4.root'),
                 ('FT_R_44_V11::All','/store/data/Run2011B/HT/RECO/19Nov2011-v1/10001/B2E314BC-4746-E111-9BC1-00261894390A.root')],
        }["44X"][len(options.signal)+ 2*options.isData]
    options.files = options.files if options.files else defaultFile
    options.GlobalTag = options.GlobalTag if options.GlobalTag else defaultGT

    if not options.isData : #remove L2L3Residual correction from simulation options
        jecs = [jc for jc in options.jetCorrections if jc!='L2L3Residual']
        options.clearList('jetCorrections')
        options.jetCorrections = jecs

    return options
