import FWCore.ParameterSet.Config as cms

process = cms.Process("DJ")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/Fall11/HTo2LongLivedTo4F_MH-400_MFF-150_CTau-400_7TeV-pythia6/GEN-SIM-RECODEBUG/DEBUG-PU_S6_START44_V9B-v4/0000/F604103E-168B-E111-B732-00266CFFC7E4.root')
)
process.HBHENoiseFilterResultProducer = cms.EDProducer("HBHENoiseFilterResultProducer",
    minRBXHits = cms.int32(999),
    minIsolatedNoiseSumE = cms.double(50.0),
    minHighEHitTime = cms.double(-9999.0),
    minHPDNoOtherHits = cms.int32(10),
    useTS4TS5 = cms.bool(True),
    noiselabel = cms.InputTag("hcalnoise"),
    minZeros = cms.int32(10),
    minNumIsolatedNoiseChannels = cms.int32(10),
    maxRatio = cms.double(999),
    maxHighEHitTime = cms.double(9999.0),
    maxRBXEMF = cms.double(-999.0),
    minHPDHits = cms.int32(17),
    minIsolatedNoiseSumEt = cms.double(25.0),
    minRatio = cms.double(-999)
)


process.HBHENoiseFilterResultProducerNoIso = cms.EDProducer("HBHENoiseFilterResultProducer",
    maxRBXEMF = cms.double(-999.0),
    minHPDHits = cms.int32(17),
    minIsolatedNoiseSumE = cms.double(999999.0),
    minHighEHitTime = cms.double(-9999.0),
    minHPDNoOtherHits = cms.int32(10),
    useTS4TS5 = cms.bool(True),
    noiselabel = cms.InputTag("hcalnoise"),
    minZeros = cms.int32(10),
    minNumIsolatedNoiseChannels = cms.int32(999999),
    maxHighEHitTime = cms.double(9999.0),
    maxRatio = cms.double(999),
    minRBXHits = cms.int32(999),
    minIsolatedNoiseSumEt = cms.double(999999.0),
    minRatio = cms.double(-999)
)


process.TrackProducer = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ak5JetExtender = cms.EDProducer("JetExtender",
    jets = cms.InputTag("ak5CaloJets"),
    jet2TracksAtCALO = cms.InputTag("ak5JetTracksAssociatorAtCaloFace"),
    jet2TracksAtVX = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    coneSize = cms.double(0.5)
)


process.ak5JetID = cms.EDProducer("JetIDProducer",
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    hoRecHitsColl = cms.InputTag("horeco"),
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    useRecHits = cms.bool(True),
    src = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtCaloFace = cms.EDProducer("JetTracksAssociatorAtCaloFace",
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator"),
    jets = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5CaloJets")
)


process.beamhaloTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("beamhaloTrackerSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('BeamHaloPropagatorAlong'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('BeamHaloPropagatorOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('BeamHaloNavigationSchool'),
    TrajectoryBuilder = cms.string('CkfTrajectoryBuilderBH')
)


process.beamhaloTrackerSeeds = cms.EDProducer("CtfSpecialSeedGenerator",
    ErrorRescaling = cms.double(50.0),
    OrderedHitsFactoryPSets = cms.VPSet(cms.PSet(
        ComponentName = cms.string('BeamHaloPairGenerator'),
        maxTheta = cms.double(0.1),
        NavigationDirection = cms.string('outsideIn'),
        LayerPSet = cms.PSet(
            TEC4 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC5 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC6 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC = cms.PSet(
                minRing = cms.int32(5),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(7)
            ),
            TEC1 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC2 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            TEC3 = cms.PSet(
                minRing = cms.int32(1),
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(True),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                maxRing = cms.int32(2)
            ),
            FPix = cms.PSet(
                hitErrorRZ = cms.double(0.0036),
                hitErrorRPhi = cms.double(0.0051),
                TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
                HitProducer = cms.string('siPixelRecHits'),
                useErrorsFromParam = cms.bool(True)
            ),
            TID = cms.PSet(
                matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
            ),
            layerList = cms.vstring('FPix1_pos+FPix2_pos', 
                'FPix1_neg+FPix2_neg', 
                'TID2_pos+TID3_pos', 
                'TID2_neg+TID3_neg', 
                'TEC1_neg+TEC2_neg', 
                'TEC1_pos+TEC2_pos', 
                'TEC2_neg+TEC3_neg', 
                'TEC2_pos+TEC3_pos', 
                'TEC3_neg+TEC4_neg', 
                'TEC3_pos+TEC4_pos', 
                'TEC4_neg+TEC5_neg', 
                'TEC4_pos+TEC5_pos', 
                'TEC5_neg+TEC6_neg', 
                'TEC5_pos+TEC6_pos', 
                'TEC7_neg+TEC8_neg', 
                'TEC7_pos+TEC8_pos', 
                'TEC8_neg+TEC9_neg', 
                'TEC8_pos+TEC9_pos')
        ),
        PropagationDirection = cms.string('alongMomentum')
    ), 
        cms.PSet(
            ComponentName = cms.string('BeamHaloPairGenerator'),
            maxTheta = cms.double(0.1),
            NavigationDirection = cms.string('outsideIn'),
            LayerPSet = cms.PSet(
                TEC4 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC5 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC6 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC = cms.PSet(
                    minRing = cms.int32(5),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(7)
                ),
                TEC1 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC2 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                TEC3 = cms.PSet(
                    minRing = cms.int32(1),
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(True),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
                    maxRing = cms.int32(2)
                ),
                FPix = cms.PSet(
                    hitErrorRZ = cms.double(0.0036),
                    hitErrorRPhi = cms.double(0.0051),
                    TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
                    HitProducer = cms.string('siPixelRecHits'),
                    useErrorsFromParam = cms.bool(True)
                ),
                TID = cms.PSet(
                    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
                    useRingSlector = cms.bool(False),
                    TTRHBuilder = cms.string('WithTrackAngle'),
                    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
                ),
                layerList = cms.vstring('FPix1_pos+FPix2_pos', 
                    'FPix1_neg+FPix2_neg', 
                    'TID2_pos+TID3_pos', 
                    'TID2_neg+TID3_neg', 
                    'TEC1_neg+TEC2_neg', 
                    'TEC1_pos+TEC2_pos', 
                    'TEC2_neg+TEC3_neg', 
                    'TEC2_pos+TEC3_pos', 
                    'TEC3_neg+TEC4_neg', 
                    'TEC3_pos+TEC4_pos', 
                    'TEC4_neg+TEC5_neg', 
                    'TEC4_pos+TEC5_pos', 
                    'TEC5_neg+TEC6_neg', 
                    'TEC5_pos+TEC6_pos', 
                    'TEC7_neg+TEC8_neg', 
                    'TEC7_pos+TEC8_pos', 
                    'TEC8_neg+TEC9_neg', 
                    'TEC8_pos+TEC9_pos')
            ),
            PropagationDirection = cms.string('oppositeToMomentum')
        )),
    Charges = cms.vint32(-1, 1),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(10000),
    UseScintillatorsConstraint = cms.bool(False),
    SetMomentum = cms.bool(True),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originHalfLength = cms.double(21.2),
            originZPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            ptMin = cms.double(0.9),
            originXPos = cms.double(0.0),
            originRadius = cms.double(0.2)
        ),
        ComponentName = cms.string('GlobalRegionProducer')
    ),
    SeedsFromNegativeY = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    SeedsFromPositiveY = cms.bool(False),
    MaxNumberOfPixelClusters = cms.uint32(10000),
    SeedMomentum = cms.double(15.0),
    maxSeeds = cms.int32(10000),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    requireBOFF = cms.bool(False)
)


process.beamhaloTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("beamhaloTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherBH'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('beamhaloTracks'),
    NavigationSchool = cms.string('BeamHaloNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('beamhalo'),
    Propagator = cms.string('BeamHaloPropagatorAlong')
)


process.ckfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalMixedSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder')
)


process.ckfTrackCandidatesCombinedSeeds = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalCombinedSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder')
)


process.ckfTrackCandidatesNoOverlaps = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalMixedSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('CkfTrajectoryBuilder')
)


process.ckfTrackCandidatesPixelLess = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("globalPixelLessSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder')
)


process.cleanPatElectrons = cms.EDProducer("PATElectronCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatElectrons"),
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            src = cms.InputTag("cleanPatMuons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        )
    ),
    preselection = cms.string('')
)


process.cleanPatJets = cms.EDProducer("PATJetCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatJets"),
    checkOverlaps = cms.PSet(
        taus = cms.PSet(
            src = cms.InputTag("cleanPatTaus"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        photons = cms.PSet(
            src = cms.InputTag("cleanPatPhotons"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        electrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        muons = cms.PSet(
            src = cms.InputTag("cleanPatMuons"),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        tkIsoElectrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False)
        )
    ),
    preselection = cms.string('')
)


process.cleanPatMuons = cms.EDProducer("PATMuonCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatMuons"),
    checkOverlaps = cms.PSet(

    ),
    preselection = cms.string('')
)


process.cleanPatPhotons = cms.EDProducer("PATPhotonCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatPhotons"),
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            requireNoOverlaps = cms.bool(False),
            algorithm = cms.string('bySuperClusterSeed')
        )
    ),
    preselection = cms.string('')
)


process.cleanPatTaus = cms.EDProducer("PATTauCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatTaus"),
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            src = cms.InputTag("cleanPatMuons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        ),
        electrons = cms.PSet(
            src = cms.InputTag("cleanPatElectrons"),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            checkRecoComponents = cms.bool(False),
            algorithm = cms.string('byDeltaR'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False)
        )
    ),
    preselection = cms.string('tauID("leadingTrackFinding") > 0.5 & tauID("leadingPionPtCut") > 0.5 & tauID("byIsolationUsingLeadingPion") > 0.5 & tauID("againstMuon") > 0.5 & tauID("againstElectron") > 0.5 & (signalPFChargedHadrCands.size() = 1 | signalPFChargedHadrCands.size() = 3)')
)


process.combinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"), cms.InputTag("softMuonTagInfos"), cms.InputTag("softElectronTagInfos"))
)


