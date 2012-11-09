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
        "44X" : [('START44_V9B::All','/store/mc/Fall11/QCD_Pt-120to170_TuneZ2_7TeV_pythia6/AODSIM/PU_S6_START42_V14B-v1/0000/0A8E5F68-73F4-E011-AB1C-00E08178C0D5.root'),
                 ('START44_V9B::All','/store/mc/Fall11/HTo2LongLivedTo4F_MH-1000_MFF-350_CTau-350_7TeV-pythia6/GEN-SIM-RECODEBUG/DEBUG-PU_S6_START44_V9B-v4/0000/E83B1DB8-158B-E111-9DB4-0017A477003C.root'),
                 ('FT_R_44_V11::All','/store/data/Run2011B/HT/RECO/19Nov2011-v1/10001/B2E314BC-4746-E111-9BC1-00261894390A.root')],
        "53X" : [('START53_V7F::All','/store/mc/Summer12_DR53X/QCD_Pt-170to300_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v2/00000/0CECB336-B70E-E211-B22D-0018F3D096CE.root'),
                 ('START53_V7F::All','/store/mc/Summer12_DR53X/HTo2LongLivedTo4F_MH-1000_MFF-350_CTau35To3500_8TeV-pythia6/AODSIM/DEBUG_PU_S10_START53_V7A-v1/0000/9C61CA50-0BF3-E111-91E1-003048D2BB22.root'),
                 ('FT_53_V10_AN2','/store/data/Run2012C/JetHT/AOD/PromptReco-v2/000/199/021/EC91A7AA-1BD1-E111-A51D-BCAEC5329717.root')]
        }["53X"][len(options.signal)+ 2*options.isData]
    options.files = options.files if options.files else defaultFile
    options.GlobalTag = options.GlobalTag if options.GlobalTag else defaultGT

    if not options.isData : #remove L2L3Residual correction from simulation options
        jecs = [jc for jc in options.jetCorrections if jc!='L2L3Residual']
        options.clearList('jetCorrections')
        options.jetCorrections = jecs

    return options