process.combinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.combinedSecondaryVertexBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"), cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.combinedSecondaryVertexMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.combinedSecondaryVertexMVABJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexMVA'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"), cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.convClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("tobTecStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("tobTecStepSelector","tobTecStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(30.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.convStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("convStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(1),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(3),
        chi2n_par = cms.double(3.0),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(5.0, 8.0),
        applyAdaptedPVCuts = cms.bool(False),
        dz_par1 = cms.vdouble(5.0, 8.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('convStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(5.0, 8.0),
        d0_par1 = cms.vdouble(5.0, 8.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(1),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(2.5),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('convStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('convStepLoose'),
            d0_par2 = cms.vdouble(5.0, 8.0),
            d0_par1 = cms.vdouble(5.0, 8.0),
            res_par = cms.vdouble(0.003, 0.001)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(1),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(2.0),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(5.0, 8.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('convStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(5.0, 8.0),
            d0_par1 = cms.vdouble(5.0, 8.0),
            preFilterName = cms.string('convStepTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.convStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("convTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('convStepFitterSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter8'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.convTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("photonConvTrajSeedFromSingleLeg","convSeedCandidates"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('convCkfTrajectoryBuilder')
)


process.conversionStepTracks = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(False),
    MinPT = cms.double(0.05),
    makeReKeyedSeeds = cms.untracked.bool(False),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("convStepSelector","convStep")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(1)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("convStepTracks")),
    newQuality = cms.string('confirmed')
)


process.corMetGlobalMuons = cms.EDProducer("MuonMET",
    muonMETDepositValueMapInputTag = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    metTypeInputTag = cms.InputTag("CaloMET"),
    muonsInputTag = cms.InputTag("muons"),
    uncorMETInputTag = cms.InputTag("met")
)


process.ctfCombinedSeeds = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesCombinedSeeds"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfNoOverlaps = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesNoOverlaps"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfPixelLess = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidatesPixelLess"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.ctfWithMaterialTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("ckfTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('undefAlgorithm'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.dedxDiscrimASmi = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(3),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxDiscrimBTag = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(1),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxDiscrimProd = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(0),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxDiscrimSmi = cms.EDProducer("DeDxDiscriminatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    ProbabilityMode = cms.untracked.string('Accumulation'),
    tracks = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    Formula = cms.untracked.uint32(2),
    Reccord = cms.untracked.string('SiStripDeDxMip_3D_Rcd'),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxHarmonic2 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('generic'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    trajectoryTrackAssociation = cms.InputTag("generalTracks"),
    UsePixel = cms.bool(False),
    exponent = cms.double(-2.0)
)


process.dedxMedian = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('median'),
    ShapeTest = cms.bool(False),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxTruncated40 = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('truncated'),
    ShapeTest = cms.bool(True),
    fraction = cms.double(0.4),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.dedxUnbinned = cms.EDProducer("DeDxEstimatorProducer",
    UseStrip = cms.bool(True),
    MeVperADCPixel = cms.double(3.61e-06),
    UseCalibration = cms.bool(False),
    calibrationPath = cms.string(''),
    tracks = cms.InputTag("generalTracks"),
    estimator = cms.string('unbinnedFit'),
    ShapeTest = cms.bool(True),
    MeVperADCStrip = cms.double(0.00095665),
    UsePixel = cms.bool(False),
    trajectoryTrackAssociation = cms.InputTag("generalTracks")
)


process.detachedTripletStep = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(False),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("detachedTripletStepSelector","detachedTripletStepVtx"), cms.InputTag("detachedTripletStepSelector","detachedTripletStepTrk")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1, 1),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(0, 1)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("detachedTripletStepTracks"), cms.InputTag("detachedTripletStepTracks")),
    newQuality = cms.string('confirmed')
)


process.detachedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("pixelPairStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("pixelPairStepSelector","pixelPairStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.detachedTripletStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('detachedTripletStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(1.0),
            nSigmaZ = cms.double(4.0),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            ptMin = cms.double(0.2)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.detachedTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("detachedTripletStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(3),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.3, 3.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.2, 3.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('detachedTripletStepVtxLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(1.3, 3.0),
        d0_par1 = cms.vdouble(1.2, 3.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(0),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('loose'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.6, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.6, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepTrkLoose'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.6, 4.0),
            d0_par1 = cms.vdouble(1.6, 4.0),
            preFilterName = cms.string('')
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.9, 3.0),
            dz_par2 = cms.vdouble(1.0, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepVtxTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('detachedTripletStepVtxLoose'),
            d0_par2 = cms.vdouble(1.0, 3.0),
            d0_par1 = cms.vdouble(0.95, 3.0),
            res_par = cms.vdouble(0.003, 0.001)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.5),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepTrkTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('detachedTripletStepTrkLoose'),
            d0_par2 = cms.vdouble(1.1, 4.0),
            d0_par1 = cms.vdouble(1.1, 4.0),
            res_par = cms.vdouble(0.003, 0.001)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.9, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.8, 3.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepVtx'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.9, 3.0),
            d0_par1 = cms.vdouble(0.85, 3.0),
            preFilterName = cms.string('detachedTripletStepVtxTight')
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.4),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.0, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.0, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('detachedTripletStepTrk'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.0, 4.0),
            d0_par1 = cms.vdouble(1.0, 4.0),
            preFilterName = cms.string('detachedTripletStepTrkTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.detachedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("detachedTripletStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('detachedTripletStepTrajectoryBuilder')
)


process.detachedTripletStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("detachedTripletStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter3'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.djdisplacedjets = cms.EDProducer("DJ_DisplacedJets",
    TrackPtCut = cms.double(1.0),
    patJetCollectionTag = cms.InputTag("selectedPatJets"),
    vertexfitter = cms.PSet(
        fitter = cms.string('avf')
    ),
    useTrackingParticles = cms.bool(True),
    PromptTrackDxyCut = cms.double(0.05)
)


process.djevent = cms.EDProducer("DJ_Event")


process.djeventfilters = cms.EDProducer("DJ_EventFilters",
    HcalLaserEventFilterInputTag = cms.InputTag("hcalLaserEventFilter"),
    VertexMaxd0 = cms.double(2.0),
    NumTracks = cms.uint32(10),
    TrackingFailureJets = cms.InputTag("ak5PFJets"),
    EcalDeadCellTriggerPrimitiveFilterInputTag = cms.InputTag("EcalDeadCellTriggerPrimitiveFilter"),
    EcalMaskedCellDRFilterInputTag = cms.InputTag("simpleDRfilter","deadCellStatus"),
    VertexMaxAbsZ = cms.double(24.0),
    HPTrackThreshold = cms.double(0.25),
    VertexMinimumNDOF = cms.uint32(4),
    BeamHaloInputTag = cms.InputTag("BeamHaloSummary"),
    VertexInputTag = cms.InputTag("offlinePrimaryVertices"),
    L1InputTag = cms.InputTag("gtDigis"),
    EcalDeadCellBoundaryEnergyFilterInputTag = cms.InputTag("EcalDeadCellBoundaryEnergyFilter"),
    TrackingFailureDxyTrVtxMax = cms.double(0.2),
    CaloBoundaryDRFilterInputTag = cms.InputTag("simpleDRfilter","boundaryStatus"),
    HcalNoiseInputTag = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResult"),
    BadEESupercrystalFilterInputTag = cms.InputTag("eeBadScFilter"),
    TrackingFailureDzTrVtzMax = cms.double(1.0),
    TrackingFailureMinSumPtOverHT = cms.double(0.1),
    EcalLaserCorrFilterInputTag = cms.InputTag("ecalLaserCorrFilter"),
    TrackingFailureFilterInputTag = cms.InputTag("trackingFailureFilter"),
    TracksInputTag = cms.InputTag("generalTracks")
)


process.djgenevent = cms.EDProducer("DJ_GenEvent")


process.djpileupsummary = cms.EDProducer("DJ_PileupSummary",
    Prefix = cms.string('pileup'),
    InputTag = cms.InputTag("addPileupInfo"),
    Suffix = cms.string('')
)


process.djtriggers = cms.EDProducer("DJ_Triggers",
    TriggerEventInputTag = cms.InputTag("hltTriggerSummaryAOD"),
    HLTPaths = cms.vstring('HLT_HT250_DoubleDisplacedJet60_v*', 
        'HLT_HT250_DoubleDisplacedJet60_PromptTrack_v*', 
        'HLT_HT250_v*'),
    InputTag = cms.InputTag("TriggerResults")
)


process.eidCutBasedExt = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('loose'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidLoose = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('loose'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('classbased'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidRobustHighEnergy = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('highenergy'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidRobustLoose = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('loose'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidRobustTight = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('tight'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('robust'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eidTight = cms.EDProducer("EleIdCutBasedExtProducer",
    electronQuality = cms.string('tight'),
    classbasedtightEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(10.9, 7.01, 8.75, 3.51, 7.75, 
            1.62, 11.6, 9.9, 4.97, 5.33, 
            3.18, 2.32, 0.164, 5.46, 12.0, 
            0.00604, 4.1, 0.000628),
        cutmishits = cms.vdouble(5.5, 1.5, 0.5, 1.5, 2.5, 
            0.5, 3.5, 5.5, 0.5, 0.5, 
            0.5, 0.5, 0.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0871, 0.0289, 0.0783, 0.0946, 0.0245, 
            0.0363, 0.0671, 0.048, 0.0614, 0.0924, 
            0.0158, 0.049, 0.0382, 0.0915, 0.0451, 
            0.0452, 0.00196, 0.0043),
        cutdeta = cms.vdouble(0.00915, 0.00302, 0.0061, 0.0135, 0.00565, 
            0.00793, 0.0102, 0.00266, 0.0106, 0.00903, 
            0.00766, 0.00723, 0.0116, 0.00203, 0.00659, 
            0.0148, 0.00555, 0.0128),
        cuteopin = cms.vdouble(0.878, 0.859, 0.874, 0.944, 0.737, 
            0.773, 0.86, 0.967, 0.917, 0.812, 
            0.915, 1.01, 0.847, 0.953, 0.979, 
            0.841, 0.771, 1.09),
        cutip = cms.vdouble(0.0239, 0.027, 0.0768, 0.0231, 0.178, 
            0.0957, 0.0102, 0.0168, 0.043, 0.0166, 
            0.0594, 0.0308, 2.1, 0.00527, 3.17, 
            4.91, 0.769, 5.9),
        cutisotk = cms.vdouble(6.53, 4.6, 6.0, 8.63, 3.11, 
            7.77, 5.42, 4.81, 4.06, 6.47, 
            2.8, 3.45, 5.29, 5.18, 15.4, 
            5.38, 4.47, 0.0347),
        cutsee = cms.vdouble(0.0131, 0.0106, 0.0115, 0.0306, 0.028, 
            0.0293, 0.0131, 0.0106, 0.0115, 0.0317, 
            0.029, 0.0289, 0.0142, 0.0106, 0.0103, 
            0.035, 0.0296, 0.0333),
        cutdphi = cms.vdouble(0.0369, 0.0307, 0.117, 0.0475, 0.0216, 
            0.117, 0.0372, 0.0246, 0.0426, 0.0612, 
            0.0142, 0.039, 0.0737, 0.0566, 0.0359, 
            0.0187, 0.012, 0.0358),
        cutisoecal = cms.vdouble(20.0, 27.2, 4.48, 13.5, 4.56, 
            3.19, 12.2, 13.1, 7.42, 7.67, 
            4.12, 4.85, 10.1, 12.4, 11.1, 
            11.0, 10.6, 13.4)
    ),
    classbasedtightEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    classbasedtightEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.032, 0.016, 0.0525, 0.09, 0.025, 
            0.035, 0.065, 0.092),
        hOverE = cms.vdouble(0.05, 0.042, 0.045, 0.0, 0.055, 
            0.037, 0.05, 0.0),
        sigmaEtaEta = cms.vdouble(0.0125, 0.011, 0.01, 0.0, 0.0265, 
            0.0252, 0.026, 0.0),
        deltaEtaIn = cms.vdouble(0.0055, 0.003, 0.0065, 0.0, 0.006, 
            0.0055, 0.0075, 0.0),
        eSeedOverPin = cms.vdouble(0.24, 0.94, 0.11, 0.0, 0.32, 
            0.83, 0.0, 0.0)
    ),
    classbasedtightEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.0225, 0.0114, 0.0234, 0.039, 0.0215, 
            0.0095, 0.0148, 0.0167),
        hOverE = cms.vdouble(0.056, 0.0221, 0.037, 0.0, 0.0268, 
            0.0102, 0.0104, 0.0),
        sigmaEtaEta = cms.vdouble(0.0095, 0.0094, 0.0094, 0.0, 0.026, 
            0.0257, 0.0246, 0.0),
        deltaEtaIn = cms.vdouble(0.0043, 0.00282, 0.0036, 0.0, 0.0066, 
            0.0049, 0.0041, 0.0),
        eSeedOverPin = cms.vdouble(0.32, 0.94, 0.221, 0.0, 0.74, 
            0.89, 0.66, 0.0)
    ),
    classbasedtightEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    classbasedtightEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00811, 0.00341, 0.00633, 0.0103, 0.00667, 
            0.01, 0.0106, 0.0145, 0.0163, 0.0076, 
            0.00259, 0.00511, 0.00941, 0.0043, 0.00857, 
            0.012, 0.0169, 0.00172, 0.00861, 0.00362, 
            0.00601, 0.00925, 0.00489, 0.00832, 0.0119, 
            0.0169, 0.000996),
        cutiso_sum = cms.vdouble(11.8, 8.31, 6.26, 6.18, 3.28, 
            4.38, 4.17, 5.4, 1.57, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0213, 0.0422, 0.0632, 0.0361, 0.073, 
            0.126, 0.171, 0.119, 0.0372, 0.0131, 
            0.0146, 0.0564, 0.0152, 0.0222, 0.0268, 
            0.0314, 0.0884, 0.00374, 0.00852, 0.00761, 
            0.0143, 0.0106, 0.0127, 0.0119, 0.0123, 
            0.0235, 0.00363),
        cuthoe = cms.vdouble(0.0783, 0.0387, 0.105, 0.118, 0.0227, 
            0.062, 0.13, 2.47, 0.38, 0.0888, 
            0.0503, 0.0955, 0.0741, 0.015, 0.03, 
            0.589, 1.13, 0.612, 0.0494, 0.0461, 
            0.0292, 0.0369, 0.0113, 0.0145, 0.124, 
            2.05, 0.61),
        cutfmishits = cms.vdouble(2.5, 1.5, 1.5, 1.5, 1.5, 
            0.5, 2.5, 0.5, 0.5, 2.5, 
            1.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5, -0.5, 2.5, 1.5, 
            0.5, 0.5, 0.5, 0.5, 0.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(13.7, 11.6, 7.14, 9.98, 3.52, 
            4.87, 6.24, 7.96, 2.53, 11.2, 
            11.9, 7.88, 8.16, 5.58, 5.03, 
            11.4, 8.15, 5.79, 10.4, 11.1, 
            10.4, 7.47, 5.08, 5.9, 11.8, 
            14.1, 11.7),
        cutdcotdist = cms.vdouble(0.0393, 0.0256, 0.00691, 0.0394, 0.0386, 
            0.039, 0.0325, 0.0384, 0.0382, 0.0245, 
            0.000281, 5.46e-05, 0.0342, 0.0232, 0.00107, 
            0.0178, 0.0193, 0.000758, 0.000108, 0.0248, 
            0.000458, 0.0129, 0.00119, 0.0182, 4.53e-05, 
            0.0189, 0.000928),
        cutsee = cms.vdouble(0.0143, 0.0105, 0.0123, 0.0324, 0.0307, 
            0.0301, 0.0109, 0.027, 0.0292, 0.0133, 
            0.0104, 0.0116, 0.0332, 0.0296, 0.031, 
            0.00981, 0.0307, 0.072, 0.0149, 0.0105, 
            0.011, 0.0342, 0.0307, 0.0303, 0.00954, 
            0.0265, 0.0101),
        cuteseedopcor = cms.vdouble(0.784, 0.366, 0.57, 0.911, 0.298, 
            0.645, 0.51, 0.497, 0.932, 0.835, 
            0.968, 0.969, 0.923, 0.898, 0.98, 
            0.63, 0.971, 1.0, 0.515, 0.963, 
            0.986, 0.823, 0.879, 1.01, 0.931, 
            0.937, 1.05),
        cutdphiin = cms.vdouble(0.0404, 0.0499, 0.263, 0.042, 0.0484, 
            0.241, 0.242, 0.231, 0.286, 0.0552, 
            0.0338, 0.154, 0.0623, 0.0183, 0.0392, 
            0.0547, 0.0588, 0.00654, 0.042, 0.0217, 
            0.0885, 0.0445, 0.0141, 0.0234, 0.065, 
            0.0258, 0.0346),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 13.7, 13.2, 
            13.6, 14.2, 14.1, 13.9, 12.9, 
            14.9, 17.7)
    ),
    electronIDType = cms.string('classbased'),
    robusttightEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    electronVersion = cms.string(''),
    robusttightEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.015, 0.0092, 0.02, 0.0025, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.018, 0.025, 0.02, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusttightEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.01, 0.0099, 0.025, 0.004, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.01, 0.028, 0.02, 0.0066, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    robusttightEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    verticesCollection = cms.InputTag("offlinePrimaryVerticesWithBS"),
    classbasedlooseEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    robusttightEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.011, 0.09, 0.005, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.1, 0.0275, 0.09, 0.007, -1, 
            -1, 9999.0, 9999.0, 0, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robusthighenergyEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedlooseEleIDCutsV00 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.05, 0.025, 0.053, 0.09, 0.07, 
            0.03, 0.092, 0.092),
        hOverE = cms.vdouble(0.115, 0.1, 0.055, 0.0, 0.145, 
            0.12, 0.15, 0.0),
        sigmaEtaEta = cms.vdouble(0.014, 0.012, 0.0115, 0.0, 0.0275, 
            0.0265, 0.0265, 0.0),
        deltaEtaIn = cms.vdouble(0.009, 0.0045, 0.0085, 0.0, 0.0105, 
            0.0068, 0.01, 0.0),
        eSeedOverPin = cms.vdouble(0.11, 0.91, 0.11, 0.0, 0.0, 
            0.85, 0.0, 0.0)
    ),
    classbasedlooseEleIDCutsV01 = cms.PSet(
        deltaPhiIn = cms.vdouble(0.053, 0.0189, 0.059, 0.099, 0.0278, 
            0.0157, 0.042, 0.08),
        hOverE = cms.vdouble(0.076, 0.033, 0.07, 0.0, 0.083, 
            0.0148, 0.033, 0.0),
        sigmaEtaEta = cms.vdouble(0.0101, 0.0095, 0.0097, 0.0, 0.0271, 
            0.0267, 0.0259, 0.0),
        deltaEtaIn = cms.vdouble(0.0078, 0.00259, 0.0062, 0.0, 0.0078, 
            0.0061, 0.0061, 0.0),
        eSeedOverPin = cms.vdouble(0.3, 0.92, 0.211, 0.0, 0.42, 
            0.88, 0.68, 0.0)
    ),
    classbasedlooseEleIDCutsV02 = cms.PSet(
        cutisohcal = cms.vdouble(13.5, 9.93, 7.56, 14.8, 8.1, 
            10.8, 42.7, 20.1, 9.11, 10.4, 
            6.89, 5.59, 8.53, 9.59, 24.2, 
            2.78, 8.67, 0.288),
        cutmishits = cms.vdouble(5.5, 1.5, 5.5, 2.5, 2.5, 
            2.5, 3.5, 5.5, 0.5, 1.5, 
            2.5, 0.5, 1.5, 1.5, 0.5, 
            0.5, 0.5, 0.5),
        cuthoe = cms.vdouble(0.0887, 0.0934, 0.0949, 0.0986, 0.0431, 
            0.0878, 0.097, 0.0509, 0.098, 0.0991, 
            0.0321, 0.0928, 0.0663, 0.0717, 0.0966, 
            0.0758, 0.0149, 0.0131),
        cutdeta = cms.vdouble(0.00958, 0.00406, 0.0122, 0.0137, 0.00837, 
            0.0127, 0.011, 0.00336, 0.00977, 0.015, 
            0.00675, 0.0109, 0.014, 0.00508, 0.0109, 
            0.0146, 0.00506, 0.0127),
        cuteopin = cms.vdouble(0.878, 0.802, 0.814, 0.942, 0.735, 
            0.774, 0.829, 0.909, 0.829, 0.813, 
            0.86, 0.897, 0.817, 0.831, 0.818, 
            0.861, 0.787, 0.789),
        cutip = cms.vdouble(0.0246, 0.076, 0.0966, 0.0885, 0.441, 
            0.205, 0.0292, 0.0293, 0.0619, 0.0251, 
            0.159, 0.0815, 7.29, 0.0106, 5.76, 
            6.89, 1.27, 5.89),
        cutisotk = cms.vdouble(24.3, 8.45, 14.4, 27.8, 6.02, 
            10.5, 14.1, 10.2, 14.5, 19.1, 
            6.1, 14.1, 8.59, 8.33, 8.3, 
            8.93, 8.6, 16.0),
        cutsee = cms.vdouble(0.0172, 0.0115, 0.0143, 0.0344, 0.0295, 
            0.0304, 0.0145, 0.0108, 0.0128, 0.0347, 
            0.0307, 0.0316, 0.018, 0.011, 0.0132, 
            0.0349, 0.031, 0.0327),
        cutdphi = cms.vdouble(0.0372, 0.114, 0.118, 0.0488, 0.117, 
            0.119, 0.0606, 0.0548, 0.117, 0.07, 
            0.0355, 0.117, 0.088, 0.045, 0.118, 
            0.0919, 0.0236, 0.0515),
        cutisoecal = cms.vdouble(33.4, 28.1, 7.32, 27.4, 7.33, 
            21.7, 93.8, 102.0, 12.1, 26.0, 
            8.91, 10.0, 16.1, 31.3, 16.9, 
            15.4, 13.3, 37.7)
    ),
    classbasedlooseEleIDCutsV03 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV04 = cms.PSet(
        cutdetain = cms.vdouble(0.00989, 0.00484, 0.0146, 0.0146, 0.00902, 
            0.0172, 0.0137, 0.0477, 0.0275, 0.00967, 
            0.00377, 0.00924, 0.013, 0.00666, 0.0123, 
            0.0125, 0.0228, 0.0112, 0.0106, 0.0038, 
            0.00897, 0.0139, 0.00667, 0.0122, 0.0122, 
            0.0193, 0.00239),
        cutiso_sum = cms.vdouble(31.5, 10.3, 8.8, 11.0, 6.13, 
            6.94, 7.52, 9.0, 3.5, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 
            100000.0, 100000.0),
        cutip_gsf = cms.vdouble(0.0431, 0.0767, 0.139, 0.101, 0.149, 
            0.154, 0.932, 0.15, 0.124, 0.0238, 
            0.0467, 0.0759, 0.0369, 0.147, 0.0986, 
            0.0626, 0.195, 0.116, 0.0122, 0.0125, 
            0.0693, 0.0162, 0.089, 0.0673, 0.0467, 
            0.0651, 0.0221),
        cuthoe = cms.vdouble(0.166, 0.0771, 0.144, 0.37, 0.0497, 
            0.139, 0.401, 2.68, 0.516, 0.234, 
            0.0556, 0.144, 0.368, 0.031, 0.12, 
            0.602, 2.01, 1.05, 0.104, 0.063, 
            0.0565, 0.38, 0.0192, 0.0294, 0.537, 
            4.65, 1.87),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 2.5, 2.5, 1.5, 2.5, 
            1.5, 1.5, 1.5, 1.5, 0.5, 
            2.5, 2.5, 0.5, 2.5, 1.5, 
            0.5, 1.5, 1.5, 0.5, 2.5, 
            0.5, 0.5),
        cutiso_sumoet = cms.vdouble(28.9, 15.3, 12.0, 18.3, 7.17, 
            9.42, 11.0, 9.81, 3.94, 22.7, 
            15.9, 12.3, 17.0, 7.58, 8.89, 
            15.2, 12.7, 6.17, 20.8, 21.2, 
            17.2, 15.5, 9.37, 10.6, 19.8, 
            22.1, 15.6),
        cutdcotdist = cms.vdouble(0.0393, 0.0392, 0.0397, 0.0394, 0.0393, 
            0.039, 0.0378, 0.0388, 0.0382, 0.0385, 
            0.0167, 0.00325, 0.0394, 0.0387, 0.0388, 
            0.0227, 0.0258, 0.0127, 0.0298, 0.03, 
            0.00946, 0.039, 0.0231, 0.0278, 0.00162, 
            0.0367, 0.0199),
        cutsee = cms.vdouble(0.0175, 0.0127, 0.0177, 0.0373, 0.0314, 
            0.0329, 0.0157, 0.0409, 0.14, 0.0169, 
            0.0106, 0.0142, 0.0363, 0.0322, 0.0354, 
            0.0117, 0.0372, 28.2, 0.0171, 0.0113, 
            0.014, 0.0403, 0.0323, 0.0411, 0.0104, 
            0.0436, 0.0114),
        cuteseedopcor = cms.vdouble(0.78, 0.302, 0.483, 0.904, 0.168, 
            0.645, 0.108, 0.284, 0.324, 0.591, 
            0.286, 0.488, 0.813, 0.791, 0.672, 
            0.398, 0.834, 0.878, 0.515, 0.937, 
            0.806, 0.816, 0.85, 0.507, 0.367, 
            0.83, 0.648),
        cutdphiin = cms.vdouble(0.041, 0.275, 0.365, 0.047, 0.273, 
            0.296, 0.329, 0.465, 0.627, 0.0581, 
            0.0954, 0.327, 0.0702, 0.0582, 0.279, 
            0.117, 0.318, 0.246, 0.0821, 0.052, 
            0.292, 0.116, 0.0435, 0.312, 0.118, 
            0.296, 0.0459),
        cutet = cms.vdouble(-100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, -100000.0, -100000.0, 
            -100000.0, -100000.0, -100000.0, 12.0, 12.0, 
            12.0, 12.0, 12.0, 12.0, 12.0, 
            12.0, 12.5)
    ),
    classbasedlooseEleIDCutsV06 = cms.PSet(
        cutdetain = cms.vdouble(0.0137, 0.00678, 0.0241, 0.0187, 0.0161, 
            0.0224, 0.0252, 0.0308, 0.0273),
        cutiso_sum = cms.vdouble(33.0, 17.0, 17.9, 18.8, 8.55, 
            12.5, 17.6, 18.5, 2.98),
        cutip_gsf = cms.vdouble(0.0551, 0.0765, 0.143, 0.0874, 0.594, 
            0.37, 0.0913, 1.15, 0.231),
        cutip_gsfl = cms.vdouble(0.0186, 0.0759, 0.138, 0.0473, 0.62, 
            0.304, 0.109, 0.775, 0.0479),
        cuthoe = cms.vdouble(0.247, 0.137, 0.147, 0.371, 0.0588, 
            0.147, 0.52, 0.452, 0.404),
        cutiso_sumoetl = cms.vdouble(11.3, 9.05, 9.07, 9.94, 5.25, 
            6.15, 10.7, 10.8, 4.4),
        cutfmishits = cms.vdouble(4.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 4.5, 3.5, 3.5),
        cuthoel = cms.vdouble(0.236, 0.126, 0.147, 0.375, 0.0392, 
            0.145, 0.365, 0.383, 0.384),
        cutdphiin = cms.vdouble(0.0897, 0.262, 0.353, 0.116, 0.357, 
            0.319, 0.342, 0.404, 0.336),
        cutseel = cms.vdouble(0.0164, 0.0118, 0.015, 0.0523, 0.0326, 
            0.0456, 0.0185, 0.0589, 0.0544),
        cutiso_sumoet = cms.vdouble(34.5, 12.7, 12.1, 19.9, 6.35, 
            8.85, 14.0, 10.5, 9.74),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0176, 0.0125, 0.0181, 0.0415, 0.0364, 
            0.0418, 0.0146, 0.0678, 0.133),
        cuteseedopcor = cms.vdouble(0.63, 0.82, 0.401, 0.718, 0.4, 
            0.458, 0.15, 0.664, 0.373),
        cutdphiinl = cms.vdouble(0.0747, 0.25, 0.356, 0.0956, 0.347, 
            0.326, 0.333, 0.647, 0.289),
        cutdetainl = cms.vdouble(0.0124, 0.00503, 0.0257, 0.0228, 0.0118, 
            0.0178, 0.0188, 0.14, 0.024)
    ),
    src = cms.InputTag("gsfElectrons"),
    robusttightEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.0201, 0.0102, 0.0211, 0.00606, -1, 
            -1, 2.34, 3.24, 4.51, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.00253, 0.0291, 0.022, 0.0032, -1, 
            -1, 0.826, 2.7, 0.255, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    classbasedtightEleIDCuts = cms.PSet(
        cutdetain = cms.vdouble(0.0116, 0.00449, 0.00938, 0.0184, 0.00678, 
            0.0109, 0.0252, 0.0268, 0.0139),
        cutiso_sum = cms.vdouble(15.5, 12.2, 12.2, 11.7, 7.16, 
            9.71, 8.66, 11.9, 2.98),
        cutip_gsf = cms.vdouble(0.0131, 0.0586, 0.0839, 0.0366, 0.452, 
            0.204, 0.0913, 0.0802, 0.0731),
        cutip_gsfl = cms.vdouble(0.0119, 0.0527, 0.0471, 0.0212, 0.233, 
            0.267, 0.109, 0.122, 0.0479),
        cuthoe = cms.vdouble(0.215, 0.0608, 0.147, 0.369, 0.0349, 
            0.102, 0.52, 0.422, 0.404),
        cutiso_sumoetl = cms.vdouble(6.21, 6.81, 5.3, 5.39, 2.73, 
            4.73, 4.84, 3.46, 3.73),
        cutfmishits = cms.vdouble(1.5, 1.5, 1.5, 2.5, 2.5, 
            1.5, 1.5, 2.5, 0.5),
        cuthoel = cms.vdouble(0.228, 0.0836, 0.143, 0.37, 0.0392, 
            0.0979, 0.3, 0.381, 0.339),
        cutdphiin = cms.vdouble(0.0897, 0.0993, 0.295, 0.0979, 0.151, 
            0.252, 0.341, 0.308, 0.328),
        cutseel = cms.vdouble(0.0132, 0.0117, 0.0112, 0.0387, 0.0281, 
            0.0287, 0.00987, 0.0296, 0.0544),
        cutiso_sumoet = cms.vdouble(11.9, 7.81, 6.28, 8.92, 4.65, 
            5.49, 9.36, 8.84, 5.94),
        cutdcotdist = cms.vdouble(9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0),
        cutsee = cms.vdouble(0.0145, 0.0116, 0.012, 0.039, 0.0297, 
            0.0311, 0.00987, 0.0347, 0.0917),
        cuteseedopcor = cms.vdouble(0.637, 0.943, 0.742, 0.748, 0.763, 
            0.631, 0.214, 0.873, 0.473),
        cutdphiinl = cms.vdouble(0.061, 0.14, 0.286, 0.0921, 0.197, 
            0.24, 0.333, 0.303, 0.258),
        cutdetainl = cms.vdouble(0.00816, 0.00401, 0.0081, 0.019, 0.00588, 
            0.00893, 0.0171, 0.0434, 0.0143)
    ),
    algorithm = cms.string('eIDCB'),
    robusthighenergyEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 9999, 0.09, 0.005, 0.94, 
            0.83, 7.5, 2, 0.03, 9999.0, 
            0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.05, 0.03, 0.09, 0.007, -1, 
            -1, 15, 2.5, 0.03, 2.5, 
            0, 0.5, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCuts = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV02 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV03 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV00 = cms.PSet(
        barrel = cms.vdouble(0.115, 0.014, 0.09, 0.009, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.15, 0.0275, 0.092, 0.0105, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV01 = cms.PSet(
        barrel = cms.vdouble(0.075, 0.0132, 0.058, 0.0077, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.083, 0.027, 0.042, 0.01, -1, 
            -1, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    robustlooseEleIDCutsV04 = cms.PSet(
        barrel = cms.vdouble(0.05, 0.0103, 0.8, 0.00688, -1, 
            -1, 7.33, 4.68, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0),
        endcap = cms.vdouble(0.0389, 0.0307, 0.7, 0.00944, -1, 
            -1, 7.76, 3.09, 2.23, 9999.0, 
            9999.0, 9999.0, 9999.0, 9999.0, 9999.0, 
            9999.0, 9999.0, 9999.0, 0.0, -9999.0, 
            9999.0, 9999.0, 9999, -1, 0, 
            0)
    ),
    additionalCategories = cms.bool(True),
    etBinning = cms.bool(True)
)


process.eleIsoDepositEcalFromHits = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("gsfElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        isolationVariable = cms.string('et'),
        tryBoth = cms.bool(True),
        intStrip = cms.double(0.0),
        ComponentName = cms.string('EgammaRecHitExtractor'),
        endcapEcalHits = cms.InputTag("reducedEcalRecHitsEE"),
        recHitFlagsToBeExcluded = cms.vstring('kFaultyHardware', 
            'kPoorCalib', 
            'kTowerRecovered', 
            'kDead'),
        intRadius = cms.double(0.0),
        severityLevelCut = cms.int32(4),
        energyMin = cms.double(0.08),
        extRadius = cms.double(0.6),
        subtractSuperClusterEnergy = cms.bool(False),
        vetoClustered = cms.bool(False),
        etMin = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        barrelEcalHits = cms.InputTag("reducedEcalRecHitsEB")
    )
)


process.eleIsoDepositHcalFromTowers = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("gsfElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        caloTowers = cms.InputTag("towerMaker"),
        ComponentName = cms.string('EgammaTowerExtractor'),
        hcalDepth = cms.int32(-1),
        intRadius = cms.double(0.0),
        extRadius = cms.double(0.6),
        DepositLabel = cms.untracked.string(''),
        etMin = cms.double(-999.0)
    )
)


process.eleIsoDepositTk = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("gsfElectrons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        dzOption = cms.string('vz'),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('EgammaTrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(9999.0),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.0),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        inputTrackCollection = cms.InputTag("generalTracks")
    )
)


process.eleIsoFromDepsEcalFromHitsByCrystal = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("eleIsoDepositEcalFromHits"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('NumCrystalVeto(3.0)', 
            'NumCrystalEtaPhiVeto(1.5,9999.0)', 
            'EcalBarrel:AbsThresholdFromTransverse(0.08)', 
            'EcalEndcaps:AbsThreshold(0.100)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.eleIsoFromDepsHcalFromTowers = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("eleIsoDepositHcalFromTowers"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.15'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.eleIsoFromDepsTk = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("eleIsoDepositTk"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('RectangularEtaPhiVeto(-0.015,0.015,-0.5,0.5)', 
            'Threshold(0.7)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.electronMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("gsfElectrons"),
    maxDPtRel = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.5),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.gamIsoDepositEcalFromHits = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("photons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        isolationVariable = cms.string('et'),
        tryBoth = cms.bool(True),
        intStrip = cms.double(0.0),
        ComponentName = cms.string('EgammaRecHitExtractor'),
        endcapEcalHits = cms.InputTag("reducedEcalRecHitsEE"),
        recHitFlagsToBeExcluded = cms.vstring('kFaultyHardware', 
            'kPoorCalib', 
            'kTowerRecovered', 
            'kDead'),
        intRadius = cms.double(0.0),
        severityLevelCut = cms.int32(4),
        energyMin = cms.double(0.08),
        extRadius = cms.double(0.6),
        subtractSuperClusterEnergy = cms.bool(False),
        vetoClustered = cms.bool(False),
        detector = cms.string('Ecal'),
        etMin = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        barrelEcalHits = cms.InputTag("reducedEcalRecHitsEB")
    )
)


process.gamIsoDepositHcalFromTowers = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("photons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        caloTowers = cms.InputTag("towerMaker"),
        ComponentName = cms.string('EgammaTowerExtractor'),
        hcalDepth = cms.int32(-1),
        intRadius = cms.double(0.0),
        extRadius = cms.double(0.6),
        DepositLabel = cms.untracked.string(''),
        etMin = cms.double(-999.0)
    )
)


process.gamIsoDepositTk = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("photons"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        dzOption = cms.string('vz'),
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ComponentName = cms.string('EgammaTrackExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(9999.0),
        Chi2Prob_Min = cms.double(-1.0),
        DR_Veto = cms.double(0.0),
        NHits_Min = cms.uint32(0),
        Chi2Ndof_Max = cms.double(1e+64),
        Pt_Min = cms.double(-1.0),
        DepositLabel = cms.untracked.string(''),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        inputTrackCollection = cms.InputTag("generalTracks")
    )
)


process.gamIsoFromDepsEcalFromHits = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("gamIsoDepositEcalFromHits"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('EcalBarrel:0.045', 
            'EcalBarrel:RectangularEtaPhiVeto(-0.02,0.02,-0.5,0.5)', 
            'EcalBarrel:AbsThresholdFromTransverse(0.080)', 
            'EcalEndcaps:0.070', 
            'EcalEndcaps:RectangularEtaPhiVeto(-0.02,0.02,-0.5,0.5)', 
            'EcalEndcaps:AbsThreshold(0.100)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.gamIsoFromDepsHcalFromTowers = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("gamIsoDepositHcalFromTowers"),
        deltaR = cms.double(0.4),
        weight = cms.string('1'),
        vetos = cms.vstring('0.15'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.gamIsoFromDepsTk = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        src = cms.InputTag("gamIsoDepositTk"),
        deltaR = cms.double(0.3),
        weight = cms.string('1'),
        vetos = cms.vstring('RectangularEtaPhiVeto(-0.015,0.015,-0.5,0.5)', 
            'Threshold(1.0)'),
        skipDefaultVeto = cms.bool(True),
        mode = cms.string('sum')
    ))
)


process.generalTracks = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(False),
    MinPT = cms.double(0.05),
    makeReKeyedSeeds = cms.untracked.bool(False),
    copyExtras = cms.untracked.bool(True),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("initialStepSelector","initialStep"), cms.InputTag("lowPtTripletStepSelector","lowPtTripletStep"), cms.InputTag("pixelPairStepSelector","pixelPairStep"), cms.InputTag("detachedTripletStep"), cms.InputTag("mixedTripletStep"), 
        cms.InputTag("pixelLessStepSelector","pixelLessStep"), cms.InputTag("tobTecStepSelector","tobTecStep")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1, 1, 1, 1, 1, 
        1, 1),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(0, 1, 2, 3, 4, 
            5, 6)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("initialStepTracks"), cms.InputTag("lowPtTripletStepTracks"), cms.InputTag("pixelPairStepTracks"), cms.InputTag("detachedTripletStepTracks"), cms.InputTag("mixedTripletStepTracks"), 
        cms.InputTag("pixelLessStepTracks"), cms.InputTag("tobTecStepTracks")),
    newQuality = cms.string('confirmed')
)


process.ghostTrackBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('ghostTrack'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("ghostTrackVertexTagInfos"))
)


process.ghostTrackVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        primcut = cms.double(2.0),
        seccut = cms.double(4.0),
        maxFitChi2 = cms.double(10.0),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        mergeThreshold = cms.double(3.0),
        finder = cms.string('gtvr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(1),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.globalCombinedSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("globalSeedsFromTripletsWithVertices"), cms.InputTag("globalSeedsFromPairsWithVertices"))
)


process.globalMixedSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(21.2)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('MixedLayerPairs')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalPixelLessSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(40)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(5000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('pixelLessLayerPairs4PixelLessTracking')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalPixelSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(21.2)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('PixelLayerPairs')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalSeedsFromPairsWithVertices = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            useFixedError = cms.bool(True),
            originRadius = cms.double(0.2),
            sigmaZVertex = cms.double(3.0),
            fixedError = cms.double(0.2),
            VertexCollection = cms.InputTag("pixelVertices"),
            ptMin = cms.double(0.9),
            useFoundVertices = cms.bool(True),
            nSigmaZ = cms.double(4.0)
        ),
        ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('MixedLayerPairs')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.globalSeedsFromTriplets = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(0.2),
            ptMin = cms.double(0.9),
            originHalfLength = cms.double(21.2)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('PixelLayerTriplets')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.impactParameterMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('impactParameterMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.impactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeGhostTrack = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.impactParameterTagInfosAOD = cms.EDProducer("TrackIPProducer",
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag("jetTracksAssociatorAtVertex"),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5.0)
)


process.initialStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('PixelLayerTriplets')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(0.03),
            nSigmaZ = cms.double(4.0),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            ptMin = cms.double(0.6)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.initialStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("initialStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(0),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(0.45, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(0.65, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('initialStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.01),
        d0_par2 = cms.vdouble(0.55, 4.0),
        d0_par1 = cms.vdouble(0.55, 4.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('initialStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('initialStepLoose'),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            res_par = cms.vdouble(0.003, 0.01)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.35, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('initialStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            preFilterName = cms.string('initialStepTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.initialStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("initialStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('initialStepTrajectoryBuilder')
)


process.initialStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("initialStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter0'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.jetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetBProbabilityBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.jetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetProbabilityBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbability'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.jetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    jets = cms.InputTag("ak5PFJets"),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)


process.kt6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    doAreaFastjet = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    maxBadHcalCells = cms.uint32(9999999),
    doAreaDiskApprox = cms.bool(False),
    maxRecoveredEcalCells = cms.uint32(9999999),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    Ghost_EtaMax = cms.double(5.0),
    doRhoFastjet = cms.bool(True),
    jetAlgorithm = cms.string('Kt'),
    nSigmaPU = cms.double(1.0),
    GhostArea = cms.double(0.01),
    Rho_EtaMax = cms.double(4.4),
    maxBadEcalCells = cms.uint32(9999999),
    useDeterministicSeed = cms.bool(True),
    doPVCorrection = cms.bool(False),
    maxRecoveredHcalCells = cms.uint32(9999999),
    rParam = cms.double(0.6),
    maxProblematicHcalCells = cms.uint32(9999999),
    doOutputJets = cms.bool(True),
    src = cms.InputTag("particleFlow"),
    inputEtMin = cms.double(0.0),
    srcPVs = cms.InputTag(""),
    jetPtMin = cms.double(3.0),
    radiusPU = cms.double(0.5),
    maxProblematicEcalCells = cms.uint32(9999999),
    doPUOffsetCorr = cms.bool(False),
    inputEMin = cms.double(0.0)
)


process.lowPtTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("initialStepTracks"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("initialStepSelector","initialStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.lowPtTripletStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.037),
            ComponentName = cms.string('PixelTripletHLTGenerator')
        ),
        SeedingLayers = cms.string('lowPtTripletStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(0.03),
            nSigmaZ = cms.double(4.0),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            ptMin = cms.double(0.2)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.lowPtTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("lowPtTripletStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(0),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(0.45, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(0.65, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('lowPtTripletStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.01),
        d0_par2 = cms.vdouble(0.55, 4.0),
        d0_par1 = cms.vdouble(0.55, 4.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('lowPtTripletStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('lowPtTripletStepLoose'),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            res_par = cms.vdouble(0.003, 0.01)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.35, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('lowPtTripletStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            preFilterName = cms.string('lowPtTripletStepTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.lowPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("lowPtTripletStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('lowPtTripletStepTrajectoryBuilder')
)


process.lowPtTripletStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("lowPtTripletStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter1'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.metJESCorAK5CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('ak5CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ak5CaloL2L3'),
    UscaleA = cms.double(2.0),
    UscaleB = cms.double(1.3),
    UscaleC = cms.double(0.1),
    refcorrector = cms.string('ic5CaloL1Fastjet')
)


process.metJESCorAK5CaloJetMuons = cms.EDProducer("MuonMET",
    muonMETDepositValueMapInputTag = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    metTypeInputTag = cms.InputTag("CaloMET"),
    muonsInputTag = cms.InputTag("muons"),
    uncorMETInputTag = cms.InputTag("metJESCorAK5CaloJet")
)


process.metJESCorAK5PFJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('ak5PFJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('PFMET'),
    jetPTthreshold = cms.double(10.0),
    inputUncorMetLabel = cms.string('pfMet'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ak5PFL2L3'),
    UscaleA = cms.double(1.5),
    UscaleB = cms.double(0.0),
    UscaleC = cms.double(0.0),
    refcorrector = cms.string('ak5PFL1Fastjet')
)


process.metJESCorAK7CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('ak7CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ak7CaloL2L3'),
    UscaleA = cms.double(2.0),
    UscaleB = cms.double(1.3),
    UscaleC = cms.double(0.1),
    refcorrector = cms.string('ic5CaloL1Fastjet')
)


process.metJESCorIC5CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('iterativeCone5CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('ic5CaloL2L3'),
    UscaleA = cms.double(2.0),
    UscaleB = cms.double(1.3),
    UscaleC = cms.double(0.1),
    refcorrector = cms.string('ic5CaloL1Fastjet')
)


process.metJESCorKT4CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('kt4CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('kt4CaloL2L3'),
    UscaleA = cms.double(2.0),
    UscaleB = cms.double(1.3),
    UscaleC = cms.double(0.1),
    refcorrector = cms.string('ic5CaloL1Fastjet')
)


process.metJESCorKT6CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('kt6CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('kt6CaloL2L3'),
    UscaleA = cms.double(2.0),
    UscaleB = cms.double(1.3),
    UscaleC = cms.double(0.1),
    refcorrector = cms.string('ic5CaloL1Fastjet')
)


process.metJESCorSC5CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('sisCone5CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('sisCone5CaloL2L3'),
    UscaleA = cms.double(2.0),
    UscaleB = cms.double(1.3),
    UscaleC = cms.double(0.1),
    refcorrector = cms.string('ic5CaloL1Fastjet')
)


process.metJESCorSC7CaloJet = cms.EDProducer("Type1MET",
    inputUncorJetsLabel = cms.string('sisCone7CaloJets'),
    jetEMfracLimit = cms.double(0.9),
    metType = cms.string('CaloMET'),
    jetPTthreshold = cms.double(20.0),
    inputUncorMetLabel = cms.string('met'),
    subtractL1Fast = cms.bool(False),
    hasMuonsCorr = cms.bool(False),
    useTypeII = cms.bool(False),
    corrector = cms.string('sisCone7CaloL2L3'),
    UscaleA = cms.double(2.0),
    UscaleB = cms.double(1.3),
    UscaleC = cms.double(0.1),
    refcorrector = cms.string('ic5CaloL1Fastjet')
)


process.mixedTripletStep = cms.EDProducer("TrackListMerger",
    ShareFrac = cms.double(0.19),
    writeOnlyTrkQuals = cms.bool(True),
    MinPT = cms.double(0.05),
    copyExtras = cms.untracked.bool(False),
    Epsilon = cms.double(-0.001),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("mixedTripletStepSelector","mixedTripletStepVtx"), cms.InputTag("mixedTripletStepSelector","mixedTripletStepTrk")),
    allowFirstHitShare = cms.bool(True),
    MaxNormalizedChisq = cms.double(1000.0),
    hasSelector = cms.vint32(1, 1),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(0, 1)
    )),
    MinFound = cms.int32(3),
    TrackProducers = cms.VInputTag(cms.InputTag("mixedTripletStepTracks"), cms.InputTag("mixedTripletStepTracks")),
    newQuality = cms.string('confirmed')
)


process.mixedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("detachedTripletStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("detachedTripletStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.mixedTripletStepSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"), cms.InputTag("mixedTripletStepSeedsB"))
)


process.mixedTripletStepSeedsA = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            ComponentName = cms.string('PixelTripletLargeTipGenerator'),
            extraHitRPhitolerance = cms.double(0.0),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.0)
        ),
        SeedingLayers = cms.string('mixedTripletStepSeedLayersA')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(2.0),
            ptMin = cms.double(0.35),
            originHalfLength = cms.double(10.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.mixedTripletStepSeedsB = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            maxElement = cms.uint32(100000),
            ComponentName = cms.string('PixelTripletLargeTipGenerator'),
            extraHitRPhitolerance = cms.double(0.0),
            useMultScattering = cms.bool(True),
            phiPreFiltering = cms.double(0.3),
            extraHitRZtolerance = cms.double(0.0)
        ),
        SeedingLayers = cms.string('mixedTripletStepSeedLayersB')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(2.0),
            ptMin = cms.double(0.5),
            originHalfLength = cms.double(10.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.mixedTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("mixedTripletStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(2),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(3),
        chi2n_par = cms.double(1.2),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.3, 3.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.2, 3.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('mixedTripletStepVtxLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(1.3, 3.0),
        d0_par1 = cms.vdouble(1.2, 3.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('loose'),
            minNumberLayers = cms.uint32(4),
            chi2n_par = cms.double(0.6),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.2, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.2, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepTrkLoose'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.2, 4.0),
            d0_par1 = cms.vdouble(1.2, 4.0),
            preFilterName = cms.string('')
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.6),
            dz_par1 = cms.vdouble(1.1, 3.0),
            dz_par2 = cms.vdouble(1.2, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepVtxTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('mixedTripletStepVtxLoose'),
            d0_par2 = cms.vdouble(1.2, 3.0),
            d0_par1 = cms.vdouble(1.1, 3.0),
            res_par = cms.vdouble(0.003, 0.001)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(4),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.4),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepTrkTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('mixedTripletStepTrkLoose'),
            d0_par2 = cms.vdouble(1.1, 4.0),
            d0_par1 = cms.vdouble(1.1, 4.0),
            res_par = cms.vdouble(0.003, 0.001)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.4),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.2, 3.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.1, 3.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepVtx'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.2, 3.0),
            d0_par1 = cms.vdouble(1.1, 3.0),
            preFilterName = cms.string('mixedTripletStepVtxTight')
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(4),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.3),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.9, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.9, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('mixedTripletStepTrk'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.9, 4.0),
            d0_par1 = cms.vdouble(0.9, 4.0),
            preFilterName = cms.string('mixedTripletStepTrkTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.mixedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("mixedTripletStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('mixedTripletStepTrajectoryBuilder')
)


process.mixedTripletStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("mixedTripletStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter4'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.muonMETValueMapProducer = cms.EDProducer("MuonMETValueMapProducer",
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(False),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(False),
        useCalo = cms.bool(True),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(False)
    ),
    beamSpotInputTag = cms.InputTag("offlineBeamSpot"),
    minPt = cms.double(10.0),
    maxNormChi2 = cms.double(10.0),
    minnValidStaHits = cms.int32(1),
    useHO = cms.bool(False),
    minnHits = cms.int32(11),
    useTrackAssociatorPositions = cms.bool(True),
    useRecHits = cms.bool(False),
    maxEta = cms.double(2.5),
    maxd0 = cms.double(0.2),
    towerEtThreshold = cms.double(0.3),
    isAlsoTkMu = cms.bool(True),
    muonInputTag = cms.InputTag("muons")
)


process.muonMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("muons"),
    maxDPtRel = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.5),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.newCombinedSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("initialStepSeeds"), cms.InputTag("pixelPairStepSeeds"), cms.InputTag("mixedTripletStepSeeds"), cms.InputTag("pixelLessStepSeeds"))
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    embedHighLevelSelection = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    electronSource = cms.InputTag("gsfElectrons"),
    resolutions = cms.PSet(

    ),
    userIsolation = cms.PSet(

    ),
    embedSuperCluster = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    pfElectronSource = cms.InputTag("pfIsolatedElectrons"),
    addElectronID = cms.bool(True),
    efficiencies = cms.PSet(

    ),
    embedGsfTrack = cms.bool(True),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    embedTrack = cms.bool(False),
    addEfficiencies = cms.bool(False),
    usePV = cms.bool(True),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    electronIDSources = cms.PSet(
        eidTight = cms.InputTag("eidTight"),
        eidLoose = cms.InputTag("eidLoose"),
        eidRobustTight = cms.InputTag("eidRobustTight"),
        eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
        eidRobustLoose = cms.InputTag("eidRobustLoose")
    ),
    genParticleMatch = cms.InputTag("electronMatch"),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    isoDeposits = cms.PSet(

    ),
    embedGenMatch = cms.bool(True)
)


process.patHemispheres = cms.EDProducer("PATHemisphereProducer",
    patJets = cms.InputTag("cleanLayer1Jets"),
    maxTauEta = cms.double(-1),
    maxPhotonEta = cms.double(5),
    minMuonEt = cms.double(7),
    patMuons = cms.InputTag("cleanLayer1Muons"),
    seedMethod = cms.int32(3),
    patElectrons = cms.InputTag("cleanLayer1Electrons"),
    patMets = cms.InputTag("layer1METs"),
    maxMuonEta = cms.double(5),
    minTauEt = cms.double(1000000),
    minPhotonEt = cms.double(200000),
    minElectronEt = cms.double(7),
    patPhotons = cms.InputTag("cleanLayer1Photons"),
    combinationMethod = cms.int32(3),
    maxJetEta = cms.double(5),
    maxElectronEta = cms.double(5),
    minJetEt = cms.double(30),
    patTaus = cms.InputTag("cleanLayer1Taus")
)


process.patJetCharge = cms.EDProducer("JetChargeProducer",
    var = cms.string('Pt'),
    src = cms.InputTag("jetTracksAssociatorAtVertex"),
    exp = cms.double(1.0)
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    src = cms.InputTag("ak5PFJets"),
    emf = cms.bool(False),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    useNPV = cms.bool(True),
    rho = cms.InputTag("kt6PFJets","rho"),
    useRho = cms.bool(True),
    payload = cms.string('AK5PF'),
    flavorType = cms.string('J')
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("patJetPartonAssociation"),
    physicsDefinition = cms.bool(False)
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("ak5PFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("ak5GenJets")
)


process.patJetPartonAssociation = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("ak5PFJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("patJetPartons")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("ak5PFJets"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.4),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.patJetPartons = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    addJetCharge = cms.bool(True),
    addGenJetMatch = cms.bool(True),
    embedPFCandidates = cms.bool(True),
    embedGenJetMatch = cms.bool(True),
    addAssociatedTracks = cms.bool(True),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    addGenPartonMatch = cms.bool(True),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociation"),
    resolutions = cms.PSet(

    ),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    addTagInfos = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(True),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    jetSource = cms.InputTag("ak5PFJets"),
    addEfficiencies = cms.bool(False),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactors")),
    trackAssociationSource = cms.InputTag("jetTracksAssociatorAtVertex"),
    tagInfoSources = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"), cms.InputTag("secondaryVertexTagInfosAOD"), cms.InputTag("softMuonTagInfosAOD")),
    discriminatorSources = cms.VInputTag(cms.InputTag("jetBProbabilityBJetTagsAOD"), cms.InputTag("jetProbabilityBJetTagsAOD"), cms.InputTag("trackCountingHighPurBJetTagsAOD"), cms.InputTag("trackCountingHighEffBJetTagsAOD"), cms.InputTag("simpleSecondaryVertexHighEffBJetTagsAOD"), 
        cms.InputTag("simpleSecondaryVertexHighPurBJetTagsAOD"), cms.InputTag("combinedSecondaryVertexBJetTagsAOD"), cms.InputTag("combinedSecondaryVertexMVABJetTagsAOD"), cms.InputTag("softMuonBJetTagsAOD"), cms.InputTag("softMuonByPtBJetTagsAOD"), 
        cms.InputTag("softMuonByIP3dBJetTagsAOD")),
    addBTagInfo = cms.bool(True),
    embedCaloTowers = cms.bool(True),
    addResolutions = cms.bool(False),
    getJetMCFlavour = cms.bool(True),
    addDiscriminators = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    addJetCorrFactors = cms.bool(True),
    jetIDMap = cms.InputTag("ak5pfJetID"),
    addJetID = cms.bool(True)
)


process.patMETs = cms.EDProducer("PATMETProducer",
    metSource = cms.InputTag("metJESCorAK5CaloJetMuons"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addResolutions = cms.bool(False),
    addEfficiencies = cms.bool(False),
    genMETSource = cms.InputTag("genMetTrue"),
    efficiencies = cms.PSet(

    ),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(True),
    muonSource = cms.InputTag("muons"),
    resolutions = cms.PSet(

    )
)


process.patMHTs = cms.EDProducer("PATMHTProducer",
    verbose = cms.double(0.0),
    muonEtaMax = cms.double(2.5),
    jetTag = cms.untracked.InputTag("allLayer1Jets"),
    eleEtaMax = cms.double(3.0),
    noHF = cms.bool(False),
    muonTag = cms.untracked.InputTag("allLayer1Muons"),
    CaloTowerTag = cms.InputTag("towerMaker"),
    elePhiUncertaintyParameter0 = cms.double(0.01),
    uncertaintyScaleFactor = cms.double(1.0),
    muonPtMin = cms.double(10.0),
    eleEtUncertaintyParameter0 = cms.double(0.01),
    useHO = cms.bool(False),
    jetEtUncertaintyParameter2 = cms.double(0.033),
    jetEtUncertaintyParameter1 = cms.double(1.25),
    jetEMfracMax = cms.double(0.9),
    jetPhiUncertaintyParameter2 = cms.double(0.023),
    jetPhiUncertaintyParameter0 = cms.double(4.75),
    jetPhiUncertaintyParameter1 = cms.double(-0.426),
    tauTag = cms.untracked.InputTag("allLayer1Taus"),
    jetEtUncertaintyParameter0 = cms.double(5.6),
    electronTag = cms.untracked.InputTag("allLayer1Electrons"),
    jetEtaMax = cms.double(5.0),
    elePtMin = cms.double(10.0),
    jetPtMin = cms.double(20.0),
    muonEtUncertaintyParameter0 = cms.double(0.01),
    photonTag = cms.untracked.InputTag("allLayer1Photons"),
    muonPhiUncertaintyParameter0 = cms.double(0.01),
    controlledUncertainty = cms.bool(True),
    towerEtThreshold = cms.double(0.5)
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    embedTpfmsMuon = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedCaloMETMuonCorrs = cms.bool(True),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    resolutions = cms.PSet(

    ),
    embedDytMuon = cms.bool(True),
    userIsolation = cms.PSet(

    ),
    embedPFCandidate = cms.bool(True),
    pfMuonSource = cms.InputTag("pfIsolatedMuons"),
    efficiencies = cms.PSet(

    ),
    embedStandAloneMuon = cms.bool(True),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    embedTrack = cms.bool(False),
    addEfficiencies = cms.bool(False),
    usePV = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(True),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    muonSource = cms.InputTag("muons"),
    embedCombinedMuon = cms.bool(True),
    genParticleMatch = cms.InputTag("muonMatch"),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    isoDeposits = cms.PSet(

    ),
    embedGenMatch = cms.bool(True),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    embedPickyMuon = cms.bool(True)
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addEfficiencies = cms.bool(False),
    photonIDSources = cms.PSet(
        PhotonCutBasedIDTight = cms.InputTag("PhotonIDProd","PhotonCutBasedIDTight"),
        PhotonCutBasedIDLoose = cms.InputTag("PhotonIDProd","PhotonCutBasedIDLoose")
    ),
    isoDeposits = cms.PSet(

    ),
    efficiencies = cms.PSet(

    ),
    embedSuperCluster = cms.bool(True),
    embedGenMatch = cms.bool(True),
    resolutions = cms.PSet(

    ),
    addPhotonID = cms.bool(True),
    photonSource = cms.InputTag("photons"),
    userIsolation = cms.PSet(

    ),
    genParticleMatch = cms.InputTag("photonMatch")
)


process.patTaus = cms.EDProducer("PATTauProducer",
    tauIDSources = cms.PSet(
        leadingPionPtCut = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingPionPtCut"),
        byIsolationUsingLeadingPion = cms.InputTag("shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion"),
        againstMuon = cms.InputTag("shrinkingConePFTauDiscriminationAgainstMuon"),
        againstElectron = cms.InputTag("shrinkingConePFTauDiscriminationAgainstElectron"),
        leadingTrackFinding = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding")
    ),
    addGenJetMatch = cms.bool(True),
    embedGenJetMatch = cms.bool(True),
    embedLeadTrack = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    addTauJetCorrFactors = cms.bool(False),
    resolutions = cms.PSet(

    ),
    userIsolation = cms.PSet(
        pfAllParticles = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFCandidates"),
            deltaR = cms.double(0.5)
        ),
        pfNeutralHadron = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFNeutralHadrons"),
            deltaR = cms.double(0.5)
        ),
        pfChargedHadron = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFChargedHadrons"),
            deltaR = cms.double(0.5)
        ),
        pfGamma = cms.PSet(
            threshold = cms.double(0.0),
            src = cms.InputTag("tauIsoDepositPFGammas"),
            deltaR = cms.double(0.5)
        )
    ),
    embedIsolationPFGammaCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genJetMatch = cms.InputTag("tauGenJetMatch"),
    embedIsolationPFCands = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    embedSignalPFCands = cms.bool(False),
    addEfficiencies = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    tauSource = cms.InputTag("shrinkingConePFTauProducer"),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    addTauID = cms.bool(True),
    genParticleMatch = cms.InputTag("tauMatch"),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    isoDeposits = cms.PSet(
        pfAllParticles = cms.InputTag("tauIsoDepositPFCandidates"),
        pfNeutralHadron = cms.InputTag("tauIsoDepositPFNeutralHadrons"),
        pfChargedHadron = cms.InputTag("tauIsoDepositPFChargedHadrons"),
        pfGamma = cms.InputTag("tauIsoDepositPFGammas")
    ),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedGenMatch = cms.bool(True),
    embedLeadPFNeutralCand = cms.bool(False)
)


process.pfNoPileUp = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowTmp"),
    enable = cms.bool(True),
    topCollection = cms.InputTag("pfPileUp"),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUpIso = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlow"),
    enable = cms.bool(True),
    topCollection = cms.InputTag("pfPileUpIso"),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    verbose = cms.untracked.bool(False)
)


process.pfPileUp = cms.EDProducer("PFPileUp",
    PFCandidates = cms.InputTag("particleFlowTmp"),
    Enable = cms.bool(True),
    checkClosestZVertex = cms.bool(True),
    verbose = cms.untracked.bool(False),
    Vertices = cms.InputTag("offlinePrimaryVertices")
)


process.pfPileUpIso = cms.EDProducer("PFPileUp",
    checkClosestZVertex = cms.bool(True),
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlow"),
    verbose = cms.untracked.bool(False),
    Vertices = cms.InputTag("offlinePrimaryVertices")
)


process.photonConvTrajSeedFromSingleLeg = cms.EDProducer("PhotonConversionTrajectorySeedProducerFromSingleLeg",
    vtxMinDoF = cms.double(4),
    beamSpotInputTag = cms.InputTag("offlineBeamSpot"),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        MaxNumberOfPixelClusters = cms.uint32(20000),
        cut = cms.string('strip < 150000 && pixel < 20000 && (strip < 50000 || (strip < 20000 + 7* pixel))'),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters")
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            originRadius = cms.double(3.0),
            ptMin = cms.double(0.2),
            originHalfLength = cms.double(12.0),
            beamSpot = cms.InputTag("offlineBeamSpot")
        )
    ),
    DoxcheckSeedCandidates = cms.bool(False),
    xcheckSeedCandidates = cms.string('xcheckSeedCandidates'),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedForPhotonConversion1Leg'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    ),
    TrackRefitter = cms.InputTag("generalTracks"),
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(10000),
        SeedingLayers = cms.string('convLayerPairs'),
        maxHitPairsPerTrackAndGenerator = cms.uint32(10)
    ),
    applyTkVtxConstraint = cms.bool(True),
    maxDZSigmas = cms.double(10.0),
    maxNumSelVtx = cms.uint32(2),
    primaryVerticesTag = cms.InputTag("pixelVertices"),
    newSeedCandidates = cms.string('convSeedCandidates')
)


process.photonMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("photons"),
    maxDPtRel = cms.double(1.0),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.2),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.pixelLessStepClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("mixedTripletStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("mixedTripletStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.pixelLessStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('pixelLessStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(2.0),
            ptMin = cms.double(0.6),
            originHalfLength = cms.double(10.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.pixelLessStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("pixelLessStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(3),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(5),
        chi2n_par = cms.double(0.5),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.5, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.5, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('pixelLessStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(1.5, 4.0),
        d0_par1 = cms.vdouble(1.5, 4.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.35),
            dz_par1 = cms.vdouble(1.2, 4.0),
            dz_par2 = cms.vdouble(1.2, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelLessStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('pixelLessStepLoose'),
            d0_par2 = cms.vdouble(1.2, 4.0),
            d0_par1 = cms.vdouble(1.2, 4.0),
            res_par = cms.vdouble(0.003, 0.001)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.25),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.0, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.0, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelLessStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.0, 4.0),
            d0_par1 = cms.vdouble(1.0, 4.0),
            preFilterName = cms.string('pixelLessStepTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.pixelLessStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("pixelLessStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('pixelLessStepTrajectoryBuilder')
)


process.pixelLessStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("pixelLessStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter5'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.pixelPairStepClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("lowPtTripletStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("lowPtTripletStepSelector","lowPtTripletStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.pixelPairStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('pixelPairStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            useFixedError = cms.bool(True),
            originRadius = cms.double(0.01),
            sigmaZVertex = cms.double(3.0),
            fixedError = cms.double(0.03),
            VertexCollection = cms.InputTag("pixelVertices"),
            ptMin = cms.double(0.6),
            useFoundVertices = cms.bool(True),
            nSigmaZ = cms.double(4.0)
        ),
        ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.pixelPairStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("pixelPairStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(0),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(0),
        chi2n_par = cms.double(1.6),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(0.45, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(0.65, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(999),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('pixelPairStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.01),
        d0_par2 = cms.vdouble(0.55, 4.0),
        d0_par1 = cms.vdouble(0.55, 4.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelPairStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('pixelPairStepLoose'),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            res_par = cms.vdouble(0.003, 0.01)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(3),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(3),
            chi2n_par = cms.double(0.7),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(0.35, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('pixelPairStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(0.4, 4.0),
            d0_par1 = cms.vdouble(0.3, 4.0),
            preFilterName = cms.string('pixelPairStepTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.pixelPairStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("pixelPairStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('pixelPairStepTrajectoryBuilder')
)


process.pixelPairStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("pixelPairStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.regionalCosmicCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("regionalCosmicTrackerSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilderP5')
)


process.regionalCosmicTrackerSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        MaxNumberOfPixelClusters = cms.uint32(10000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(10000),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        doClusterCheck = cms.bool(False)
    ),
    RegionFactoryPSet = cms.PSet(
        CollectionsPSet = cms.PSet(
            recoMuonsCollection = cms.InputTag(""),
            recoTrackMuonsCollection = cms.InputTag("cosmicMuons"),
            recoL2MuonsCollection = cms.InputTag("")
        ),
        ComponentName = cms.string('CosmicRegionalSeedGenerator'),
        RegionInJetsCheckPSet = cms.PSet(
            recoCaloJetsCollection = cms.InputTag("ak5CaloJets"),
            deltaRExclusionSize = cms.double(0.3),
            jetsPtMin = cms.double(5),
            doJetsExclusionCheck = cms.bool(True)
        ),
        ToolsPSet = cms.PSet(
            regionBase = cms.string('seedOnCosmicMuon'),
            thePropagatorName = cms.string('AnalyticalPropagator')
        ),
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            deltaPhiRegion = cms.double(0.1),
            measurementTrackerName = cms.string(''),
            zVertex = cms.double(5),
            deltaEtaRegion = cms.double(0.1),
            ptMin = cms.double(1.0),
            rVertex = cms.double(5)
        )
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('CosmicSeedCreator'),
        maxseeds = cms.int32(10000),
        propagator = cms.string('PropagatorWithMaterial')
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('GenericPairGenerator'),
        LayerPSet = cms.PSet(
            TOB = cms.PSet(
                TTRHBuilder = cms.string('WithTrackAngle')
            ),
            TEC = cms.PSet(
                useRingSlector = cms.bool(False),
                TTRHBuilder = cms.string('WithTrackAngle'),
                minRing = cms.int32(6),
                maxRing = cms.int32(7)
            ),
            layerList = cms.vstring('TOB6+TOB5', 
                'TOB6+TOB4', 
                'TOB6+TOB3', 
                'TOB5+TOB4', 
                'TOB5+TOB3', 
                'TOB4+TOB3', 
                'TEC1_neg+TOB6', 
                'TEC1_neg+TOB5', 
                'TEC1_neg+TOB4', 
                'TEC1_pos+TOB6', 
                'TEC1_pos+TOB5', 
                'TEC1_pos+TOB4')
        )
    ),
    TTRHBuilder = cms.string('WithTrackAngle')
)


process.regionalCosmicTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("regionalCosmicCkfTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('FittingSmootherRKP5'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    AlgorithmName = cms.string('ctf'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.roadSearchClouds = cms.EDProducer("RoadSearchCloudMaker",
    MinimalFractionOfUsedLayersPerCloud = cms.double(0.5),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    MergingFraction = cms.double(0.8),
    MaxDetHitsInCloudPerDetId = cms.uint32(8),
    SeedProducer = cms.InputTag("roadSearchSeeds"),
    DoCloudCleaning = cms.bool(True),
    IncreaseMaxNumberOfConsecutiveMissedLayersPerCloud = cms.uint32(4),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    UseStereoRecHits = cms.bool(False),
    ZPhiRoadSize = cms.double(0.06),
    MaximalFractionOfConsecutiveMissedLayersPerCloud = cms.double(0.15),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    MaximalFractionOfMissedLayersPerCloud = cms.double(0.3),
    scalefactorRoadSeedWindow = cms.double(1.5),
    UsePixelsinRS = cms.bool(True),
    IncreaseMaxNumberOfMissedLayersPerCloud = cms.uint32(3),
    RoadsLabel = cms.string(''),
    MaxRecHitsInCloud = cms.int32(100),
    UseRphiRecHits = cms.bool(False),
    StraightLineNoBeamSpotCloud = cms.bool(False),
    RPhiRoadSize = cms.double(0.02),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    MinimumHalfRoad = cms.double(0.55)
)


process.roadSearchSeeds = cms.EDProducer("RoadSearchSeedFinder",
    OuterSeedRecHitAccessMode = cms.string('RPHI'),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    MaximalEndcapImpactParameter = cms.double(1.2),
    MergeSeedsCenterCut_C = cms.double(0.4),
    MergeSeedsCenterCut_B = cms.double(0.25),
    MergeSeedsCenterCut_A = cms.double(0.05),
    MergeSeedsDifferentHitsCut = cms.uint32(1),
    rphiStripRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    MaximalBarrelImpactParameter = cms.double(0.2),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    MaxNumberOfSeeds = cms.int32(-1),
    doClusterCheck = cms.bool(False),
    stereoStripRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    OuterSeedRecHitAccessUseStereo = cms.bool(False),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    MinimalReconstructedTransverseMomentum = cms.double(1.5),
    PhiRangeForDetIdLookupInRings = cms.double(0.5),
    Mode = cms.string('STANDARD'),
    MaxNumberOfPixelClusters = cms.uint32(300),
    AllNegativeOnly = cms.bool(False),
    RoadsLabel = cms.string(''),
    InnerSeedRecHitAccessMode = cms.string('RPHI'),
    InnerSeedRecHitAccessUseStereo = cms.bool(False),
    OuterSeedRecHitAccessUseRPhi = cms.bool(False),
    MergeSeedsRadiusCut_B = cms.double(0.25),
    MergeSeedsRadiusCut_C = cms.double(0.4),
    matchedStripRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    MergeSeedsRadiusCut_A = cms.double(0.05),
    InnerSeedRecHitAccessUseRPhi = cms.bool(False),
    AllPositiveOnly = cms.bool(False)
)


process.rsTrackCandidates = cms.EDProducer("RoadSearchTrackCandidateMaker",
    NumHitCut = cms.int32(5),
    InitialVertexErrorXY = cms.double(0.2),
    HitChi2Cut = cms.double(30.0),
    StraightLineNoBeamSpotCloud = cms.bool(False),
    nFoundMin = cms.int32(4),
    MinimumChunkLength = cms.int32(7),
    TTRHBuilder = cms.string('WithTrackAngle'),
    CosmicTrackMerging = cms.bool(False),
    MeasurementTrackerName = cms.string(''),
    CloudProducer = cms.InputTag("roadSearchClouds"),
    CosmicSeedPt = cms.double(5.0),
    SplitMatchedHits = cms.bool(False)
)


process.rsWithMaterialTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("rsTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('RKFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('rs'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.secondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(-0.01),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(-0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(-99999.9),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(-3.0),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(-2.5),
        distSig3dMin = cms.double(-99999.9)
    ),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSort = cms.string('sip3dSig')
)


process.secondaryVertexTagInfosAOD = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    ),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfosAOD"),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip3dSig')
)


process.simpleSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighEffBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.simpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighPurBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3Trk'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAOD"))
)


process.simpleSecondaryVertexNegativeBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.softElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softElectron'),
    tagInfos = cms.VInputTag(cms.InputTag("softElectronTagInfos"))
)


process.softElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softElectronTagInfos"))
)


process.softElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softElectronTagInfos"))
)


process.softElectronCands = cms.EDProducer("SoftElectronCandProducer",
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.017),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.39),
    BarrelMVACuts = cms.vdouble(-0.1, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0),
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.006),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(-0.24, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 7.01),
    electrons = cms.InputTag("gsfElectrons")
)


process.softElectronSelector = cms.EDProducer("BtagGsfElectronSelector",
    input = cms.InputTag("gsfElectrons"),
    selection = cms.InputTag("eidLoose"),
    cut = cms.double(0.5)
)


process.softElectronTagInfos = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(0),
    leptons = cms.InputTag("gsfElectrons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag("softElectronCands"),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak5CaloJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(10.0)
)


process.softMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuon'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAOD"))
)


process.softMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonByIP3dBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByIP3d'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAOD"))
)


process.softMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonByPtBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softLeptonByPt'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfosAOD"))
)


process.softMuonNoIPBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softMuonNoIP'),
    tagInfos = cms.VInputTag(cms.InputTag("softMuonTagInfos"))
)


process.softMuonTagInfos = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak5CaloJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.softMuonTagInfosAOD = cms.EDProducer("SoftLepton",
    muonSelection = cms.uint32(1),
    leptons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    leptonCands = cms.InputTag(""),
    leptonId = cms.InputTag(""),
    refineJetAxis = cms.uint32(0),
    jets = cms.InputTag("ak5PFJets"),
    leptonDeltaRCut = cms.double(0.4),
    leptonChi2Cut = cms.double(9999.0)
)


process.tauGenJetMatch = cms.EDProducer("GenJetMatcher",
    src = cms.InputTag("shrinkingConePFTauProducer"),
    maxDPtRel = cms.double(3.0),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(0.1),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("tauGenJetsSelectorAllHadrons")
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    includeNeutrinos = cms.bool(False),
    GenParticles = cms.InputTag("genParticles"),
    verbose = cms.untracked.bool(False)
)


process.tauIsoDepositPFCandidates = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("shrinkingConePFTauProducer"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(10000.0),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(10000.0),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("shrinkingConePFTauProducer"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauIsoDepositPFChargedHadrons = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("shrinkingConePFTauProducer"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(0.2),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("shrinkingConePFTauProducer"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("pfAllChargedHadrons"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauIsoDepositPFGammas = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("shrinkingConePFTauProducer"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(10000.0),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(10000.0),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("shrinkingConePFTauProducer"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("pfAllPhotons"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauIsoDepositPFNeutralHadrons = cms.EDProducer("CandIsoDepositProducer",
    src = cms.InputTag("shrinkingConePFTauProducer"),
    MultipleDepositsFlag = cms.bool(False),
    trackType = cms.string('candidate'),
    ExtractorPSet = cms.PSet(
        Diff_z = cms.double(10000.0),
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        Diff_r = cms.double(10000.0),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("shrinkingConePFTauProducer"),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        candidateSource = cms.InputTag("pfAllNeutralHadrons"),
        dRmatchPFTau = cms.double(0.1)
    )
)


process.tauMatch = cms.EDProducer("MCMatcher",
    src = cms.InputTag("shrinkingConePFTauProducer"),
    maxDPtRel = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = cms.double(999.9),
    checkCharge = cms.bool(True),
    resolveAmbiguities = cms.bool(True),
    matched = cms.InputTag("genParticles")
)


process.tobTecStepClusters = cms.EDProducer("TrackClusterRemover",
    trajectories = cms.InputTag("pixelLessStepTracks"),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    overrideTrkQuals = cms.InputTag("pixelLessStepSelector","pixelLessStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    TrackQuality = cms.string('highPurity'),
    clusterLessSolution = cms.bool(True)
)


process.tobTecStepSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32(100000),
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.string('tobTecStepSeedLayers')
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    ClusterCheckPSet = cms.PSet(
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(150000),
        doClusterCheck = cms.bool(True),
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfPixelClusters = cms.uint32(20000)
    ),
    RegionFactoryPSet = cms.PSet(
        RegionPSet = cms.PSet(
            precise = cms.bool(True),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originRadius = cms.double(6.0),
            ptMin = cms.double(0.6),
            originHalfLength = cms.double(30.0)
        ),
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    )
)


process.tobTecStepSelector = cms.EDProducer("MultiTrackSelector",
    src = cms.InputTag("tobTecStepTracks"),
    trackSelectors = cms.VPSet(cms.PSet(
        max_d0 = cms.double(100.0),
        minNumber3DLayers = cms.uint32(2),
        applyAbsCutsIfNoPV = cms.bool(False),
        qualityBit = cms.string('loose'),
        minNumberLayers = cms.uint32(5),
        chi2n_par = cms.double(0.4),
        nSigmaZ = cms.double(4.0),
        dz_par2 = cms.vdouble(1.8, 4.0),
        applyAdaptedPVCuts = cms.bool(True),
        dz_par1 = cms.vdouble(1.8, 4.0),
        copyTrajectories = cms.untracked.bool(False),
        vtxNumber = cms.int32(-1),
        keepAllTracks = cms.bool(False),
        maxNumberLostLayers = cms.uint32(1),
        max_relpterr = cms.double(9999.0),
        copyExtras = cms.untracked.bool(True),
        vertexCut = cms.string('ndof>=2&!isFake'),
        max_z0 = cms.double(100.0),
        min_nhits = cms.uint32(0),
        name = cms.string('tobTecStepLoose'),
        chi2n_no1Dmod_par = cms.double(9999),
        res_par = cms.vdouble(0.003, 0.001),
        d0_par2 = cms.vdouble(2.0, 4.0),
        d0_par1 = cms.vdouble(2.0, 4.0),
        preFilterName = cms.string('')
    ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(2),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('tight'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.3),
            dz_par1 = cms.vdouble(1.4, 4.0),
            dz_par2 = cms.vdouble(1.4, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            nSigmaZ = cms.double(4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('tobTecStepTight'),
            chi2n_no1Dmod_par = cms.double(9999),
            preFilterName = cms.string('tobTecStepLoose'),
            d0_par2 = cms.vdouble(1.5, 4.0),
            d0_par1 = cms.vdouble(1.5, 4.0),
            res_par = cms.vdouble(0.003, 0.001)
        ), 
        cms.PSet(
            max_d0 = cms.double(100.0),
            minNumber3DLayers = cms.uint32(2),
            applyAbsCutsIfNoPV = cms.bool(False),
            qualityBit = cms.string('highPurity'),
            minNumberLayers = cms.uint32(5),
            chi2n_par = cms.double(0.2),
            nSigmaZ = cms.double(4.0),
            dz_par2 = cms.vdouble(1.3, 4.0),
            applyAdaptedPVCuts = cms.bool(True),
            dz_par1 = cms.vdouble(1.3, 4.0),
            copyTrajectories = cms.untracked.bool(False),
            vtxNumber = cms.int32(-1),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_relpterr = cms.double(9999.0),
            copyExtras = cms.untracked.bool(True),
            vertexCut = cms.string('ndof>=2&!isFake'),
            max_z0 = cms.double(100.0),
            min_nhits = cms.uint32(0),
            name = cms.string('tobTecStep'),
            chi2n_no1Dmod_par = cms.double(9999),
            res_par = cms.vdouble(0.003, 0.001),
            d0_par2 = cms.vdouble(1.4, 4.0),
            d0_par1 = cms.vdouble(1.4, 4.0),
            preFilterName = cms.string('tobTecStepTight')
        )),
    beamspot = cms.InputTag("offlineBeamSpot"),
    vertices = cms.InputTag("pixelVertices"),
    useVtxError = cms.bool(False),
    useVertices = cms.bool(True)
)


process.tobTecStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    src = cms.InputTag("tobTecStepSeeds"),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    TransientInitialStateEstimatorParameters = cms.PSet(
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        numberMeasurementsForFit = cms.int32(4),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    cleanTrajectoryAfterInOut = cms.bool(True),
    useHitsSplitting = cms.bool(True),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(100000),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryBuilder = cms.string('tobTecStepTrajectoryBuilder')
)


process.tobTecStepTracks = cms.EDProducer("TrackProducer",
    src = cms.InputTag("tobTecStepTrackCandidates"),
    clusterRemovalInfo = cms.InputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Fitter = cms.string('tobTecStepFitterSmoother'),
    useHitsSplitting = cms.bool(False),
    MeasurementTracker = cms.string(''),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    AlgorithmName = cms.string('iter6'),
    Propagator = cms.string('RungeKuttaTrackerPropagator')
)


process.trackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighEffBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2nd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.trackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighPurBJetTagsAOD = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rd'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAOD"))
)


process.trackExtrapolator = cms.EDProducer("TrackExtrapolator",
    trackQuality = cms.string('goodIterative'),
    trackSrc = cms.InputTag("generalTracks")
)


process.countPatElectrons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatElectrons"),
    minNumber = cms.uint32(0)
)


process.countPatJets = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatJets"),
    minNumber = cms.uint32(0)
)


process.countPatLeptons = cms.EDFilter("PATLeptonCountFilter",
    maxNumber = cms.uint32(999999),
    countElectrons = cms.bool(False),
    muonSource = cms.InputTag("selectedPatMuons"),
    minNumber = cms.uint32(0),
    electronSource = cms.InputTag("selectedPatElectrons"),
    tauSource = cms.InputTag("selectedPatTaus"),
    countTaus = cms.bool(False),
    countMuons = cms.bool(False)
)


process.countPatMuons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatMuons"),
    minNumber = cms.uint32(0)
)


process.countPatPhotons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatPhotons"),
    minNumber = cms.uint32(0)
)


process.countPatTaus = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    src = cms.InputTag("selectedPatTaus"),
    minNumber = cms.uint32(0)
)


process.djsignalfilteruds = cms.EDFilter("XtoFFbarFilter",
    src = cms.InputTag("genParticles"),
    idMotherY = cms.vint32(6000111),
    idMotherX = cms.vint32(6000111),
    idDaugtherX = cms.vint32(),
    idDaugtherY = cms.vint32(),
    idDaughterF = cms.vint32(1, 2, 3, 4, 5, 
        6, 11, 13, 15),
    idDaughterG = cms.vint32(1, 2, 3, 4, 5, 
        6, 11, 13, 15)
)


process.hcalNoiseSummaryExists = cms.EDFilter("DJ_HcalNoiseSummaryExists")


process.pfAllChargedHadrons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllChargedParticles = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllElectrons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(11, -11),
    src = cms.InputTag("pfNoMuon")
)


process.pfAllMuons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(-13, 13),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllNeutralHadrons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllNeutralHadronsAndPhotons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfAllPhotons = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIso")
)


process.pfPileUpAllChargedParticles = cms.EDFilter("PdgIdPFCandidateSelector",
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfPileUpIso")
)


process.selectedPatElectrons = cms.EDFilter("PATElectronSelector",
    src = cms.InputTag("patElectrons"),
    cut = cms.string('')
)


process.selectedPatJets = cms.EDFilter("PATJetSelector",
    src = cms.InputTag("patJets"),
    cut = cms.string('pt > 40 & abs(eta) < 2.0 && neutralHadronEnergyFraction < 0.9 && neutralEmEnergyFraction < 0.90 && chargedHadronEnergyFraction>0 && chargedHadronMultiplicity > 0 && chargedEmEnergyFraction < 0.99 && nConstituents > 2')
)


process.selectedPatMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuons"),
    cut = cms.string('')
)


process.selectedPatPhotons = cms.EDFilter("PATPhotonSelector",
    src = cms.InputTag("patPhotons"),
    cut = cms.string('')
)


process.selectedPatTaus = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("patTaus"),
    cut = cms.string('')
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    src = cms.InputTag("tauGenJets"),
    select = cms.vstring('oneProng0Pi0', 
        'oneProng1Pi0', 
        'oneProng2Pi0', 
        'oneProngOther', 
        'threeProng0Pi0', 
        'threeProng1Pi0', 
        'threeProngOther', 
        'rare')
)


process.cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    logName = cms.untracked.string('cleanPatCandidates|PATSummaryTables'),
    candidates = cms.VInputTag(cms.InputTag("cleanPatElectrons"), cms.InputTag("cleanPatMuons"), cms.InputTag("cleanPatTaus"), cms.InputTag("cleanPatPhotons"), cms.InputTag("cleanPatJets"))
)


process.djTree = cms.EDAnalyzer("DJTree",
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_dj*_*_*', 
        'keep *_*FilterFlag__*')
)


process.patCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    logName = cms.untracked.string('patCandidates|PATSummaryTables'),
    candidates = cms.VInputTag(cms.InputTag("patElectrons"), cms.InputTag("patMuons"), cms.InputTag("patTaus"), cms.InputTag("patPhotons"), cms.InputTag("patJets"), 
        cms.InputTag("patMETs"))
)


process.selectedPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    logName = cms.untracked.string('selectedPatCanddiates|PATSummaryTables'),
    candidates = cms.VInputTag(cms.InputTag("selectedPatElectrons"), cms.InputTag("selectedPatMuons"), cms.InputTag("selectedPatTaus"), cms.InputTag("selectedPatPhotons"), cms.InputTag("selectedPatJets"))
)


process.regionalCosmicTracksSeq = cms.Sequence(process.regionalCosmicTrackerSeeds+process.regionalCosmicCkfTrackCandidates+process.regionalCosmicTracks)


process.pfSortByTypeSequence = cms.Sequence(process.pfAllNeutralHadrons+process.pfAllChargedHadrons+process.pfAllPhotons+process.pfAllChargedParticles+process.pfPileUpAllChargedParticles+process.pfAllNeutralHadronsAndPhotons)


process.patElectronTrackIsolation = cms.Sequence(process.eleIsoDepositTk+process.eleIsoFromDepsTk)


process.recoJetId = cms.Sequence(process.ak5JetID)


process.ctfTracksCombinedSeeds = cms.Sequence(process.globalSeedsFromPairsWithVertices+process.globalSeedsFromTriplets+process.globalCombinedSeeds+process.ckfTrackCandidatesCombinedSeeds+process.ctfCombinedSeeds)


process.patPhotonTrackIsolation = cms.Sequence(process.gamIsoDepositTk+process.gamIsoFromDepsTk)


process.PixelLessStep = cms.Sequence(process.pixelLessStepClusters+process.pixelLessStepSeeds+process.pixelLessStepTrackCandidates+process.pixelLessStepTracks+process.pixelLessStepSelector)


process.patJetFlavourId = cms.Sequence(process.patJetPartons+process.patJetPartonAssociation+process.patJetFlavourAssociation)


process.patPhotonEcalIsolation = cms.Sequence(process.gamIsoDepositEcalFromHits+process.gamIsoFromDepsEcalFromHits)


process.TobTecStep = cms.Sequence(process.tobTecStepClusters+process.tobTecStepSeeds+process.tobTecStepTrackCandidates+process.tobTecStepTracks+process.tobTecStepSelector)


process.ctfTracksPixelLess = cms.Sequence(process.globalPixelLessSeeds+process.ckfTrackCandidatesPixelLess+process.ctfPixelLess)


process.btagging = cms.Sequence(process.impactParameterTagInfos+process.trackCountingHighEffBJetTags+process.trackCountingHighPurBJetTags+process.jetProbabilityBJetTags+process.jetBProbabilityBJetTags+process.secondaryVertexTagInfos+process.simpleSecondaryVertexHighEffBJetTags+process.simpleSecondaryVertexHighPurBJetTags+process.combinedSecondaryVertexBJetTags+process.combinedSecondaryVertexMVABJetTags+process.ghostTrackVertexTagInfos+process.ghostTrackBJetTags+process.softElectronCands+process.softElectronTagInfos+process.softElectronByIP3dBJetTags+process.softElectronByPtBJetTags+process.softMuonTagInfos+process.softMuonBJetTags+process.softMuonByIP3dBJetTags+process.softMuonByPtBJetTags)


process.patPFTauIsolation = cms.Sequence(process.tauIsoDepositPFCandidates+process.tauIsoDepositPFChargedHadrons+process.tauIsoDepositPFNeutralHadrons+process.tauIsoDepositPFGammas)


process.patElectronHcalIsolation = cms.Sequence(process.eleIsoDepositHcalFromTowers+process.eleIsoFromDepsHcalFromTowers)


process.makePatElectrons = cms.Sequence(process.electronMatch+process.patElectrons)


process.makePatPhotons = cms.Sequence(process.photonMatch+process.patPhotons)


process.LowPtTripletStep = cms.Sequence(process.lowPtTripletStepClusters+process.lowPtTripletStepSeeds+process.lowPtTripletStepTrackCandidates+process.lowPtTripletStepTracks+process.lowPtTripletStepSelector)


process.ctfTracksNoOverlaps = cms.Sequence(process.ckfTrackCandidatesNoOverlaps+process.ctfNoOverlaps)


process.rstracks = cms.Sequence(process.roadSearchSeeds+process.roadSearchClouds+process.rsTrackCandidates+process.rsWithMaterialTracks)


process.btaggingJetTagsAOD = cms.Sequence(process.jetBProbabilityBJetTagsAOD+process.jetProbabilityBJetTagsAOD+process.trackCountingHighPurBJetTagsAOD+process.trackCountingHighEffBJetTagsAOD+process.simpleSecondaryVertexHighEffBJetTagsAOD+process.simpleSecondaryVertexHighPurBJetTagsAOD+process.combinedSecondaryVertexBJetTagsAOD+process.combinedSecondaryVertexMVABJetTagsAOD+process.softMuonBJetTagsAOD+process.softMuonByPtBJetTagsAOD+process.softMuonByIP3dBJetTagsAOD)


process.cleanPatCandidates = cms.Sequence(process.cleanPatMuons+process.cleanPatElectrons+process.cleanPatPhotons+process.cleanPatTaus+process.cleanPatJets+process.cleanPatCandidateSummary)


process.patElectronId = cms.Sequence(process.eidRobustHighEnergy)


process.patJetCorrections = cms.Sequence(process.patJetCorrFactors)


process.MixedTripletStep = cms.Sequence(process.mixedTripletStepClusters+process.mixedTripletStepSeedsA+process.mixedTripletStepSeedsB+process.mixedTripletStepSeeds+process.mixedTripletStepTrackCandidates+process.mixedTripletStepTracks+process.mixedTripletStepSelector+process.mixedTripletStep)


process.pfNoPileUpIsoSequence = cms.Sequence(process.pfPileUpIso+process.pfNoPileUpIso)


process.ak5JTA = cms.Sequence(process.ak5JetTracksAssociatorAtVertex+process.ak5JetTracksAssociatorAtCaloFace+process.ak5JetExtender)


process.ConvStep = cms.Sequence(process.convClusters+process.photonConvTrajSeedFromSingleLeg+process.convTrackCandidates+process.convStepTracks+process.convStepSelector)


process.makePatMHTs = cms.Sequence(process.patMHTs)


process.patPhotonHcalIsolation = cms.Sequence(process.gamIsoDepositHcalFromTowers+process.gamIsoFromDepsHcalFromTowers)


process.patPhotonIsolation = cms.Sequence(process.patPhotonTrackIsolation+process.patPhotonEcalIsolation+process.patPhotonHcalIsolation)


process.MetType1Corrections = cms.Sequence(process.metJESCorIC5CaloJet+process.metJESCorKT4CaloJet+process.metJESCorKT6CaloJet+process.metJESCorAK5CaloJet+process.metJESCorAK7CaloJet+process.metJESCorSC5CaloJet+process.metJESCorSC7CaloJet)


process.eIdSequence = cms.Sequence(process.eidRobustLoose+process.eidRobustTight+process.eidRobustHighEnergy+process.eidLoose+process.eidTight)


process.DetachedTripletStep = cms.Sequence(process.detachedTripletStepClusters+process.detachedTripletStepSeeds+process.detachedTripletStepTrackCandidates+process.detachedTripletStepTracks+process.detachedTripletStepSelector+process.detachedTripletStep)


process.beamhaloTracksSeq = cms.Sequence(process.beamhaloTrackerSeeds+process.beamhaloTrackCandidates+process.beamhaloTracks)


process.patElectronEcalIsolation = cms.Sequence(process.eleIsoDepositEcalFromHits+process.eleIsoFromDepsEcalFromHitsByCrystal)


process.PixelPairStep = cms.Sequence(process.pixelPairStepClusters+process.pixelPairStepSeeds+process.pixelPairStepTrackCandidates+process.pixelPairStepTracks+process.pixelPairStepSelector)


process.selectedPatCandidates = cms.Sequence(process.selectedPatElectrons+process.selectedPatMuons+process.selectedPatTaus+process.selectedPatPhotons+process.selectedPatJets+process.selectedPatCandidateSummary)


process.countPatCandidates = cms.Sequence(process.countPatElectrons+process.countPatMuons+process.countPatTaus+process.countPatLeptons+process.countPatPhotons+process.countPatJets)


process.doAlldEdXEstimators = cms.Sequence(process.dedxTruncated40+process.dedxHarmonic2+process.dedxDiscrimASmi)


process.empty = cms.Sequence()


process.InitialStep = cms.Sequence(process.initialStepSeeds+process.initialStepTrackCandidates+process.initialStepTracks+process.initialStepSelector)


process.makePatMuons = cms.Sequence(process.muonMatch+process.patMuons)


process.doAlldEdXDiscriminators = cms.Sequence(process.dedxDiscrimProd+process.dedxDiscrimBTag+process.dedxDiscrimSmi+process.dedxDiscrimASmi)


process.patMETCorrections = cms.Sequence(process.metJESCorAK5CaloJet+process.metJESCorAK5CaloJetMuons)


process.patElectronIsolation = cms.Sequence(process.patElectronTrackIsolation+process.patElectronEcalIsolation+process.patElectronHcalIsolation)


process.patJetMETCorrections = cms.Sequence(process.patJetCorrections)


process.makePatJets = cms.Sequence(process.patJetCorrections+process.patJetCharge+process.patJetPartonMatch+process.patJetGenJetMatch+process.patJetFlavourId+process.patJets)


process.btaggingTagInfosAOD = cms.Sequence(process.impactParameterTagInfosAOD+process.secondaryVertexTagInfosAOD+process.softMuonTagInfosAOD+process.btaggingJetTagsAOD)


process.makePatMETs = cms.Sequence(process.patMETCorrections+process.patMETs)


process.iterTracking = cms.Sequence(process.InitialStep+process.LowPtTripletStep+process.PixelPairStep+process.DetachedTripletStep+process.MixedTripletStep+process.PixelLessStep+process.TobTecStep+process.generalTracks+process.ConvStep+process.conversionStepTracks)


process.patPFCandidateIsoDepositSelection = cms.Sequence(process.pfNoPileUpIsoSequence+process.pfSortByTypeSequence)


process.ckftracks = cms.Sequence(process.iterTracking+process.newCombinedSeeds+process.doAlldEdXEstimators)


process.ckftracks_wodEdX = cms.Sequence(process.iterTracking+process.newCombinedSeeds)


process.btaggingAOD = cms.Sequence(process.btaggingTagInfosAOD)


process.ckftracks_woBH = cms.Sequence(process.iterTracking+process.newCombinedSeeds+process.doAlldEdXEstimators)


process.ckftracks_plus_pixelless = cms.Sequence(process.ckftracks+process.ctfTracksPixelLess)


process.trackingGlobalReco = cms.Sequence(process.ckftracks+process.trackExtrapolator)


process.patDefaultSequence = cms.Sequence(process.kt6PFJets+process.patJetCorrFactors+process.jetTracksAssociatorAtVertex+process.btaggingAOD+process.patJetCharge+process.patJetPartonMatch+process.patJetGenJetMatch+process.patJetFlavourId+process.patJets+process.makePatMETs+process.patCandidateSummary+process.selectedPatJets+process.selectedPatCandidateSummary+process.countPatLeptons+process.countPatJets)


process.makePatTaus = cms.Sequence(process.patPFCandidateIsoDepositSelection+process.patPFTauIsolation+process.tauMatch+process.tauGenJets+process.tauGenJetsSelectorAllHadrons+process.tauGenJetMatch+process.patTaus)


process.patCandidates = cms.Sequence(process.makePatElectrons+process.makePatMuons+process.makePatTaus+process.makePatPhotons+process.makePatJets+process.makePatMETs+process.patCandidateSummary)


process.p_djPat = cms.Path(process.patDefaultSequence)


process.p_hbheFlag = cms.Path(process.hcalNoiseSummaryExists+process.HBHENoiseFilterResultProducer+process.HBHENoiseFilterResultProducerNoIso)


process.p_DJ = cms.Path(process.empty+process.djsignalfilteruds+process.djpileupsummary+process.djgenevent+process.djtriggers+process.djeventfilters+process.djevent+process.djdisplacedjets+process.djTree)


process.MessageLogger = cms.Service("MessageLogger",
    suppressInfo = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    suppressDebug = cms.untracked.vstring(),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    cerr_stats = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        output = cms.untracked.string('cerr'),
        optionalPSet = cms.untracked.bool(True)
    ),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noTimeStamps = cms.untracked.bool(False),
        FwkReport = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(100)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        threshold = cms.untracked.string('INFO'),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        FwkSummary = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    FrameworkJobReport = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring(),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    debugModules = cms.untracked.vstring(),
    infos = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport')
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(True),
    fileName = cms.string('ntupleu.root')
)


process.UpdaterService = cms.Service("UpdaterService")


process.AnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnalyticalPropagator'),
    PropagationDirection = cms.string('alongMomentum')
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    PropagationDirection = cms.string('anyDirection')
)


process.BeamHaloMPropagatorAlong = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('BeamHaloMPropagatorAlong'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(10000),
    useRungeKutta = cms.bool(True)
)


process.BeamHaloMPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('BeamHaloMPropagatorOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(10000),
    useRungeKutta = cms.bool(True)
)


process.BeamHaloPropagatorAlong = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorAlong'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorAlong')
)


process.BeamHaloPropagatorAny = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorAny'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorAny'),
    PropagationDirection = cms.string('anyDirection'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorAlong')
)


process.BeamHaloPropagatorOpposite = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorOpposite'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorOpposite')
)


process.BeamHaloSHPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorAlong'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.BeamHaloSHPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorAny'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.BeamHaloSHPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorOpposite'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string(''),
    useDDD = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string(''),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerHardcodeGeometryEP = cms.ESProducer("CaloTowerHardcodeGeometryEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorHardcodeGeometryEP = cms.ESProducer("CastorHardcodeGeometryEP")


process.Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(30.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('Chi2')
)


process.CkfTrajectoryBuilder = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('CkfTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    MeasurementTrackerName = cms.string(''),
    estimator = cms.string('Chi2'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.CkfTrajectoryBuilderBeamHalo = cms.ESProducer("CkfTrajectoryBuilderESProducer",
    propagatorAlong = cms.string('BeamHaloPropagatorAlong'),
    trajectoryFilterName = cms.string('ckfTrajectoryFilterBeamHaloMuon'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('CkfTrajectoryBuilderBH'),
    propagatorOpposite = cms.string('BeamHaloPropagatorOpposite'),
    MeasurementTrackerName = cms.string(''),
    estimator = cms.string('Chi2'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter')
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.DummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('DummyDetLayerGeometry')
)


process.EcalBarrelGeometryEP = cms.ESProducer("EcalBarrelGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryEP = cms.ESProducer("EcalEndcapGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryEP = cms.ESProducer("EcalPreshowerGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('GlobalDetLayerGeometry')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.GroupedCkfTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    maxCand = cms.int32(5),
    ComponentName = cms.string('GroupedCkfTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.HcalHardcodeGeometryEP = cms.ESProducer("HcalHardcodeGeometryEP")


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP")


process.KFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('KFFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('KFSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.KFFittingSmootherBeamHalo = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('KFFitterBH'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('KFSmootherBH'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherBH'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.KFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('RKFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('RKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.KFSwitching1DUpdatorESProducer = cms.ESProducer("KFSwitching1DUpdatorESProducer",
    ComponentName = cms.string('KFSwitching1DUpdator'),
    doEndCap = cms.bool(False)
)


process.KFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('KFFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterial'),
    minHits = cms.int32(3)
)


process.KFTrajectoryFitterBeamHalo = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('KFFitterBH'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    minHits = cms.int32(3)
)


process.KFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFTrajectorySmootherBeamHalo = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('KFSmootherBH'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.KFUpdatorESProducer = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('KFUpdator')
)


process.MRHFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('MRHFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('MRHSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('MRHFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.MRHTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('MRHFitter'),
    Estimator = cms.string('MRHChi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.MRHTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('MRHSmoother'),
    Estimator = cms.string('MRHChi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.MeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    inactivePixelDetectorLabels = cms.VInputTag(cms.InputTag("siPixelDigis")),
    PixelCPE = cms.string('PixelCPEGeneric'),
    stripLazyGetterProducer = cms.string(''),
    OnDemand = cms.bool(False),
    Regional = cms.bool(False),
    UsePixelModuleQualityDB = cms.bool(True),
    pixelClusterProducer = cms.string('siPixelClusters'),
    switchOffPixelsIfEmpty = cms.bool(True),
    inactiveStripDetectorLabels = cms.VInputTag(cms.InputTag("siStripDigis")),
    MaskBadAPVFibers = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    UseStripAPVFiberQualityDB = cms.bool(True),
    stripClusterProducer = cms.string('siStripClusters'),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    SiStripQualityLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TOB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TID = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TEC = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        ),
        TIB = cms.PSet(
            maxConsecutiveBad = cms.uint32(2),
            maxBad = cms.uint32(4)
        )
    ),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    ComponentName = cms.string(''),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    UseStripModuleQualityDB = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.OppositeAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('AnalyticalPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    label = cms.untracked.string('parametrizedField')
)


process.PixelCPEGenericESProducer = cms.ESProducer("PixelCPEGenericESProducer",
    EdgeClusterErrorX = cms.double(50.0),
    DoCosmics = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    TruncatePixelCharge = cms.bool(True),
    size_cutY = cms.double(3.0),
    size_cutX = cms.double(3.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    IrradiationBiasCorrection = cms.bool(False),
    TanLorentzAnglePerTesla = cms.double(0.106),
    inflate_errors = cms.bool(False),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_highY = cms.double(1.0),
    ClusterProbComputationFlag = cms.int32(0),
    EdgeClusterErrorY = cms.double(85.0),
    ComponentName = cms.string('PixelCPEGeneric'),
    eff_charge_cut_lowY = cms.double(0.0),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    Alpha2Order = cms.bool(True)
)


process.RK1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('RK1DFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('RK1DSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RK1DFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.RK1DTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('RK1DFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFSwitching1DUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.RK1DTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('RK1DSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFSwitching1DUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.RKFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(-1.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('RKFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('RKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.RKOutliers1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(20.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    Fitter = cms.string('RK1DFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('RK1DSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKOutliers1DFittingSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.RKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('RKFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    minHits = cms.int32(3)
)


process.RKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('RKSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    useDDD = cms.untracked.bool(True),
    compatibiltyWith11 = cms.untracked.bool(True)
)


process.RungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('RungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    ptMin = cms.double(-1.0),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('alongMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('anyDirection'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.SteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    endcapShiftInZNeg = cms.double(0.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    NoErrorPropagation = cms.bool(False),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    returnTangentPlane = cms.bool(True),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorOpposite'),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    endcapShiftInZPos = cms.double(0.0)
)


process.StripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('SimpleStripCPE')
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle')
)


process.TTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPETemplateReco'),
    ComponentName = cms.string('WithAngleAndTemplate')
)


process.TrackAssociatorByHits = cms.ESProducer("TrackAssociatorByHitsESProducer",
    Quality_SimToReco = cms.double(0.5),
    ThreeHitTracksAreSpecial = cms.bool(True),
    UseGrouped = cms.bool(True),
    associatePixel = cms.bool(True),
    ROUList = cms.vstring('TrackerHitsTIBLowTof', 
        'TrackerHitsTIBHighTof', 
        'TrackerHitsTIDLowTof', 
        'TrackerHitsTIDHighTof', 
        'TrackerHitsTOBLowTof', 
        'TrackerHitsTOBHighTof', 
        'TrackerHitsTECLowTof', 
        'TrackerHitsTECHighTof', 
        'TrackerHitsPixelBarrelLowTof', 
        'TrackerHitsPixelBarrelHighTof', 
        'TrackerHitsPixelEndcapLowTof', 
        'TrackerHitsPixelEndcapHighTof'),
    UseSplitting = cms.bool(True),
    Purity_SimToReco = cms.double(0.75),
    UsePixels = cms.bool(True),
    associateRecoTracks = cms.bool(True),
    AbsoluteNumberOfHits = cms.bool(False),
    associateStrip = cms.bool(True),
    Cut_RecoToSim = cms.double(0.75),
    SimToRecoDenominator = cms.string('sim'),
    ComponentName = cms.string('TrackAssociatorByHits')
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    fromDDD = cms.bool(True)
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
    overrideMasterSector = cms.bool(False),
    useParametrizedTrackerField = cms.bool(True),
    label = cms.untracked.string(''),
    version = cms.string('grid_1103l_090322_3_8t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('parametrizedField'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.ZdcHardcodeGeometryEP = cms.ESProducer("ZdcHardcodeGeometryEP")


process.beamHaloNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('BeamHaloNavigationSchool')
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.ckfBaseInOutTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.9),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        chargeSignificance = cms.double(-1.0),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('ckfBaseInOutTrajectoryFilter')
)


process.ckfBaseTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.9),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        chargeSignificance = cms.double(-1.0),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(5)
    ),
    ComponentName = cms.string('ckfBaseTrajectoryFilter')
)


process.ckfTrajectoryFilterBeamHaloMuon = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(3),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(2),
        chargeSignificance = cms.double(-1.0),
        nSigmaMinPt = cms.double(5.0),
        minimumNumberOfHits = cms.int32(4)
    ),
    ComponentName = cms.string('ckfTrajectoryFilterBeamHaloMuon')
)


process.combinedMVA = cms.ESProducer("CombinedMVAJetTagESProducer",
    useCategories = cms.bool(False),
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        variables = cms.bool(False),
        jetTagComputer = cms.string('jetProbability')
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            variables = cms.bool(False),
            jetTagComputer = cms.string('combinedSecondaryVertex')
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            variables = cms.bool(False),
            jetTagComputer = cms.string('softMuon')
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            variables = cms.bool(False),
            jetTagComputer = cms.string('softElectron')
        ))
)


process.combinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    useTrackWeights = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    charmCut = cms.double(1.5),
    vertexFlip = cms.bool(False),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip2dSig'),
    trackFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    useCategories = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory')
)


process.combinedSecondaryVertexMVA = cms.ESProducer("CombinedSecondaryVertexESProducer",
    useTrackWeights = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    charmCut = cms.double(1.5),
    vertexFlip = cms.bool(False),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSort = cms.string('sip2dSig'),
    trackFlip = cms.bool(False),
    calibrationRecords = cms.vstring('CombinedSVMVARecoVertex', 
        'CombinedSVMVAPseudoVertex', 
        'CombinedSVMVANoVertex'),
    useCategories = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory')
)


process.compositeTrajectoryFilterESProducer = cms.ESProducer("CompositeTrajectoryFilterESProducer",
    filterNames = cms.vstring(),
    ComponentName = cms.string('compositeTrajectoryFilter')
)


process.convCkfTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('convCkfTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('convCkfTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    clustersToSkip = cms.InputTag("convClusters"),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(3),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.convCkfTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(3),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('convCkfTrajectoryFilter')
)


process.convLayerPairs = cms.ESProducer("SeedingLayersESProducer",
    TOB5 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TOB4 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TIB1 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    TOB6 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TOB1 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    TOB3 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TID3 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(2)
    ),
    TOB2 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    ComponentName = cms.string('convLayerPairs'),
    TEC = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(7),
        minRing = cms.int32(1)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix2+BPix3', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'BPix3+TIB1', 
        'BPix3+TIB2', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TIB1+TIB2', 
        'TIB1+TIB3', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB2+TID2_pos', 
        'TIB2+TID2_neg', 
        'TIB2+TIB3', 
        'TIB2+TIB4', 
        'TIB3+TIB4', 
        'TIB3+TOB1', 
        'TIB3+TID1_pos', 
        'TIB3+TID1_neg', 
        'TIB4+TOB1', 
        'TIB4+TOB2', 
        'TOB1+TOB2', 
        'TOB1+TOB3', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TOB2+TOB3', 
        'TOB2+TOB4', 
        'TOB2+TEC1_pos', 
        'TOB2+TEC1_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC1_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC7_pos+TEC8_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg', 
        'TEC7_neg+TEC8_neg'),
    TID2 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(2)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("convClusters"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    TIB2 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    TIB4 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TID1 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters"),
        maxRing = cms.int32(2)
    ),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("convClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB3 = cms.PSet(
        skipClusters = cms.InputTag("convClusters"),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    )
)


process.convStepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(30),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('RKFitter'),
    MinNumberOfHits = cms.int32(3),
    Smoother = cms.string('convStepRKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('convStepFitterSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.convStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3),
    ComponentName = cms.string('convStepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("SkippingLayerCosmicNavigationSchoolESProducer",
    noPXB = cms.bool(False),
    noTID = cms.bool(False),
    noPXF = cms.bool(False),
    noTIB = cms.bool(False),
    ComponentName = cms.string('CosmicNavigationSchool'),
    allSelf = cms.bool(True),
    noTEC = cms.bool(False),
    noTOB = cms.bool(False),
    selfSearch = cms.bool(True)
)


process.detachedTripletStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('detachedTripletStepChi2Est')
)


process.detachedTripletStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
    ),
    ComponentName = cms.string('detachedTripletStepSeedLayers')
)


process.detachedTripletStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('detachedTripletStepTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('detachedTripletStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('detachedTripletStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.detachedTripletStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.075),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(3),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('detachedTripletStepTrajectoryFilter')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kRecovered = cms.vuint32(),
        kGood = cms.vuint32(0),
        kTime = cms.vuint32(),
        kWeird = cms.vuint32(),
        kBad = cms.vuint32(11, 12, 13, 14, 15, 
            16),
        kProblematic = cms.vuint32(1, 2, 3, 4, 5, 
            6, 7, 8, 9, 10)
    ),
    timeThresh = cms.double(2.0),
    flagMask = cms.PSet(
        kRecovered = cms.vstring('kLeadingEdgeRecovered', 
            'kTowerRecovered'),
        kGood = cms.vstring('kGood'),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring('kWeird', 
            'kDiWeird'),
        kBad = cms.vstring('kFaultyHardware', 
            'kDead', 
            'kKilled'),
        kProblematic = cms.vstring('kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated')
    )
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.ghostTrack = cms.ESProducer("GhostTrackESProducer",
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    charmCut = cms.double(1.5),
    trackSort = cms.string('sip2dSig'),
    minimumTrackWeight = cms.double(0.5),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    calibrationRecords = cms.vstring('GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'),
    useCategories = cms.bool(True),
    categoryVariableName = cms.string('vertexCategory')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    RecoveredRecHitBits = cms.vstring('TimingAddedBit', 
        'TimingSubtractedBit'),
    SeverityLevels = cms.VPSet(cms.PSet(
        RecHitFlags = cms.vstring(''),
        ChannelStatus = cms.vstring(''),
        Level = cms.int32(0)
    ), 
        cms.PSet(
            RecHitFlags = cms.vstring(''),
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HSCP_R1R2', 
                'HSCP_FracLeader', 
                'HSCP_OuterEnergy', 
                'HSCP_ExpFit', 
                'ADCSaturationBit', 
                'HBHEIsolatedNoise'),
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(5)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HBHEHpdHitMultiplicity', 
                'HBHEPulseShape', 
                'HOBit', 
                'HFDigiTime', 
                'HFInTimeWindow', 
                'ZDCBit', 
                'CalibrationBit', 
                'TimingErrorBit'),
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(8)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring('HFLongShort', 
                'HFPET', 
                'HFS8S1Ratio'),
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(11)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(''),
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(''),
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15)
        ), 
        cms.PSet(
            RecHitFlags = cms.vstring(''),
            ChannelStatus = cms.vstring('HcalCellOff', 
                'HcalCellDead'),
            Level = cms.int32(20)
        )),
    DropChannelStatusBits = cms.vstring('HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    file = cms.untracked.string(''),
    dump = cms.untracked.vstring('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    useDDD = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string('fakeForIdeal'),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(False)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.impactParameterMVAComputer = cms.ESProducer("GenericMVAJetTagESProducer",
    useCategories = cms.bool(False),
    calibrationRecord = cms.string('ImpactParameterMVA')
)


process.initialStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(9.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('initialStepChi2Est')
)


process.initialStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('initialStepTrajectoryFilter'),
    maxCand = cms.int32(3),
    ComponentName = cms.string('initialStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('initialStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.initialStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.4),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(3),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('initialStepTrajectoryFilter')
)


process.jetBProbability = cms.ESProducer("JetBProbabilityESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    trackIpSign = cms.int32(1),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    maximumDecayLength = cms.double(5.0)
)


process.jetProbability = cms.ESProducer("JetProbabilityESProducer",
    deltaR = cms.double(0.3),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    trackIpSign = cms.int32(1),
    minimumProbability = cms.double(0.005),
    maximumDecayLength = cms.double(5.0)
)


process.lowPtTripletStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(9.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('lowPtTripletStepChi2Est')
)


process.lowPtTripletStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
    ),
    ComponentName = cms.string('lowPtTripletStepSeedLayers')
)


process.lowPtTripletStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('lowPtTripletStepTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('lowPtTripletStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('lowPtTripletStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.lowPtTripletStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(3),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('lowPtTripletStepTrajectoryFilter')
)


process.mixedTripletStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('mixedTripletStepChi2Est')
)


process.mixedTripletStepPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('alongMomentum'),
    ComponentName = cms.string('mixedTripletStepPropagator'),
    Mass = cms.double(0.105),
    ptMin = cms.double(0.1),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    PropagationDirection = cms.string('oppositeToMomentum'),
    ComponentName = cms.string('mixedTripletStepPropagatorOpposite'),
    Mass = cms.double(0.105),
    ptMin = cms.double(0.1),
    MaxDPhi = cms.double(1.6),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepSeedLayersA = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix2_pos+TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC2_neg+TEC3_neg'),
    TEC = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        maxRing = cms.int32(1)
    ),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    ComponentName = cms.string('mixedTripletStepSeedLayersA')
)


process.mixedTripletStepSeedLayersB = cms.ESProducer("SeedingLayersESProducer",
    ComponentName = cms.string('mixedTripletStepSeedLayersB'),
    layerList = cms.vstring('BPix2+BPix3+TIB1', 
        'BPix2+BPix3+TIB2', 
        'BPix3+TIB1+TIB2'),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    TIB = cms.PSet(
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)


process.mixedTripletStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('mixedTripletStepPropagator'),
    trajectoryFilterName = cms.string('mixedTripletStepTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('mixedTripletStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('mixedTripletStepPropagatorOpposite'),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('mixedTripletStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.mixedTripletStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(3),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('mixedTripletStepTrajectoryFilter')
)


process.mixedlayerpairs = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix2_pos+TEC1_pos', 
        'FPix2_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC1_neg', 
        'FPix2_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'),
    TEC = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        minRing = cms.int32(1),
        maxRing = cms.int32(1)
    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    ComponentName = cms.string('MixedLayerPairs')
)


process.mixedlayertriplets = cms.ESProducer("SeedingLayersESProducer",
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix1+BPix2+TIB1', 
        'BPix1+BPix3+TIB1', 
        'BPix2+BPix3+TIB1', 
        'BPix1+FPix1_pos+TID1_pos', 
        'BPix1+FPix1_neg+TID1_neg', 
        'BPix1+FPix1_pos+TID2_pos', 
        'BPix1+FPix1_neg+TID2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix1_pos+FPix2_pos+TEC2_pos', 
        'FPix1_neg+FPix2_neg+TEC2_neg'),
    ComponentName = cms.string('MixedLayerTriplets'),
    TEC = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TID = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    includeBadChambers = cms.bool(False),
    etaBinSize = cms.double(0.125),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.myTTRHBuilderWithoutAngle4MixedPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedPairs')
)


process.myTTRHBuilderWithoutAngle4MixedTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedTriplets')
)


process.myTTRHBuilderWithoutAngle4PixelPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelPairs')
)


process.myTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelTriplets')
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool')
)


process.pixelLessLayerPairs4PixelLessTracking = cms.ESProducer("SeedingLayersESProducer",
    TIB3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched")
    ),
    TIB2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched")
    ),
    TIB1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched")
    ),
    TID1 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1)
    ),
    TID3 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1)
    ),
    TID2 = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1)
    ),
    ComponentName = cms.string('pixelLessLayerPairs4PixelLessTracking'),
    TEC = cms.PSet(
        useSimpleRphiHitsCleaner = cms.bool(False),
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        maxRing = cms.int32(2),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched")
    ),
    layerList = cms.vstring('TIB1+TIB2', 
        'TIB1+TIB3', 
        'TIB2+TIB3', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg')
)


process.pixelLessStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('pixelLessStepChi2Est')
)


process.pixelLessStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    TID = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        maxRing = cms.int32(2)
    ),
    ComponentName = cms.string('pixelLessStepSeedLayers'),
    layerList = cms.vstring('TIB1+TIB2', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC3_pos+TEC5_pos', 
        'TEC4_pos+TEC5_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC3_neg+TEC5_neg', 
        'TEC4_neg+TEC5_neg'),
    TEC = cms.PSet(
        minRing = cms.int32(1),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        maxRing = cms.int32(2)
    ),
    TIB = cms.PSet(
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    )
)


process.pixelLessStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('pixelLessStepTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('pixelLessStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(4),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('pixelLessStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.pixelLessStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(6),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('pixelLessStepTrajectoryFilter')
)


process.pixelPairStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(9.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('pixelPairStepChi2Est')
)


process.pixelPairStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("pixelPairStepClusters"),
        hitErrorRPhi = cms.double(0.0051)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        skipClusters = cms.InputTag("pixelPairStepClusters"),
        hitErrorRPhi = cms.double(0.0027)
    ),
    ComponentName = cms.string('pixelPairStepSeedLayers')
)


process.pixelPairStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('pixelPairStepTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('pixelPairStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"),
    inOutTrajectoryFilterName = cms.string('ckfBaseTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(5),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(True),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(True),
    estimator = cms.string('pixelPairStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.pixelPairStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(1),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(3),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('pixelPairStepTrajectoryFilter')
)


process.pixellayerpairs = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    layerList = cms.vstring('BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    ComponentName = cms.string('PixelLayerPairs')
)


process.pixellayertriplets = cms.ESProducer("SeedingLayersESProducer",
    FPix = cms.PSet(
        hitErrorRZ = cms.double(0.0036),
        hitErrorRPhi = cms.double(0.0051),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'),
    BPix = cms.PSet(
        hitErrorRZ = cms.double(0.006),
        hitErrorRPhi = cms.double(0.0027),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        HitProducer = cms.string('siPixelRecHits'),
        useErrorsFromParam = cms.bool(True)
    ),
    ComponentName = cms.string('PixelLayerTriplets')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.rings = cms.ESProducer("RingMakerESProducer",
    DumpDetIds = cms.untracked.bool(False),
    ComponentName = cms.string(''),
    RingAsciiFileName = cms.untracked.string('rings.dat'),
    DetIdsDumpFileName = cms.untracked.string('tracker_detids.dat'),
    WriteOutRingsToAsciiFile = cms.untracked.bool(False),
    Configuration = cms.untracked.string('FULL')
)


process.roads = cms.ESProducer("RoadMapMakerESProducer",
    GeometryStructure = cms.string('FullDetector'),
    ComponentName = cms.string(''),
    RingsLabel = cms.string(''),
    WriteOutRoadMapToAsciiFile = cms.untracked.bool(False),
    SeedingType = cms.string('FourRingSeeds'),
    RoadMapAsciiFile = cms.untracked.string('roads.dat')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    printDebug = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    APVGain = cms.VPSet(cms.PSet(
        Record = cms.string('SiStripApvGainRcd'),
        NormalizationFactor = cms.untracked.double(1.0),
        Label = cms.untracked.string('')
    ), 
        cms.PSet(
            Record = cms.string('SiStripApvGain2Rcd'),
            NormalizationFactor = cms.untracked.double(1.0),
            Label = cms.untracked.string('')
        )),
    AutomaticNormalization = cms.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        record = cms.string('SiStripLatencyRcd'),
        label = cms.untracked.string('')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('deconvolution')
    ),
    LorentzAnglePeakMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('peak')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    appendToDataLabel = cms.string(''),
    PrintDebugOutput = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        ))
)


process.simpleSecondaryVertex2Trk = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    useSignificance = cms.bool(True),
    use3d = cms.bool(True)
)


process.simpleSecondaryVertex3Trk = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    useSignificance = cms.bool(True),
    use3d = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.softElectron = cms.ESProducer("ElectronTaggerESProducer",
    ipSign = cms.string('any')
)


process.softLeptonByIP3d = cms.ESProducer("LeptonTaggerByIPESProducer",
    use3d = cms.bool(True),
    ipSign = cms.string('any')
)


process.softLeptonByPt = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softMuon = cms.ESProducer("MuonTaggerESProducer",
    ipSign = cms.string('any')
)


process.softMuonNoIP = cms.ESProducer("MuonTaggerNoIPESProducer",
    ipSign = cms.string('any')
)


process.templates = cms.ESProducer("PixelCPETemplateRecoESProducer",
    DoCosmics = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    ComponentName = cms.string('PixelCPETemplateReco'),
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    speed = cms.int32(-2),
    UseClusterSplitter = cms.bool(False)
)


process.tobTecStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    MaxChi2 = cms.double(16.0),
    nSigma = cms.double(3.0),
    ComponentName = cms.string('tobTecStepChi2Est')
)


process.tobTecStepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    EstimateCut = cms.double(30),
    LogPixelProbabilityCut = cms.double(-14.0),
    Fitter = cms.string('tobTecStepRKFitter'),
    MinNumberOfHits = cms.int32(8),
    Smoother = cms.string('tobTecStepRKSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('tobTecStepFitterSmoother'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)


process.tobTecStepInOutTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(4),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('tobTecStepInOutTrajectoryFilter')
)


process.tobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ComponentName = cms.string('tobTecStepRKFitter'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    minHits = cms.int32(8)
)


process.tobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(8),
    ComponentName = cms.string('tobTecStepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Updator = cms.string('KFUpdator'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry')
)


process.tobTecStepSeedLayers = cms.ESProducer("SeedingLayersESProducer",
    TOB = cms.PSet(
        skipClusters = cms.InputTag("tobTecStepClusters"),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    ComponentName = cms.string('tobTecStepSeedLayers'),
    layerList = cms.vstring('TOB1+TOB2', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg'),
    TEC = cms.PSet(
        minRing = cms.int32(5),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        useRingSlector = cms.bool(True),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        maxRing = cms.int32(5)
    )
)


process.tobTecStepTrajectoryBuilder = cms.ESProducer("GroupedCkfTrajectoryBuilderESProducer",
    bestHitOnly = cms.bool(True),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    trajectoryFilterName = cms.string('tobTecStepTrajectoryFilter'),
    maxCand = cms.int32(2),
    ComponentName = cms.string('tobTecStepTrajectoryBuilder'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    clustersToSkip = cms.InputTag("tobTecStepClusters"),
    inOutTrajectoryFilterName = cms.string('tobTecStepInOutTrajectoryFilter'),
    MeasurementTrackerName = cms.string(''),
    minNrOfHitsForRebuild = cms.int32(4),
    lockHits = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    foundHitBonus = cms.double(5.0),
    updator = cms.string('KFUpdator'),
    alwaysUseInvalidHits = cms.bool(False),
    requireSeedHitsInRebuild = cms.bool(True),
    useSameTrajFilter = cms.bool(False),
    estimator = cms.string('tobTecStepChi2Est'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0)
)


process.tobTecStepTrajectoryFilter = cms.ESProducer("TrajectoryFilterESProducer",
    filterPset = cms.PSet(
        minPt = cms.double(0.1),
        minHitsMinPt = cms.int32(3),
        ComponentType = cms.string('CkfBaseTrajectoryFilter'),
        maxLostHits = cms.int32(0),
        maxNumberOfHits = cms.int32(100),
        maxConsecLostHits = cms.int32(1),
        minimumNumberOfHits = cms.int32(6),
        nSigmaMinPt = cms.double(5.0),
        chargeSignificance = cms.double(-1.0)
    ),
    ComponentName = cms.string('tobTecStepTrajectoryFilter')
)


process.trackCounting3D2nd = cms.ESProducer("TrackCountingESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(2)
)


process.trackCounting3D3rd = cms.ESProducer("TrackCountingESProducer",
    deltaR = cms.double(-1.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    impactParameterType = cms.int32(0),
    trackQualityClass = cms.string('any'),
    maximumDecayLength = cms.double(5.0),
    nthTrack = cms.int32(3)
)


process.trajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    ComponentName = cms.string('TrajectoryCleanerBySharedHits'),
    fractionShared = cms.double(0.19),
    allowSharedFirstHit = cms.bool(True)
)


process.ttrhbwor = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('Fake'),
    Matcher = cms.string('Fake'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('Fake'),
    ComponentName = cms.string('WithoutRefit')
)


process.ttrhbwr = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    Matcher = cms.string('StandardMatcher'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    PixelCPE = cms.string('PixelCPEGeneric'),
    ComponentName = cms.string('WithTrackAngle')
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord'),
    firstValid = cms.vuint32(1)
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    toGet = cms.VPSet(),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    globaltag = cms.string('START44_V9B::All')
)


process.XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/CMSCommonData/data/cmsTracker.xml', 
        'Geometry/CMSCommonData/data/caloBase.xml', 
        'Geometry/CMSCommonData/data/cmsCalo.xml', 
        'Geometry/CMSCommonData/data/muonBase.xml', 
        'Geometry/CMSCommonData/data/cmsMuon.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/CMSCommonData/data/beampipe.xml', 
        'Geometry/CMSCommonData/data/cmsBeam.xml', 
        'Geometry/CMSCommonData/data/muonMB.xml', 
        'Geometry/CMSCommonData/data/muonMagnet.xml', 
        'Geometry/TrackerCommonData/data/pixfwdMaterials.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x2.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x3.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x4.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanelBase.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanel.xml', 
        'Geometry/TrackerCommonData/data/pixfwdBlade.xml', 
        'Geometry/TrackerCommonData/data/pixfwdNipple.xml', 
        'Geometry/TrackerCommonData/data/pixfwdDisk.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCylinder.xml', 
        'Geometry/TrackerCommonData/data/pixfwd.xml', 
        'Geometry/TrackerCommonData/data/pixbarmaterial.xml', 
        'Geometry/TrackerCommonData/data/pixbarladder.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderfull.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderhalf.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer0.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer1.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer2.xml', 
        'Geometry/TrackerCommonData/data/pixbar.xml', 
        'Geometry/TrackerCommonData/data/tibtidcommonmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmodpar.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0a.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0b.xml', 
        'Geometry/TrackerCommonData/data/tibmodule2.xml', 
        'Geometry/TrackerCommonData/data/tibstringpar.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring0lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring0.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring1lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring1.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring2lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring2.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring3lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring3.xml', 
        'Geometry/TrackerCommonData/data/tiblayerpar.xml', 
        'Geometry/TrackerCommonData/data/tiblayer0.xml', 
        'Geometry/TrackerCommonData/data/tiblayer1.xml', 
        'Geometry/TrackerCommonData/data/tiblayer2.xml', 
        'Geometry/TrackerCommonData/data/tiblayer3.xml', 
        'Geometry/TrackerCommonData/data/tib.xml', 
        'Geometry/TrackerCommonData/data/tidmaterial.xml', 
        'Geometry/TrackerCommonData/data/tidmodpar.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule2.xml', 
        'Geometry/TrackerCommonData/data/tidringpar.xml', 
        'Geometry/TrackerCommonData/data/tidring0.xml', 
        'Geometry/TrackerCommonData/data/tidring0f.xml', 
        'Geometry/TrackerCommonData/data/tidring0b.xml', 
        'Geometry/TrackerCommonData/data/tidring1.xml', 
        'Geometry/TrackerCommonData/data/tidring1f.xml', 
        'Geometry/TrackerCommonData/data/tidring1b.xml', 
        'Geometry/TrackerCommonData/data/tidring2.xml', 
        'Geometry/TrackerCommonData/data/tid.xml', 
        'Geometry/TrackerCommonData/data/tidf.xml', 
        'Geometry/TrackerCommonData/data/tidb.xml', 
        'Geometry/TrackerCommonData/data/tibtidservices.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesf.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesb.xml', 
        'Geometry/TrackerCommonData/data/tobmaterial.xml', 
        'Geometry/TrackerCommonData/data/tobmodpar.xml', 
        'Geometry/TrackerCommonData/data/tobmodule0.xml', 
        'Geometry/TrackerCommonData/data/tobmodule2.xml', 
        'Geometry/TrackerCommonData/data/tobmodule4.xml', 
        'Geometry/TrackerCommonData/data/tobrodpar.xml', 
        'Geometry/TrackerCommonData/data/tobrod0c.xml', 
        'Geometry/TrackerCommonData/data/tobrod0l.xml', 
        'Geometry/TrackerCommonData/data/tobrod0h.xml', 
        'Geometry/TrackerCommonData/data/tobrod0.xml', 
        'Geometry/TrackerCommonData/data/tobrod1l.xml', 
        'Geometry/TrackerCommonData/data/tobrod1h.xml', 
        'Geometry/TrackerCommonData/data/tobrod1.xml', 
        'Geometry/TrackerCommonData/data/tobrod2c.xml', 
        'Geometry/TrackerCommonData/data/tobrod2l.xml', 
        'Geometry/TrackerCommonData/data/tobrod2h.xml', 
        'Geometry/TrackerCommonData/data/tobrod2.xml', 
        'Geometry/TrackerCommonData/data/tobrod3l.xml', 
        'Geometry/TrackerCommonData/data/tobrod3h.xml', 
        'Geometry/TrackerCommonData/data/tobrod3.xml', 
        'Geometry/TrackerCommonData/data/tobrod4c.xml', 
        'Geometry/TrackerCommonData/data/tobrod4l.xml', 
        'Geometry/TrackerCommonData/data/tobrod4h.xml', 
        'Geometry/TrackerCommonData/data/tobrod4.xml', 
        'Geometry/TrackerCommonData/data/tobrod5l.xml', 
        'Geometry/TrackerCommonData/data/tobrod5h.xml', 
        'Geometry/TrackerCommonData/data/tobrod5.xml', 
        'Geometry/TrackerCommonData/data/tob.xml', 
        'Geometry/TrackerCommonData/data/tecmaterial.xml', 
        'Geometry/TrackerCommonData/data/tecmodpar.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule2.xml', 
        'Geometry/TrackerCommonData/data/tecmodule3.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule5.xml', 
        'Geometry/TrackerCommonData/data/tecmodule6.xml', 
        'Geometry/TrackerCommonData/data/tecpetpar.xml', 
        'Geometry/TrackerCommonData/data/tecring0.xml', 
        'Geometry/TrackerCommonData/data/tecring1.xml', 
        'Geometry/TrackerCommonData/data/tecring2.xml', 
        'Geometry/TrackerCommonData/data/tecring3.xml', 
        'Geometry/TrackerCommonData/data/tecring4.xml', 
        'Geometry/TrackerCommonData/data/tecring5.xml', 
        'Geometry/TrackerCommonData/data/tecring6.xml', 
        'Geometry/TrackerCommonData/data/tecring0f.xml', 
        'Geometry/TrackerCommonData/data/tecring1f.xml', 
        'Geometry/TrackerCommonData/data/tecring2f.xml', 
        'Geometry/TrackerCommonData/data/tecring3f.xml', 
        'Geometry/TrackerCommonData/data/tecring4f.xml', 
        'Geometry/TrackerCommonData/data/tecring5f.xml', 
        'Geometry/TrackerCommonData/data/tecring6f.xml', 
        'Geometry/TrackerCommonData/data/tecring0b.xml', 
        'Geometry/TrackerCommonData/data/tecring1b.xml', 
        'Geometry/TrackerCommonData/data/tecring2b.xml', 
        'Geometry/TrackerCommonData/data/tecring3b.xml', 
        'Geometry/TrackerCommonData/data/tecring4b.xml', 
        'Geometry/TrackerCommonData/data/tecring5b.xml', 
        'Geometry/TrackerCommonData/data/tecring6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetalf.xml', 
        'Geometry/TrackerCommonData/data/tecpetalb.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8b.xml', 
        'Geometry/TrackerCommonData/data/tecwheel.xml', 
        'Geometry/TrackerCommonData/data/tecwheela.xml', 
        'Geometry/TrackerCommonData/data/tecwheelb.xml', 
        'Geometry/TrackerCommonData/data/tecwheelc.xml', 
        'Geometry/TrackerCommonData/data/tecwheeld.xml', 
        'Geometry/TrackerCommonData/data/tecwheel6.xml', 
        'Geometry/TrackerCommonData/data/tecservices.xml', 
        'Geometry/TrackerCommonData/data/tecbackplate.xml', 
        'Geometry/TrackerCommonData/data/tec.xml', 
        'Geometry/TrackerCommonData/data/trackermaterial.xml', 
        'Geometry/TrackerCommonData/data/tracker.xml', 
        'Geometry/TrackerCommonData/data/trackerpixbar.xml', 
        'Geometry/TrackerCommonData/data/trackerpixfwd.xml', 
        'Geometry/TrackerCommonData/data/trackertibtidservices.xml', 
        'Geometry/TrackerCommonData/data/trackertib.xml', 
        'Geometry/TrackerCommonData/data/trackertid.xml', 
        'Geometry/TrackerCommonData/data/trackertob.xml', 
        'Geometry/TrackerCommonData/data/trackertec.xml', 
        'Geometry/TrackerCommonData/data/trackerbulkhead.xml', 
        'Geometry/TrackerCommonData/data/trackerother.xml', 
        'Geometry/EcalCommonData/data/eregalgo.xml', 
        'Geometry/EcalCommonData/data/ebalgo.xml', 
        'Geometry/EcalCommonData/data/ebcon.xml', 
        'Geometry/EcalCommonData/data/ebrot.xml', 
        'Geometry/EcalCommonData/data/eecon.xml', 
        'Geometry/EcalCommonData/data/eefixed.xml', 
        'Geometry/EcalCommonData/data/eehier.xml', 
        'Geometry/EcalCommonData/data/eealgo.xml', 
        'Geometry/EcalCommonData/data/escon.xml', 
        'Geometry/EcalCommonData/data/esalgo.xml', 
        'Geometry/EcalCommonData/data/eeF.xml', 
        'Geometry/EcalCommonData/data/eeB.xml', 
        'Geometry/HcalCommonData/data/hcalrotations.xml', 
        'Geometry/HcalCommonData/data/hcalalgo.xml', 
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml', 
        'Geometry/HcalCommonData/data/hcalendcapalgo.xml', 
        'Geometry/HcalCommonData/data/hcalouteralgo.xml', 
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml', 
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml', 
        'Geometry/MuonCommonData/data/mbCommon.xml', 
        'Geometry/MuonCommonData/data/mb1.xml', 
        'Geometry/MuonCommonData/data/mb2.xml', 
        'Geometry/MuonCommonData/data/mb3.xml', 
        'Geometry/MuonCommonData/data/mb4.xml', 
        'Geometry/MuonCommonData/data/muonYoke.xml', 
        'Geometry/MuonCommonData/data/mf.xml', 
        'Geometry/ForwardCommonData/data/forward.xml', 
        'Geometry/ForwardCommonData/data/bundle/forwardshield.xml', 
        'Geometry/ForwardCommonData/data/brmrotations.xml', 
        'Geometry/ForwardCommonData/data/brm.xml', 
        'Geometry/ForwardCommonData/data/totemMaterials.xml', 
        'Geometry/ForwardCommonData/data/totemRotations.xml', 
        'Geometry/ForwardCommonData/data/totemt1.xml', 
        'Geometry/ForwardCommonData/data/totemt2.xml', 
        'Geometry/ForwardCommonData/data/ionpump.xml', 
        'Geometry/MuonCommonData/data/muonNumbering.xml', 
        'Geometry/TrackerCommonData/data/trackerStructureTopology.xml', 
        'Geometry/TrackerSimData/data/trackersens.xml', 
        'Geometry/TrackerRecoData/data/trackerRecoMaterial.xml', 
        'Geometry/EcalSimData/data/ecalsens.xml', 
        'Geometry/HcalCommonData/data/hcalsenspmf.xml', 
        'Geometry/HcalSimData/data/hf.xml', 
        'Geometry/HcalSimData/data/hfpmt.xml', 
        'Geometry/HcalSimData/data/hffibrebundle.xml', 
        'Geometry/HcalSimData/data/CaloUtil.xml', 
        'Geometry/MuonSimData/data/muonSens.xml', 
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml', 
        'Geometry/RPCGeometryBuilder/data/RPCSpecs.xml', 
        'Geometry/ForwardCommonData/data/brmsens.xml', 
        'Geometry/HcalSimData/data/HcalProdCuts.xml', 
        'Geometry/EcalSimData/data/EcalProdCuts.xml', 
        'Geometry/EcalSimData/data/ESProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml', 
        'Geometry/MuonSimData/data/muonProdCuts.xml', 
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml', 
        'Geometry/CMSCommonData/data/FieldParameters.xml'),
    rootNodeName = cms.string('cms:OCMS')
)


process.ak5CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloL6SLB')
)


process.ak5CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak5CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Offset', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Offset', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ak5CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloL6SLB')
)


process.ak5CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    level = cms.string('L2Relative'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    era = cms.string('Spring10')
)


process.ak5CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    level = cms.string('L3Absolute'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    era = cms.string('Spring10')
)


process.ak5CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak5CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak5CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.ak5CaloResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    level = cms.string('L2L3Residual'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    era = cms.string('Spring10DataV2')
)


process.ak5JPTL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Fastjet', 
        'ak5JPTL1Offset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Fastjet', 
        'ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak5JPTL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Offset', 
        'ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5JPTL1Offset', 
        'ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ak5JPTL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Summer10'),
    section = cms.string(''),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2Relative')
)


process.ak5JPTL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Summer10'),
    section = cms.string(''),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L3Absolute')
)


process.ak5JPTResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2L3Residual')
)


process.ak5L1JPTOffset = cms.ESSource("L1JPTOffsetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset'),
    section = cms.string(''),
    era = cms.string('Jec10V1'),
    offsetService = cms.string('ak5CaloL1Offset')
)


process.ak5PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFL6SLB')
)


process.ak5PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak5PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ak5PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFL6SLB')
)


process.ak5PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak5PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak5PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.ak5PFResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak5TrackL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5TrackL2Relative', 
        'ak5TrackL3Absolute')
)


process.ak5TrackL2L3 = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak5TrackL2Relative', 
        'ak5TrackL3Absolute')
)


process.ak5TrackL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak5TrackL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak7CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ak7CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.ak7CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7JPTL1Fastjet', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak7JPTL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7JPTL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ak7JPTL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7L1JPTOffset = cms.ESSource("L1JPTOffsetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset'),
    section = cms.string(''),
    era = cms.string('Jec10V1'),
    offsetService = cms.string('ak5CaloL1Offset')
)


process.ak7PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ak7PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ak7PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.ak7PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.eegeom = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd'),
    firstValid = cms.vuint32(1)
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('GainWidths')
)


process.essourceEcalSev = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd'),
    firstValid = cms.vuint32(1)
)


process.essourceSev = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd'),
    firstValid = cms.vuint32(1)
)


process.ic5CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    era = cms.string('Jec10V1')
)


process.ic5CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ic5CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.ic5CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.ic5PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.ic5PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.ic5PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.kt4CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt4CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.kt4CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.kt4CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt4PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.kt4PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.kt4PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt6CaloL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.kt6CaloL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL2Relative = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10'),
    section = cms.string(''),
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    era = cms.string('')
)


process.kt6CaloResidual = cms.ESSource("LXXXCorrectionService",
    useCondDB = cms.untracked.bool(True),
    era = cms.string('Spring10DataV2'),
    section = cms.string(''),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1FastL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL1FastL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Fastjet = cms.ESSource("L1FastjetCorrectionService",
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    section = cms.string(''),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    era = cms.string('Jec10V1')
)


process.kt6PFL1L2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1L2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Offset = cms.ESSource("L1OffsetCorrectionService",
    minVtxNdof = cms.int32(4),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    section = cms.string(''),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    era = cms.string('Jec10V1')
)


process.kt6PFL2L3 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL2L3L6 = cms.ESSource("JetCorrectionServiceChain",
    useCondDB = cms.untracked.bool(True),
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL2L3Residual = cms.ESSource("JetCorrectionServiceChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL2Relative = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESSource("L6SLBCorrectionService",
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    section = cms.string(''),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    era = cms.string('')
)


process.kt6PFResidual = cms.ESSource("LXXXCorrectionService",
    section = cms.string(''),
    era = cms.string('Spring10DataV2'),
    useCondDB = cms.untracked.bool(True),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml', 
        'Geometry/CMSCommonData/data/materials.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.prefer("magfield")

process.ChargeSignificanceTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ChargeSignificanceTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0)
)

process.CkfBaseTrajectoryFilter_block = cms.PSet(
    minPt = cms.double(0.9),
    minHitsMinPt = cms.int32(3),
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    maxLostHits = cms.int32(1),
    maxNumberOfHits = cms.int32(100),
    maxConsecLostHits = cms.int32(1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    chargeSignificance = cms.double(-1.0)
)

process.CompositeTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet()
)

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    )
)

process.MaxConsecLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxConsecLostHitsTrajectoryFilter'),
    maxConsecLostHits = cms.int32(1)
)

process.MaxHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxHitsTrajectoryFilter'),
    maxNumberOfHits = cms.int32(100)
)

process.MaxLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxLostHitsTrajectoryFilter'),
    maxLostHits = cms.int32(1)
)

process.MinHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinHitsTrajectoryFilter'),
    minimumNumberOfHits = cms.int32(5)
)

process.MinPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinPtTrajectoryFilter'),
    nSigmaMinPt = cms.double(5.0),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(1.0)
)

process.PixelTripletHLTGenerator = cms.PSet(
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    maxElement = cms.uint32(100000),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    extraHitRPhitolerance = cms.double(0.032),
    useMultScattering = cms.bool(True),
    phiPreFiltering = cms.double(0.3),
    extraHitRZtolerance = cms.double(0.037),
    ComponentName = cms.string('PixelTripletHLTGenerator')
)

process.PixelTripletHLTGeneratorWithFilter = cms.PSet(
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    maxElement = cms.uint32(100000),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor')
    ),
    extraHitRPhitolerance = cms.double(0.032),
    useMultScattering = cms.bool(True),
    phiPreFiltering = cms.double(0.3),
    extraHitRZtolerance = cms.double(0.037),
    ComponentName = cms.string('PixelTripletHLTGenerator')
)

process.PixelTripletLargeTipGenerator = cms.PSet(
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    maxElement = cms.uint32(100000),
    ComponentName = cms.string('PixelTripletLargeTipGenerator'),
    extraHitRPhitolerance = cms.double(0.0),
    useMultScattering = cms.bool(True),
    phiPreFiltering = cms.double(0.3),
    extraHitRZtolerance = cms.double(0.0)
)

process.RegionPSetBlock = cms.PSet(
    RegionPSet = cms.PSet(
        precise = cms.bool(True),
        originHalfLength = cms.double(21.2),
        originZPos = cms.double(0.0),
        originYPos = cms.double(0.0),
        ptMin = cms.double(0.9),
        originXPos = cms.double(0.0),
        originRadius = cms.double(0.2)
    )
)

process.RegionPSetWithVerticesBlock = cms.PSet(
    RegionPSet = cms.PSet(
        precise = cms.bool(True),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        useFixedError = cms.bool(True),
        originRadius = cms.double(0.2),
        sigmaZVertex = cms.double(3.0),
        fixedError = cms.double(0.2),
        VertexCollection = cms.InputTag("pixelVertices"),
        ptMin = cms.double(0.9),
        useFoundVertices = cms.bool(True),
        nSigmaZ = cms.double(4.0)
    )
)

process.RegionPsetFomBeamSpotBlock = cms.PSet(
    RegionPSet = cms.PSet(
        precise = cms.bool(True),
        nSigmaZ = cms.double(4.0),
        originRadius = cms.double(0.2),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        ptMin = cms.double(0.9)
    )
)

process.TECi = cms.PSet(
    minRing = cms.int32(1),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    useRingSlector = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    maxRing = cms.int32(2)
)

process.ThresholdPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ThresholdPtTrajectoryFilter'),
    nSigmaThresholdPt = cms.double(5.0),
    minHitsThresholdPt = cms.int32(3),
    thresholdPt = cms.double(10.0)
)

process.TrackAssociatorParameterBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        dRHcal = cms.double(9999.0),
        dRPreshowerPreselection = cms.double(0.2),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        useEcal = cms.bool(True),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        dRMuon = cms.double(9999.0),
        propagateAllDirections = cms.bool(True),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        useHO = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        usePreshower = cms.bool(False),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        dRHcalPreselection = cms.double(0.2),
        useMuon = cms.bool(True),
        useCalo = cms.bool(False),
        accountForTrajectoryChangeCalo = cms.bool(False),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        dRMuonPreselection = cms.double(0.2),
        truthMatch = cms.bool(False),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        useHcal = cms.bool(True)
    )
)

process.TrackAssociatorParameters = cms.PSet(
    muonMaxDistanceSigmaX = cms.double(0.0),
    muonMaxDistanceSigmaY = cms.double(0.0),
    CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
    dRHcal = cms.double(9999.0),
    dREcal = cms.double(9999.0),
    CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
    useEcal = cms.bool(True),
    dREcalPreselection = cms.double(0.05),
    HORecHitCollectionLabel = cms.InputTag("horeco"),
    dRMuon = cms.double(9999.0),
    propagateAllDirections = cms.bool(True),
    muonMaxDistanceX = cms.double(5.0),
    muonMaxDistanceY = cms.double(5.0),
    useHO = cms.bool(True),
    trajectoryUncertaintyTolerance = cms.double(-1.0),
    usePreshower = cms.bool(False),
    DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
    EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    dRHcalPreselection = cms.double(0.2),
    useMuon = cms.bool(True),
    useCalo = cms.bool(False),
    accountForTrajectoryChangeCalo = cms.bool(False),
    EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    dRMuonPreselection = cms.double(0.2),
    truthMatch = cms.bool(False),
    HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
    useHcal = cms.bool(True)
)

process.combinedSecondaryVertexCommon = cms.PSet(
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    useTrackWeights = cms.bool(True),
    pseudoMultiplicityMin = cms.uint32(2),
    correctVertexMass = cms.bool(True),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    charmCut = cms.double(1.5),
    vertexFlip = cms.bool(False),
    minimumTrackWeight = cms.double(0.5),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackMultiplicityMin = cms.uint32(3),
    trackSort = cms.string('sip2dSig'),
    trackFlip = cms.bool(False)
)

process.fieldScaling = cms.PSet(
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991)
)

process.ghostTrackCommon = cms.PSet(
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    ),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    charmCut = cms.double(1.5),
    trackSort = cms.string('sip2dSig'),
    minimumTrackWeight = cms.double(0.5)
)

process.ghostTrackVertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        primcut = cms.double(2.0),
        seccut = cms.double(4.0),
        maxFitChi2 = cms.double(10.0),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        mergeThreshold = cms.double(3.0),
        finder = cms.string('gtvr')
    )
)

process.j2tParametersCALO = cms.PSet(
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator")
)

process.j2tParametersVX = cms.PSet(
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.5)
)

process.layerInfo = cms.PSet(
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    TEC = cms.PSet(
        useRingSlector = cms.bool(False),
        TTRHBuilder = cms.string('WithTrackAngle'),
        minRing = cms.int32(6),
        maxRing = cms.int32(7)
    )
)

process.looseSoftPFElectronCleanerBarrelCuts = cms.PSet(
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.017),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.39),
    BarrelMVACuts = cms.vdouble(-0.1, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0)
)

process.looseSoftPFElectronCleanerForwardCuts = cms.PSet(
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.006),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(-0.24, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 7.01)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

process.mediumSoftPFElectronCleanerBarrelCuts = cms.PSet(
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.0047),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.54),
    BarrelMVACuts = cms.vdouble(0.6, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0)
)

process.mediumSoftPFElectronCleanerForwardCuts = cms.PSet(
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.003),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(0.37, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 20.0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.tightSoftPFElectronCleanerBarrelCuts = cms.PSet(
    BarreldRGsfTrackElectronCuts = cms.vdouble(0.0, 0.006),
    BarrelEemPinRatioCuts = cms.vdouble(-0.9, 0.065),
    BarrelMVACuts = cms.vdouble(0.58, 1.0),
    BarrelPtCuts = cms.vdouble(2.0, 9999.0)
)

process.tightSoftPFElectronCleanerForwardCuts = cms.PSet(
    ForwarddRGsfTrackElectronCuts = cms.vdouble(0.0, 0.01),
    ForwardPtCuts = cms.vdouble(2.0, 9999.0),
    ForwardMVACuts = cms.vdouble(0.6, 1.0),
    ForwardInverseFBremCuts = cms.vdouble(1.0, 15.0)
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(0),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.07),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(5),
        ptMin = cms.double(0.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    )
)

process.vertexCutsBlock = cms.PSet(
    vertexCuts = cms.PSet(
        distSig3dMax = cms.double(99999.9),
        fracPV = cms.double(0.65),
        distVal2dMax = cms.double(2.5),
        useTrackWeights = cms.bool(True),
        maxDeltaRToJetAxis = cms.double(0.5),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        distSig2dMin = cms.double(3.0),
        multiplicityMin = cms.uint32(2),
        massMax = cms.double(6.5),
        distSig2dMax = cms.double(99999.9),
        distVal3dMax = cms.double(99999.9),
        minimumTrackWeight = cms.double(0.5),
        distVal3dMin = cms.double(-99999.9),
        distVal2dMin = cms.double(0.01),
        distSig3dMin = cms.double(-99999.9)
    )
)

process.vertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        seccut = cms.double(6.0),
        primcut = cms.double(1.8),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001),
        minweight = cms.double(0.5),
        finder = cms.string('avr')
    )
)

process.vertexSelectionBlock = cms.PSet(
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)

process.vertexTrackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        totalHitsMin = cms.uint32(8),
        jetDeltaRMax = cms.double(0.3),
        qualityClass = cms.string('highPurity'),
        pixelHitsMin = cms.uint32(2),
        sip3dSigMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        sip2dValMax = cms.double(99999.9),
        maxDecayLen = cms.double(99999.9),
        ptMin = cms.double(1.0),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        sip2dValMin = cms.double(-99999.9),
        normChi2Max = cms.double(99999.9)
    )
)

