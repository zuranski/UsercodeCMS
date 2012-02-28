# /dev/CMSSW_5_1_0/GRun/V102 (CMSSW_5_2_0_pre5_HLT9)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_5_1_0/GRun/V102')
)

streams = cms.PSet( 
  A = cms.vstring( 'BTag',
    'Commissioning',
    'Cosmics',
    'DoubleElectron',
    'DoubleMu',
    'ElectronHad',
    'FEDMonitor',
    'ForwardTriggers',
    'HT',
    'HcalHPDNoise',
    'Jet',
    'LogMonitor',
    'MET',
    'MinimumBias',
    'MuEG',
    'MuHad',
    'MuOnia',
    'MultiJet',
    'Photon',
    'PhotonHad',
    'SingleElectron',
    'SingleMu',
    'Tau',
    'TauPlusX' ),
  ALCALUMIPIXELS = cms.vstring( 'AlCaLumiPixels' ),
  ALCAP0 = cms.vstring( 'AlCaP0' ),
  ALCAPHISYM = cms.vstring( 'AlCaPhiSym' ),
  Calibration = cms.vstring( 'TestEnablesEcalHcalDT' ),
  DQM = cms.vstring( 'OnlineMonitor' ),
  EcalCalibration = cms.vstring( 'EcalLaser' ),
  ExpressForCosmics = cms.vstring( 'ExpressCosmics' ),
  ExpressForPP = cms.vstring( 'ExpressPhysics' ),
  HLTDQM = cms.vstring( 'OnlineHltMonitor' ),
  HLTDQMResults = cms.vstring( 'OnlineHltResults' ),
  HLTMON = cms.vstring( 'OfflineMonitor' ),
  NanoDST = cms.vstring( 'L1Accept' ),
  RPCMON = cms.vstring( 'RPCMonitor' ),
  TrackerCalibration = cms.vstring( 'TestEnablesTracker' )
)
datasets = cms.PSet( 
  AlCaLumiPixels = cms.vstring( 'AlCa_LumiPixels_v3' ),
  AlCaP0 = cms.vstring( 'AlCa_EcalEtaEBonly_v1',
    'AlCa_EcalEtaEEonly_v1',
    'AlCa_EcalPi0EBonly_v1',
    'AlCa_EcalPi0EEonly_v1' ),
  AlCaPhiSym = cms.vstring( 'AlCa_EcalPhiSym_v8' ),
  BTag = cms.vstring( 'HLT_BTagMu_DiJet110_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet20_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet40_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet70_L1FastJet_Mu5_v1',
    'HLT_BTagMu_Jet300_L1FastJet_Mu5_v1' ),
  Commissioning = cms.vstring( 'HLT_Activity_Ecal_SC7_v9',
    'HLT_BeamGas_HF_Beam1_v3',
    'HLT_BeamGas_HF_Beam2_v3',
    'HLT_IsoTrackHB_v10',
    'HLT_IsoTrackHE_v11',
    'HLT_L1SingleMuOpen_v5',
    'HLT_L1Tech_DT_GlobalOR_v2' ),
  Cosmics = cms.vstring( 'HLT_BeamHalo_v9',
    'HLT_L1SingleMuOpen_AntiBPTX_v4',
    'HLT_L1TrackerCosmics_v5' ),
  DoubleElectron = cms.vstring( 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v11',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v1',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v1',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v11' ),
  DoubleMu = cms.vstring( 'HLT_DoubleMu5_IsoMu5_v13',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v1',
    'HLT_L2DoubleMu23_NoVertex_v9',
    'HLT_Mu13_Mu8_v12',
    'HLT_Mu17_Mu8_v12',
    'HLT_Mu17_TkMu8_v5',
    'HLT_Mu22_TkMu22_v1',
    'HLT_Mu22_TkMu8_v1',
    'HLT_TripleMu5_v14' ),
  EcalLaser = cms.vstring( 'HLT_EcalCalibration_v2' ),
  ElectronHad = cms.vstring( 'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_BTagIPIter_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_DiCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v4',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Ele27_WP80_CentralPFJet80_v1',
    'HLT_Ele27_WP80_PFJet30_PFJet25_Deta3_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet100_PFJet25_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet150_PFJet25_v1',
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v10',
    'HLT_MET80_Track50_dEdx3p6_v1',
    'HLT_MET80_Track60_dEdx3p7_v1',
    'HLT_MET80_v1' ),
  ExpressCosmics = cms.vstring( 'HLT_L1SingleMuOpen_AntiBPTX_v4',
    'HLT_L1TrackerCosmics_v5',
    'HLT_Random_v1',
    'HLT_ZeroBias_v5' ),
  ExpressPhysics = cms.vstring( 'HLT_DoublePhoton80_v3',
    'HLT_MET200_v8',
    'HLT_MET400_v3',
    'HLT_Mu17_Mu8_v12',
    'HLT_Photon75_CaloIdVL_IsoL_v11',
    'HLT_ZeroBias_v5' ),
  FEDMonitor = cms.vstring( 'HLT_DTErrors_v2' ),
  ForwardTriggers = cms.vstring( 'HLT_L1Tech_CASTOR_HaloMuon_v2' ),
  HT = cms.vstring( 'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_HT200_AlphaT0p57_v1',
    'HLT_HT200_L1FastJet_v1',
    'HLT_HT250_AlphaT0p55_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_v1',
    'HLT_HT300_AlphaT0p53_v1',
    'HLT_HT300_AlphaT0p54_v6',
    'HLT_HT300_L1FastJet_v1',
    'HLT_HT350_AlphaT0p52_v1',
    'HLT_HT350_AlphaT0p53_v11',
    'HLT_HT350_L1FastJet_v4',
    'HLT_HT400_AlphaT0p51_v11',
    'HLT_HT400_AlphaT0p52_v6',
    'HLT_HT400_L1FastJet_v4',
    'HLT_HT450_AlphaT0p51_v6',
    'HLT_HT450_L1FastJet_v1',
    'HLT_HT500_L1FastJet_v1',
    'HLT_HT550_L1FastJet_v1',
    'HLT_HT750_v4',
    'HLT_PFHT350_PFMET100_v1',
    'HLT_PFHT350_v1',
    'HLT_PFHT400_PFMET100_v1',
    'HLT_PFHT650_DiCentralPFJet80_CenPFJet40_v1',
    'HLT_PFHT650_v2',
    'HLT_PFHT700_v1',
    'HLT_PFHT750_v1',
    'HLT_RsqMR40_Rsq0p04_v1',
    'HLT_RsqMR55_Rsq0p09_MR150_v1',
    'HLT_RsqMR60_Rsq0p09_MR150_v1' ),
  HcalHPDNoise = cms.vstring( 'HLT_GlobalRunHPDNoise_v6',
    'HLT_L1Tech_HBHEHO_totalOR_v4',
    'HLT_L1Tech_HCAL_HF_single_channel_v2' ),
  Jet = cms.vstring( 'HLT_DiJet80_DiJet60_DiJet20_L1FastJet_v1',
    'HLT_DiPFJetAve140_v1',
    'HLT_DiPFJetAve200_v1',
    'HLT_DiPFJetAve260_v1',
    'HLT_DiPFJetAve320_v1',
    'HLT_DiPFJetAve400_v1',
    'HLT_DiPFJetAve40_v1',
    'HLT_DiPFJetAve80_v1',
    'HLT_PFJet140_v1',
    'HLT_PFJet200_v1',
    'HLT_PFJet260_v1',
    'HLT_PFJet320_v1',
    'HLT_PFJet400_v1',
    'HLT_PFJet40_v1',
    'HLT_PFJet80_v1',
    'HLT_QuadJet50_L1FastJet_v1',
    'HLT_QuadJet60_DiJet20_L1FastJet_v1' ),
  L1Accept = cms.vstring( 'DST_Physics_v3' ),
  LogMonitor = cms.vstring( 'HLT_LogMonitor_v1' ),
  MET = cms.vstring( 'HLT_DiCentralPFJet50_PFMHT80_v2',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M600VBF_LEADINGJETS_v1',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M800VBF_ALLJETS_v1',
    'HLT_IsoMu15_eta2p1_L1ETM20_v1',
    'HLT_MET120_HBHENoiseCleaned_v1',
    'HLT_MET120_v8',
    'HLT_MET200_HBHENoiseCleaned_v1',
    'HLT_MET200_v8',
    'HLT_MET300_HBHENoiseCleaned_v1',
    'HLT_MET300_v1',
    'HLT_MET400_HBHENoiseCleaned_v1',
    'HLT_MET400_v3',
    'HLT_MonoCentralPFJet80L1FastJet_PFMHTWOM95_NHEF95_v1',
    'HLT_Mu15_eta2p1_L1ETM20_v1',
    'HLT_PFMHT150_v18',
    'HLT_PFMHT180_v1' ),
  MinimumBias = cms.vstring( 'HLT_JetE30_NoBPTX3BX_NoHalo_v11',
    'HLT_JetE30_NoBPTX_v9',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v6',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1',
    'HLT_Physics_v3',
    'HLT_Random_v1',
    'HLT_ZeroBias_v5' ),
  MuEG = cms.vstring( 'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdT_v5',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v9',
    'HLT_Mu22_Photon22_CaloIdL_v1',
    'HLT_Mu30_Ele30_CaloIdL_v1',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v1' ),
  MuHad = cms.vstring( 'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_L1FastJet_v1',
    'HLT_DoubleMu14_Mass8_PFMET40_v1',
    'HLT_DoubleMu14_Mass8_PFMET50_v1',
    'HLT_DoubleMu8_Mass8_PFHT175_v1',
    'HLT_DoubleMu8_Mass8_PFHT225_v1',
    'HLT_HcalCalibration_v2',
    'HLT_Iso10Mu17_eta2p1_TriCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_BTagIPIter_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_DiCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_IsoMu17_eta2p1_DiCentralPFJet30_PFHT350_PFMHT40_v1',
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_IsoMu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_L1FastJet_v1',
    'HLT_Mu12_DoubleCentralJet65_v1',
    'HLT_Mu12_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Mu12_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_Mu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Mu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_Mu40_FJHT200_v1',
    'HLT_Mu40_PFHT350_v1',
    'HLT_Mu60_PFHT350_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_PFHT350_Mu15_PFMET45_v1',
    'HLT_PFHT350_Mu15_PFMET50_v1',
    'HLT_PFHT400_Mu5_PFMET45_v1',
    'HLT_PFHT400_Mu5_PFMET50_v1' ),
  MuOnia = cms.vstring( 'HLT_Dimuon0_Jpsi_NoVertexing_v8',
    'HLT_Dimuon0_Jpsi_v11',
    'HLT_Dimuon0_PsiPrime_v1',
    'HLT_Dimuon0_Upsilon_v11',
    'HLT_Dimuon3p5_SameSign_v1',
    'HLT_Dimuon5_Jpsi_v1',
    'HLT_Dimuon5_PsiPrime_v1',
    'HLT_Dimuon5_Upsilon_v1',
    'HLT_Dimuon8_Upsilon_v1',
    'HLT_Dimuon9_Jpsi_v1',
    'HLT_Dimuon9_PsiPrime_v6',
    'HLT_DoubleMu3p5_LowMass_Displaced_v1',
    'HLT_DoubleMu4_Dimuon4_Bs_Barrel_v6',
    'HLT_DoubleMu4_Dimuon6_Bs_v6',
    'HLT_DoubleMu4_JpsiTk_Displaced_v1',
    'HLT_DoubleMu4_Jpsi_Displaced_v6',
    'HLT_Mu5_L2Mu3_Jpsi_v1',
    'HLT_Mu5_Track2_Jpsi_v14',
    'HLT_Mu5_Track3p5_Jpsi_v1',
    'HLT_Tau2Mu_RegPixTrack_v1' ),
  MultiJet = cms.vstring( 'HLT_DiJet40Eta2p6_L1FastJet_BTagIP3D_v1',
    'HLT_DiJet80Eta2p6_L1FastJet_BTagIP3DLoose_v1',
    'HLT_EightJet35_L1FastJet_v3',
    'HLT_EightJet40_L1FastJet_v3',
    'HLT_ExclDiJet80_HFAND_v1',
    'HLT_Jet160Eta2p4_Jet120Eta2p4_L1FastJet_DiBTagIP3DLoose_v1',
    'HLT_Jet60Eta1p7_Jet53Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_Jet80Eta1p7_Jet70Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_L1DoubleJet36Central_v5',
    'HLT_QuadJet70_L1FastJet_v1',
    'HLT_QuadJet80_L1FastJet_v3',
    'HLT_QuadJet90_L1FastJet_v1',
    'HLT_QuadL1FastJet_BTagIP_VBF_v1',
    'HLT_SixJet35_L1FastJet_v1',
    'HLT_SixJet45_L1FastJet_v3',
    'HLT_SixJet50_L1FastJet_v1' ),
  OfflineMonitor = ( cms.vstring( 'AlCa_EcalEtaEBonly_v1',
    'AlCa_EcalEtaEEonly_v1',
    'AlCa_EcalPhiSym_v8',
    'AlCa_EcalPi0EBonly_v1',
    'AlCa_EcalPi0EEonly_v1',
    'AlCa_LumiPixels_v3',
    'AlCa_RPCMuonNoHits_v7',
    'AlCa_RPCMuonNoTriggers_v7',
    'AlCa_RPCMuonNormalisation_v7',
    'HLT_Activity_Ecal_SC7_v9',
    'HLT_BTagMu_DiJet110_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet20_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet40_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet70_L1FastJet_Mu5_v1',
    'HLT_BTagMu_Jet300_L1FastJet_Mu5_v1',
    'HLT_BeamGas_HF_Beam1_v3',
    'HLT_BeamGas_HF_Beam2_v3',
    'HLT_BeamHalo_v9',
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_DTErrors_v2',
    'HLT_DiCentralPFJet50_PFMHT80_v2',
    'HLT_DiJet40Eta2p6_L1FastJet_BTagIP3D_v1',
    'HLT_DiJet80Eta2p6_L1FastJet_BTagIP3DLoose_v1',
    'HLT_DiJet80_DiJet60_DiJet20_L1FastJet_v1',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M600VBF_LEADINGJETS_v1',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M800VBF_ALLJETS_v1',
    'HLT_DiPFJetAve140_v1',
    'HLT_DiPFJetAve200_v1',
    'HLT_DiPFJetAve260_v1',
    'HLT_DiPFJetAve320_v1',
    'HLT_DiPFJetAve400_v1',
    'HLT_DiPFJetAve40_v1',
    'HLT_DiPFJetAve80_v1',
    'HLT_Dimuon0_Jpsi_NoVertexing_v8',
    'HLT_Dimuon0_Jpsi_v11',
    'HLT_Dimuon0_PsiPrime_v1',
    'HLT_Dimuon0_Upsilon_v11',
    'HLT_Dimuon3p5_SameSign_v1',
    'HLT_Dimuon5_Jpsi_v1',
    'HLT_Dimuon5_PsiPrime_v1',
    'HLT_Dimuon5_Upsilon_v1',
    'HLT_Dimuon8_Upsilon_v1',
    'HLT_Dimuon9_Jpsi_v1',
    'HLT_Dimuon9_PsiPrime_v6',
    'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_L1FastJet_v1',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1',
    'HLT_DoubleEle33_CaloIdL_v8',
    'HLT_DoubleEle33_CaloIdT_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_DoubleLooseIsoPFTau45_Trk5_eta2p1_v1',
    'HLT_DoubleMu14_Mass8_PFMET40_v1',
    'HLT_DoubleMu14_Mass8_PFMET50_v1',
    'HLT_DoubleMu3p5_LowMass_Displaced_v1',
    'HLT_DoubleMu4_Dimuon4_Bs_Barrel_v6',
    'HLT_DoubleMu4_Dimuon6_Bs_v6',
    'HLT_DoubleMu4_JpsiTk_Displaced_v1',
    'HLT_DoubleMu4_Jpsi_Displaced_v6',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdT_v5',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v9',
    'HLT_DoubleMu5_IsoMu5_v13',
    'HLT_DoubleMu8_Mass8_PFHT175_v1',
    'HLT_DoubleMu8_Mass8_PFHT225_v1',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v1',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v1',
    'HLT_DoublePhoton43_HEVT_v2',
    'HLT_DoublePhoton48_HEVT_v2',
    'HLT_DoublePhoton70_v2',
    'HLT_DoublePhoton80_v3',
    'HLT_EightJet35_L1FastJet_v3',
    'HLT_EightJet40_L1FastJet_v3',
    'HLT_Ele100_CaloIdVT_TrkIdT_v4',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v11',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20L1Jet_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele20_CaloIdVT_TrkIdT_LooseIsoPFTau20_v1',
    'HLT_Ele22_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_BTagIPIter_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_DiCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v4',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v1',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v1',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Ele27_WP80_CentralPFJet80_v1',
    'HLT_Ele27_WP80_PFJet30_PFJet25_Deta3_v1',
    'HLT_Ele27_WP80_PFMT50_v10',
    'HLT_Ele27_WP80_v4',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet100_PFJet25_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet150_PFJet25_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_v1',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele32_WP70_PFMT50_v10',
    'HLT_Ele32_WP70_v4',
    'HLT_Ele65_CaloIdVT_TrkIdT_v7',
    'HLT_Ele80_CaloIdVT_TrkIdT_v4',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v11',
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v10',
    'HLT_ExclDiJet80_HFAND_v1',
    'HLT_GlobalRunHPDNoise_v6',
    'HLT_HT200_AlphaT0p57_v1',
    'HLT_HT200_L1FastJet_v1',
    'HLT_HT250_AlphaT0p55_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_v1',
    'HLT_HT300_AlphaT0p53_v1',
    'HLT_HT300_AlphaT0p54_v6',
    'HLT_HT300_L1FastJet_v1',
    'HLT_HT350_AlphaT0p52_v1',
    'HLT_HT350_AlphaT0p53_v11',
    'HLT_HT350_L1FastJet_v4',
    'HLT_HT400_AlphaT0p51_v11',
    'HLT_HT400_AlphaT0p52_v6',
    'HLT_HT400_L1FastJet_v4',
    'HLT_HT450_AlphaT0p51_v6',
    'HLT_HT450_L1FastJet_v1',
    'HLT_HT500_L1FastJet_v1',
    'HLT_HT550_L1FastJet_v1',
    'HLT_HT750_v4',
    'HLT_HcalCalibration_v2',
    'HLT_Iso10Mu17_eta2p1_TriCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_BTagIPIter_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_DiCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_IsoMu15_eta2p1_L1ETM20_v1',
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_L1ETM20_v1',
    'HLT_IsoMu17_eta2p1_DiCentralPFJet30_PFHT350_PFMHT40_v1',
    'HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v1',
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v1',
    'HLT_IsoMu20_eta2p1_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_IsoMu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_IsoMu24_eta2p1_v8',
    'HLT_IsoMu30_eta2p1_v8',
    'HLT_IsoMu34_eta2p1_v6',
    'HLT_IsoMu40_eta2p1_v3',
    'HLT_IsoTrackHB_v10',
    'HLT_IsoTrackHE_v11',
    'HLT_Jet160Eta2p4_Jet120Eta2p4_L1FastJet_DiBTagIP3DLoose_v1',
    'HLT_Jet60Eta1p7_Jet53Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_Jet80Eta1p7_Jet70Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v11',
    'HLT_JetE30_NoBPTX_v9',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v6',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1',
    'HLT_L1DoubleJet36Central_v5',
    'HLT_L1SingleMu12_v1',
    'HLT_L1SingleMuOpen_AntiBPTX_v4',
    'HLT_L1SingleMuOpen_v5',
    'HLT_L1Tech_CASTOR_HaloMuon_v2',
    'HLT_L1Tech_DT_GlobalOR_v2',
    'HLT_L1Tech_HBHEHO_totalOR_v4',
    'HLT_L1Tech_HCAL_HF_single_channel_v2',
    'HLT_L1TrackerCosmics_v5',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v1',
    'HLT_L2DoubleMu23_NoVertex_v9',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_eta2p1_NoVertex_v1',
    'HLT_L2Mu30_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_L1FastJet_v1',
    'HLT_LogMonitor_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET70_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET75_v1',
    'HLT_LooseIsoPFTau35_Trk20_v1',
    'HLT_MET120_HBHENoiseCleaned_v1',
    'HLT_MET120_v8',
    'HLT_MET200_HBHENoiseCleaned_v1',
    'HLT_MET200_v8',
    'HLT_MET300_HBHENoiseCleaned_v1',
    'HLT_MET300_v1',
    'HLT_MET400_HBHENoiseCleaned_v1',
    'HLT_MET400_v3',
    'HLT_MET80_Track50_dEdx3p6_v1',
    'HLT_MET80_Track60_dEdx3p7_v1',
    'HLT_MET80_v1',
    'HLT_MonoCentralPFJet80L1FastJet_PFMHTWOM95_NHEF95_v1',
    'HLT_Mu12_DoubleCentralJet65_v1',
    'HLT_Mu12_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Mu12_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Mu12_v13',
    'HLT_Mu13_Mu8_v12',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_Mu15_eta2p1_L1ETM20_v1',
    'HLT_Mu15_eta2p1_v1',
    'HLT_Mu17_Mu8_v12',
    'HLT_Mu17_TkMu8_v5',
    'HLT_Mu17_v1',
    'HLT_Mu18_eta2p1_LooseIsoPFTau20_v1',
    'HLT_Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_Mu22_Photon22_CaloIdL_v1',
    'HLT_Mu22_TkMu22_v1',
    'HLT_Mu22_TkMu8_v1',
    'HLT_Mu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Mu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_Mu24_eta2p1_v1',
    'HLT_Mu30_Ele30_CaloIdL_v1',
    'HLT_Mu30_eta2p1_v1',
    'HLT_Mu40_FJHT200_v1',
    'HLT_Mu40_PFHT350_v1',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v1',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v1',
    'HLT_Mu40_eta2p1_v6',
    'HLT_Mu50_eta2p1_v3',
    'HLT_Mu5_L2Mu3_Jpsi_v1',
    'HLT_Mu5_Track2_Jpsi_v14',
    'HLT_Mu5_Track3p5_Jpsi_v1',
    'HLT_Mu5_v15',
    'HLT_Mu60_PFHT350_v1',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_Mu8_v13',
    'HLT_PFHT350_Mu15_PFMET45_v1',
    'HLT_PFHT350_Mu15_PFMET50_v1',
    'HLT_PFHT350_PFMET100_v1',
    'HLT_PFHT350_v1',
    'HLT_PFHT400_Mu5_PFMET45_v1',
    'HLT_PFHT400_Mu5_PFMET50_v1',
    'HLT_PFHT400_PFMET100_v1',
    'HLT_PFHT650_DiCentralPFJet80_CenPFJet40_v1',
    'HLT_PFHT650_v2',
    'HLT_PFHT700_v1',
    'HLT_PFHT750_v1',
    'HLT_PFJet140_v1',
    'HLT_PFJet200_v1',
    'HLT_PFJet260_v1')+cms.vstring( 'HLT_PFJet320_v1',
    'HLT_PFJet400_v1',
    'HLT_PFJet40_v1',
    'HLT_PFJet80_v1',
    'HLT_PFMHT150_v18',
    'HLT_PFMHT180_v1',
    'HLT_Photon135_v3',
    'HLT_Photon150_v1',
    'HLT_Photon160_v1',
    'HLT_Photon20_CaloIdVL_IsoL_v10',
    'HLT_Photon20_R9Id_Photon18_R9Id_v8',
    'HLT_Photon250_NoHE_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon26_Photon18_v8',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v1',
    'HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon300_NoHE_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v12',
    'HLT_Photon30_CaloIdVL_v9',
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v1',
    'HLT_Photon36_Photon22_v2',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v1',
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v1',
    'HLT_Photon40_CaloIdL_RsqMR35_Rsq0p09_MR150_v1',
    'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v1',
    'HLT_Photon50_CaloIdVL_IsoL_v10',
    'HLT_Photon50_CaloIdVL_v5',
    'HLT_Photon60_CaloIdL_FJHT300_v1',
    'HLT_Photon60_CaloIdL_MHT70_v4',
    'HLT_Photon70_CaloIdXL_FJHT400_v1',
    'HLT_Photon70_CaloIdXL_FJHT500_v1',
    'HLT_Photon70_CaloIdXL_MHT100_v4',
    'HLT_Photon75_CaloIdVL_IsoL_v11',
    'HLT_Photon75_CaloIdVL_v8',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet25_v6',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet30_v6',
    'HLT_Photon90_CaloIdVL_IsoL_v8',
    'HLT_Photon90_CaloIdVL_v5',
    'HLT_Physics_v3',
    'HLT_QuadJet50_L1FastJet_v1',
    'HLT_QuadJet60_DiJet20_L1FastJet_v1',
    'HLT_QuadJet70_L1FastJet_v1',
    'HLT_QuadJet80_L1FastJet_v3',
    'HLT_QuadJet90_L1FastJet_v1',
    'HLT_QuadL1FastJet_BTagIP_VBF_v1',
    'HLT_Random_v1',
    'HLT_RsqMR40_Rsq0p04_v1',
    'HLT_RsqMR55_Rsq0p09_MR150_v1',
    'HLT_RsqMR60_Rsq0p09_MR150_v1',
    'HLT_SixJet35_L1FastJet_v1',
    'HLT_SixJet45_L1FastJet_v3',
    'HLT_SixJet50_L1FastJet_v1',
    'HLT_Tau2Mu_RegPixTrack_v1',
    'HLT_TripleMu5_v14',
    'HLT_ZeroBias_v5') ),
  OnlineHltMonitor = ( cms.vstring( 'AlCa_EcalEtaEBonly_v1',
    'AlCa_EcalEtaEEonly_v1',
    'AlCa_EcalPhiSym_v8',
    'AlCa_EcalPi0EBonly_v1',
    'AlCa_EcalPi0EEonly_v1',
    'AlCa_LumiPixels_v3',
    'AlCa_RPCMuonNoHits_v7',
    'AlCa_RPCMuonNoTriggers_v7',
    'AlCa_RPCMuonNormalisation_v7',
    'HLT_Activity_Ecal_SC7_v9',
    'HLT_BTagMu_DiJet110_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet20_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet40_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet70_L1FastJet_Mu5_v1',
    'HLT_BTagMu_Jet300_L1FastJet_Mu5_v1',
    'HLT_BeamGas_HF_Beam1_v3',
    'HLT_BeamGas_HF_Beam2_v3',
    'HLT_BeamHalo_v9',
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_DTErrors_v2',
    'HLT_DiCentralPFJet50_PFMHT80_v2',
    'HLT_DiJet40Eta2p6_L1FastJet_BTagIP3D_v1',
    'HLT_DiJet80Eta2p6_L1FastJet_BTagIP3DLoose_v1',
    'HLT_DiJet80_DiJet60_DiJet20_L1FastJet_v1',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M600VBF_LEADINGJETS_v1',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M800VBF_ALLJETS_v1',
    'HLT_DiPFJetAve140_v1',
    'HLT_DiPFJetAve200_v1',
    'HLT_DiPFJetAve260_v1',
    'HLT_DiPFJetAve320_v1',
    'HLT_DiPFJetAve400_v1',
    'HLT_DiPFJetAve40_v1',
    'HLT_DiPFJetAve80_v1',
    'HLT_Dimuon0_Jpsi_NoVertexing_v8',
    'HLT_Dimuon0_Jpsi_v11',
    'HLT_Dimuon0_PsiPrime_v1',
    'HLT_Dimuon0_Upsilon_v11',
    'HLT_Dimuon3p5_SameSign_v1',
    'HLT_Dimuon5_Jpsi_v1',
    'HLT_Dimuon5_PsiPrime_v1',
    'HLT_Dimuon5_Upsilon_v1',
    'HLT_Dimuon8_Upsilon_v1',
    'HLT_Dimuon9_Jpsi_v1',
    'HLT_Dimuon9_PsiPrime_v6',
    'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_L1FastJet_v1',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1',
    'HLT_DoubleEle33_CaloIdL_v8',
    'HLT_DoubleEle33_CaloIdT_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_DoubleLooseIsoPFTau45_Trk5_eta2p1_v1',
    'HLT_DoubleMu14_Mass8_PFMET40_v1',
    'HLT_DoubleMu14_Mass8_PFMET50_v1',
    'HLT_DoubleMu3p5_LowMass_Displaced_v1',
    'HLT_DoubleMu4_Dimuon4_Bs_Barrel_v6',
    'HLT_DoubleMu4_Dimuon6_Bs_v6',
    'HLT_DoubleMu4_JpsiTk_Displaced_v1',
    'HLT_DoubleMu4_Jpsi_Displaced_v6',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdT_v5',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v9',
    'HLT_DoubleMu5_IsoMu5_v13',
    'HLT_DoubleMu8_Mass8_PFHT175_v1',
    'HLT_DoubleMu8_Mass8_PFHT225_v1',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v1',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v1',
    'HLT_DoublePhoton43_HEVT_v2',
    'HLT_DoublePhoton48_HEVT_v2',
    'HLT_DoublePhoton70_v2',
    'HLT_DoublePhoton80_v3',
    'HLT_EightJet35_L1FastJet_v3',
    'HLT_EightJet40_L1FastJet_v3',
    'HLT_Ele100_CaloIdVT_TrkIdT_v4',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v11',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20L1Jet_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele20_CaloIdVT_TrkIdT_LooseIsoPFTau20_v1',
    'HLT_Ele22_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_BTagIPIter_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_DiCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v4',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v1',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v1',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Ele27_WP80_CentralPFJet80_v1',
    'HLT_Ele27_WP80_PFJet30_PFJet25_Deta3_v1',
    'HLT_Ele27_WP80_PFMT50_v10',
    'HLT_Ele27_WP80_v4',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet100_PFJet25_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet150_PFJet25_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_v1',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele32_WP70_PFMT50_v10',
    'HLT_Ele32_WP70_v4',
    'HLT_Ele65_CaloIdVT_TrkIdT_v7',
    'HLT_Ele80_CaloIdVT_TrkIdT_v4',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v11',
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v10',
    'HLT_ExclDiJet80_HFAND_v1',
    'HLT_GlobalRunHPDNoise_v6',
    'HLT_HT200_AlphaT0p57_v1',
    'HLT_HT200_L1FastJet_v1',
    'HLT_HT250_AlphaT0p55_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_v1',
    'HLT_HT300_AlphaT0p53_v1',
    'HLT_HT300_AlphaT0p54_v6',
    'HLT_HT300_L1FastJet_v1',
    'HLT_HT350_AlphaT0p52_v1',
    'HLT_HT350_AlphaT0p53_v11',
    'HLT_HT350_L1FastJet_v4',
    'HLT_HT400_AlphaT0p51_v11',
    'HLT_HT400_AlphaT0p52_v6',
    'HLT_HT400_L1FastJet_v4',
    'HLT_HT450_AlphaT0p51_v6',
    'HLT_HT450_L1FastJet_v1',
    'HLT_HT500_L1FastJet_v1',
    'HLT_HT550_L1FastJet_v1',
    'HLT_HT750_v4',
    'HLT_Iso10Mu17_eta2p1_TriCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_BTagIPIter_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_DiCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_IsoMu15_eta2p1_L1ETM20_v1',
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_L1ETM20_v1',
    'HLT_IsoMu17_eta2p1_DiCentralPFJet30_PFHT350_PFMHT40_v1',
    'HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v1',
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v1',
    'HLT_IsoMu20_eta2p1_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_IsoMu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_IsoMu24_eta2p1_v8',
    'HLT_IsoMu30_eta2p1_v8',
    'HLT_IsoMu34_eta2p1_v6',
    'HLT_IsoMu40_eta2p1_v3',
    'HLT_IsoTrackHB_v10',
    'HLT_IsoTrackHE_v11',
    'HLT_Jet160Eta2p4_Jet120Eta2p4_L1FastJet_DiBTagIP3DLoose_v1',
    'HLT_Jet60Eta1p7_Jet53Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_Jet80Eta1p7_Jet70Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v11',
    'HLT_JetE30_NoBPTX_v9',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v6',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1',
    'HLT_L1DoubleJet36Central_v5',
    'HLT_L1SingleMu12_v1',
    'HLT_L1SingleMuOpen_AntiBPTX_v4',
    'HLT_L1SingleMuOpen_v5',
    'HLT_L1Tech_CASTOR_HaloMuon_v2',
    'HLT_L1Tech_DT_GlobalOR_v2',
    'HLT_L1Tech_HBHEHO_totalOR_v4',
    'HLT_L1Tech_HCAL_HF_single_channel_v2',
    'HLT_L1TrackerCosmics_v5',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v1',
    'HLT_L2DoubleMu23_NoVertex_v9',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_eta2p1_NoVertex_v1',
    'HLT_L2Mu30_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_L1FastJet_v1',
    'HLT_LogMonitor_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET70_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET75_v1',
    'HLT_LooseIsoPFTau35_Trk20_v1',
    'HLT_MET120_HBHENoiseCleaned_v1',
    'HLT_MET120_v8',
    'HLT_MET200_HBHENoiseCleaned_v1',
    'HLT_MET200_v8',
    'HLT_MET300_HBHENoiseCleaned_v1',
    'HLT_MET300_v1',
    'HLT_MET400_HBHENoiseCleaned_v1',
    'HLT_MET400_v3',
    'HLT_MET80_Track50_dEdx3p6_v1',
    'HLT_MET80_Track60_dEdx3p7_v1',
    'HLT_MET80_v1',
    'HLT_MonoCentralPFJet80L1FastJet_PFMHTWOM95_NHEF95_v1',
    'HLT_Mu12_DoubleCentralJet65_v1',
    'HLT_Mu12_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Mu12_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Mu12_v13',
    'HLT_Mu13_Mu8_v12',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_Mu15_eta2p1_L1ETM20_v1',
    'HLT_Mu15_eta2p1_v1',
    'HLT_Mu17_Mu8_v12',
    'HLT_Mu17_TkMu8_v5',
    'HLT_Mu17_v1',
    'HLT_Mu18_eta2p1_LooseIsoPFTau20_v1',
    'HLT_Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_Mu22_Photon22_CaloIdL_v1',
    'HLT_Mu22_TkMu22_v1',
    'HLT_Mu22_TkMu8_v1',
    'HLT_Mu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Mu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_Mu24_eta2p1_v1',
    'HLT_Mu30_Ele30_CaloIdL_v1',
    'HLT_Mu30_eta2p1_v1',
    'HLT_Mu40_FJHT200_v1',
    'HLT_Mu40_PFHT350_v1',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v1',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v1',
    'HLT_Mu40_eta2p1_v6',
    'HLT_Mu50_eta2p1_v3',
    'HLT_Mu5_L2Mu3_Jpsi_v1',
    'HLT_Mu5_Track2_Jpsi_v14',
    'HLT_Mu5_Track3p5_Jpsi_v1',
    'HLT_Mu5_v15',
    'HLT_Mu60_PFHT350_v1',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_Mu8_v13',
    'HLT_PFHT350_Mu15_PFMET45_v1',
    'HLT_PFHT350_Mu15_PFMET50_v1',
    'HLT_PFHT350_PFMET100_v1',
    'HLT_PFHT350_v1',
    'HLT_PFHT400_Mu5_PFMET45_v1',
    'HLT_PFHT400_Mu5_PFMET50_v1',
    'HLT_PFHT400_PFMET100_v1',
    'HLT_PFHT650_DiCentralPFJet80_CenPFJet40_v1',
    'HLT_PFHT650_v2',
    'HLT_PFHT700_v1',
    'HLT_PFHT750_v1',
    'HLT_PFJet140_v1',
    'HLT_PFJet200_v1',
    'HLT_PFJet260_v1',
    'HLT_PFJet320_v1')+cms.vstring( 'HLT_PFJet400_v1',
    'HLT_PFJet40_v1',
    'HLT_PFJet80_v1',
    'HLT_PFMHT150_v18',
    'HLT_PFMHT180_v1',
    'HLT_Photon135_v3',
    'HLT_Photon150_v1',
    'HLT_Photon160_v1',
    'HLT_Photon20_CaloIdVL_IsoL_v10',
    'HLT_Photon20_R9Id_Photon18_R9Id_v8',
    'HLT_Photon250_NoHE_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon26_Photon18_v8',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v1',
    'HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon300_NoHE_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v12',
    'HLT_Photon30_CaloIdVL_v9',
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v1',
    'HLT_Photon36_Photon22_v2',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v1',
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v1',
    'HLT_Photon40_CaloIdL_RsqMR35_Rsq0p09_MR150_v1',
    'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v1',
    'HLT_Photon50_CaloIdVL_IsoL_v10',
    'HLT_Photon50_CaloIdVL_v5',
    'HLT_Photon60_CaloIdL_FJHT300_v1',
    'HLT_Photon60_CaloIdL_MHT70_v4',
    'HLT_Photon70_CaloIdXL_FJHT400_v1',
    'HLT_Photon70_CaloIdXL_FJHT500_v1',
    'HLT_Photon70_CaloIdXL_MHT100_v4',
    'HLT_Photon75_CaloIdVL_IsoL_v11',
    'HLT_Photon75_CaloIdVL_v8',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet25_v6',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet30_v6',
    'HLT_Photon90_CaloIdVL_IsoL_v8',
    'HLT_Photon90_CaloIdVL_v5',
    'HLT_Physics_v3',
    'HLT_QuadJet50_L1FastJet_v1',
    'HLT_QuadJet60_DiJet20_L1FastJet_v1',
    'HLT_QuadJet70_L1FastJet_v1',
    'HLT_QuadJet80_L1FastJet_v3',
    'HLT_QuadJet90_L1FastJet_v1',
    'HLT_QuadL1FastJet_BTagIP_VBF_v1',
    'HLT_Random_v1',
    'HLT_RsqMR40_Rsq0p04_v1',
    'HLT_RsqMR55_Rsq0p09_MR150_v1',
    'HLT_RsqMR60_Rsq0p09_MR150_v1',
    'HLT_SixJet35_L1FastJet_v1',
    'HLT_SixJet45_L1FastJet_v3',
    'HLT_SixJet50_L1FastJet_v1',
    'HLT_Tau2Mu_RegPixTrack_v1',
    'HLT_TripleMu5_v14',
    'HLT_ZeroBias_v5') ),
  OnlineHltResults = cms.vstring( 'HLTriggerFinalPath' ),
  OnlineMonitor = ( cms.vstring( 'HLT_Activity_Ecal_SC7_v9',
    'HLT_BTagMu_DiJet110_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet20_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet40_L1FastJet_Mu5_v1',
    'HLT_BTagMu_DiJet70_L1FastJet_Mu5_v1',
    'HLT_BTagMu_Jet300_L1FastJet_Mu5_v1',
    'HLT_BeamGas_HF_Beam1_v3',
    'HLT_BeamGas_HF_Beam2_v3',
    'HLT_BeamHalo_v9',
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1',
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1',
    'HLT_DTCalibration_v1',
    'HLT_DTErrors_v2',
    'HLT_DiCentralPFJet50_PFMHT80_v2',
    'HLT_DiJet40Eta2p6_L1FastJet_BTagIP3D_v1',
    'HLT_DiJet80Eta2p6_L1FastJet_BTagIP3DLoose_v1',
    'HLT_DiJet80_DiJet60_DiJet20_L1FastJet_v1',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M600VBF_LEADINGJETS_v1',
    'HLT_DiPFJet40L1FastJet_PFMHTWOM65_M800VBF_ALLJETS_v1',
    'HLT_DiPFJetAve140_v1',
    'HLT_DiPFJetAve200_v1',
    'HLT_DiPFJetAve260_v1',
    'HLT_DiPFJetAve320_v1',
    'HLT_DiPFJetAve400_v1',
    'HLT_DiPFJetAve40_v1',
    'HLT_DiPFJetAve80_v1',
    'HLT_Dimuon0_Jpsi_NoVertexing_v8',
    'HLT_Dimuon0_Jpsi_v11',
    'HLT_Dimuon0_PsiPrime_v1',
    'HLT_Dimuon0_Upsilon_v11',
    'HLT_Dimuon3p5_SameSign_v1',
    'HLT_Dimuon5_Jpsi_v1',
    'HLT_Dimuon5_PsiPrime_v1',
    'HLT_Dimuon5_Upsilon_v1',
    'HLT_Dimuon8_Upsilon_v1',
    'HLT_Dimuon9_Jpsi_v1',
    'HLT_Dimuon9_PsiPrime_v6',
    'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_L1FastJet_v1',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1',
    'HLT_DoubleEle33_CaloIdL_v8',
    'HLT_DoubleEle33_CaloIdT_v4',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_DoubleLooseIsoPFTau45_Trk5_eta2p1_v1',
    'HLT_DoubleMu14_Mass8_PFMET40_v1',
    'HLT_DoubleMu14_Mass8_PFMET50_v1',
    'HLT_DoubleMu3p5_LowMass_Displaced_v1',
    'HLT_DoubleMu4_Dimuon4_Bs_Barrel_v6',
    'HLT_DoubleMu4_Dimuon6_Bs_v6',
    'HLT_DoubleMu4_JpsiTk_Displaced_v1',
    'HLT_DoubleMu4_Jpsi_Displaced_v6',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdT_v5',
    'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v9',
    'HLT_DoubleMu5_IsoMu5_v13',
    'HLT_DoubleMu8_Mass8_PFHT175_v1',
    'HLT_DoubleMu8_Mass8_PFHT225_v1',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v1',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v1',
    'HLT_DoublePhoton43_HEVT_v2',
    'HLT_DoublePhoton48_HEVT_v2',
    'HLT_DoublePhoton70_v2',
    'HLT_DoublePhoton80_v3',
    'HLT_EcalCalibration_v2',
    'HLT_EightJet35_L1FastJet_v3',
    'HLT_EightJet40_L1FastJet_v3',
    'HLT_Ele100_CaloIdVT_TrkIdT_v4',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v11',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20L1Jet_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele20_CaloIdVT_TrkIdT_LooseIsoPFTau20_v1',
    'HLT_Ele22_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_BTagIPIter_v1',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_DiCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_QuadCentralPFJet30_v4',
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v4',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v1',
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v1',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Ele27_WP80_CentralPFJet80_v1',
    'HLT_Ele27_WP80_PFJet30_PFJet25_Deta3_v1',
    'HLT_Ele27_WP80_PFMT50_v10',
    'HLT_Ele27_WP80_v4',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet100_PFJet25_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet150_PFJet25_v1',
    'HLT_Ele30_CaloIdVT_TrkIdT_v1',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele32_WP70_PFMT50_v10',
    'HLT_Ele32_WP70_v4',
    'HLT_Ele65_CaloIdVT_TrkIdT_v7',
    'HLT_Ele80_CaloIdVT_TrkIdT_v4',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v11',
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v10',
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v10',
    'HLT_ExclDiJet80_HFAND_v1',
    'HLT_GlobalRunHPDNoise_v6',
    'HLT_HT200_AlphaT0p57_v1',
    'HLT_HT200_L1FastJet_v1',
    'HLT_HT250_AlphaT0p55_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_ChgFraction10_v1',
    'HLT_HT250_L1FastJet_SingleDisplacedPFJet60_v1',
    'HLT_HT250_L1FastJet_v1',
    'HLT_HT300_AlphaT0p53_v1',
    'HLT_HT300_AlphaT0p54_v6',
    'HLT_HT300_L1FastJet_v1',
    'HLT_HT350_AlphaT0p52_v1',
    'HLT_HT350_AlphaT0p53_v11',
    'HLT_HT350_L1FastJet_v4',
    'HLT_HT400_AlphaT0p51_v11',
    'HLT_HT400_AlphaT0p52_v6',
    'HLT_HT400_L1FastJet_v4',
    'HLT_HT450_AlphaT0p51_v6',
    'HLT_HT450_L1FastJet_v1',
    'HLT_HT500_L1FastJet_v1',
    'HLT_HT550_L1FastJet_v1',
    'HLT_HT750_v4',
    'HLT_HcalCalibration_v2',
    'HLT_Iso10Mu17_eta2p1_TriCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_BTagIPIter_v1',
    'HLT_Iso10Mu20_eta2p1_CentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_DiCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Iso10Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_IsoMu15_eta2p1_L1ETM20_v1',
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_L1ETM20_v1',
    'HLT_IsoMu17_eta2p1_DiCentralPFJet30_PFHT350_PFMHT40_v1',
    'HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v1',
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v1',
    'HLT_IsoMu20_eta2p1_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_PFMHT20_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_IsoMu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_IsoMu24_eta2p1_v8',
    'HLT_IsoMu30_eta2p1_v8',
    'HLT_IsoMu34_eta2p1_v6',
    'HLT_IsoMu40_eta2p1_v3',
    'HLT_IsoTrackHB_v10',
    'HLT_IsoTrackHE_v11',
    'HLT_Jet160Eta2p4_Jet120Eta2p4_L1FastJet_DiBTagIP3DLoose_v1',
    'HLT_Jet60Eta1p7_Jet53Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_Jet80Eta1p7_Jet70Eta1p7_L1FastJet_DiBTagIP3D_v1',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v11',
    'HLT_JetE30_NoBPTX_v9',
    'HLT_JetE50_NoBPTX3BX_NoHalo_v6',
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1',
    'HLT_L1DoubleJet36Central_v5',
    'HLT_L1SingleMu12_v1',
    'HLT_L1SingleMuOpen_AntiBPTX_v4',
    'HLT_L1SingleMuOpen_v5',
    'HLT_L1Tech_CASTOR_HaloMuon_v2',
    'HLT_L1Tech_DT_GlobalOR_v2',
    'HLT_L1Tech_HBHEHO_totalOR_v4',
    'HLT_L1Tech_HCAL_HF_single_channel_v2',
    'HLT_L1TrackerCosmics_v5',
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v1',
    'HLT_L2DoubleMu23_NoVertex_v9',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_eta2p1_NoVertex_v1',
    'HLT_L2Mu30_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_L1FastJet_v1',
    'HLT_LogMonitor_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET70_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET75_v1',
    'HLT_LooseIsoPFTau35_Trk20_v1',
    'HLT_MET120_HBHENoiseCleaned_v1',
    'HLT_MET120_v8',
    'HLT_MET200_HBHENoiseCleaned_v1',
    'HLT_MET200_v8',
    'HLT_MET300_HBHENoiseCleaned_v1',
    'HLT_MET300_v1',
    'HLT_MET400_HBHENoiseCleaned_v1',
    'HLT_MET400_v3',
    'HLT_MET80_Track50_dEdx3p6_v1',
    'HLT_MET80_Track60_dEdx3p7_v1',
    'HLT_MET80_v1',
    'HLT_MonoCentralPFJet80L1FastJet_PFMHTWOM95_NHEF95_v1',
    'HLT_Mu12_DoubleCentralJet65_v1',
    'HLT_Mu12_RsqMR30_Rsq0p04_MR200_v1',
    'HLT_Mu12_RsqMR40_Rsq0p04_MR200_v1',
    'HLT_Mu12_v13',
    'HLT_Mu13_Mu8_v12',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1',
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1',
    'HLT_Mu15_eta2p1_L1ETM20_v1',
    'HLT_Mu15_eta2p1_v1',
    'HLT_Mu17_Mu8_v12',
    'HLT_Mu17_TkMu8_v5',
    'HLT_Mu17_v1',
    'HLT_Mu18_eta2p1_LooseIsoPFTau20_v1',
    'HLT_Mu20_eta2p1_QuadCentralPFJet30_v1',
    'HLT_Mu20_eta2p1_TriCentralPFJet30_v1',
    'HLT_Mu22_Photon22_CaloIdL_v1',
    'HLT_Mu22_TkMu22_v1',
    'HLT_Mu22_TkMu8_v1',
    'HLT_Mu24_eta2p1_CentralPFJet30_CentralPFJet25_v1',
    'HLT_Mu24_eta2p1_PFJet30_PFJet25_Deta3_v1',
    'HLT_Mu24_eta2p1_v1',
    'HLT_Mu30_Ele30_CaloIdL_v1',
    'HLT_Mu30_eta2p1_v1',
    'HLT_Mu40_FJHT200_v1',
    'HLT_Mu40_PFHT350_v1',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v1',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v1',
    'HLT_Mu40_eta2p1_v6',
    'HLT_Mu50_eta2p1_v3',
    'HLT_Mu5_L2Mu3_Jpsi_v1',
    'HLT_Mu5_Track2_Jpsi_v14',
    'HLT_Mu5_Track3p5_Jpsi_v1',
    'HLT_Mu5_v15',
    'HLT_Mu60_PFHT350_v1',
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1',
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1',
    'HLT_Mu8_v13',
    'HLT_PFHT350_Mu15_PFMET45_v1',
    'HLT_PFHT350_Mu15_PFMET50_v1',
    'HLT_PFHT350_PFMET100_v1',
    'HLT_PFHT350_v1',
    'HLT_PFHT400_Mu5_PFMET45_v1',
    'HLT_PFHT400_Mu5_PFMET50_v1',
    'HLT_PFHT400_PFMET100_v1',
    'HLT_PFHT650_DiCentralPFJet80_CenPFJet40_v1',
    'HLT_PFHT650_v2',
    'HLT_PFHT700_v1',
    'HLT_PFHT750_v1',
    'HLT_PFJet140_v1',
    'HLT_PFJet200_v1',
    'HLT_PFJet260_v1',
    'HLT_PFJet320_v1',
    'HLT_PFJet400_v1',
    'HLT_PFJet40_v1',
    'HLT_PFJet80_v1',
    'HLT_PFMHT150_v18',
    'HLT_PFMHT180_v1',
    'HLT_Photon135_v3')+cms.vstring( 'HLT_Photon150_v1',
    'HLT_Photon160_v1',
    'HLT_Photon20_CaloIdVL_IsoL_v10',
    'HLT_Photon20_R9Id_Photon18_R9Id_v8',
    'HLT_Photon250_NoHE_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon26_Photon18_v8',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v1',
    'HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon300_NoHE_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v12',
    'HLT_Photon30_CaloIdVL_v9',
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v1',
    'HLT_Photon36_Photon22_v2',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v1',
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v1',
    'HLT_Photon40_CaloIdL_RsqMR35_Rsq0p09_MR150_v1',
    'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v1',
    'HLT_Photon50_CaloIdVL_IsoL_v10',
    'HLT_Photon50_CaloIdVL_v5',
    'HLT_Photon60_CaloIdL_FJHT300_v1',
    'HLT_Photon60_CaloIdL_MHT70_v4',
    'HLT_Photon70_CaloIdXL_FJHT400_v1',
    'HLT_Photon70_CaloIdXL_FJHT500_v1',
    'HLT_Photon70_CaloIdXL_MHT100_v4',
    'HLT_Photon75_CaloIdVL_IsoL_v11',
    'HLT_Photon75_CaloIdVL_v8',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet25_v6',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet30_v6',
    'HLT_Photon90_CaloIdVL_IsoL_v8',
    'HLT_Photon90_CaloIdVL_v5',
    'HLT_Physics_v3',
    'HLT_QuadJet50_L1FastJet_v1',
    'HLT_QuadJet60_DiJet20_L1FastJet_v1',
    'HLT_QuadJet70_L1FastJet_v1',
    'HLT_QuadJet80_L1FastJet_v3',
    'HLT_QuadJet90_L1FastJet_v1',
    'HLT_QuadL1FastJet_BTagIP_VBF_v1',
    'HLT_Random_v1',
    'HLT_RsqMR40_Rsq0p04_v1',
    'HLT_RsqMR55_Rsq0p09_MR150_v1',
    'HLT_RsqMR60_Rsq0p09_MR150_v1',
    'HLT_SixJet35_L1FastJet_v1',
    'HLT_SixJet45_L1FastJet_v3',
    'HLT_SixJet50_L1FastJet_v1',
    'HLT_Tau2Mu_RegPixTrack_v1',
    'HLT_TrackerCalibration_v2',
    'HLT_TripleMu5_v14',
    'HLT_ZeroBias_v5') ),
  Photon = cms.vstring( 'HLT_DoubleEle33_CaloIdL_v8',
    'HLT_DoubleEle33_CaloIdT_v4',
    'HLT_DoublePhoton43_HEVT_v2',
    'HLT_DoublePhoton48_HEVT_v2',
    'HLT_DoublePhoton70_v2',
    'HLT_DoublePhoton80_v3',
    'HLT_Photon135_v3',
    'HLT_Photon150_v1',
    'HLT_Photon160_v1',
    'HLT_Photon20_CaloIdVL_IsoL_v10',
    'HLT_Photon20_R9Id_Photon18_R9Id_v8',
    'HLT_Photon250_NoHE_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_CaloId10_Iso50_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon26_Photon18_v8',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v1',
    'HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_Mass60_v1',
    'HLT_Photon26_R9Id85_Photon18_R9Id85_Mass60_v1',
    'HLT_Photon300_NoHE_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v12',
    'HLT_Photon30_CaloIdVL_v9',
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v1',
    'HLT_Photon36_Photon22_v2',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v1',
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v1',
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v1',
    'HLT_Photon50_CaloIdVL_IsoL_v10',
    'HLT_Photon50_CaloIdVL_v5',
    'HLT_Photon60_CaloIdL_FJHT300_v1',
    'HLT_Photon70_CaloIdXL_FJHT400_v1',
    'HLT_Photon70_CaloIdXL_FJHT500_v1',
    'HLT_Photon75_CaloIdVL_IsoL_v11',
    'HLT_Photon75_CaloIdVL_v8',
    'HLT_Photon90_CaloIdVL_IsoL_v8',
    'HLT_Photon90_CaloIdVL_v5' ),
  PhotonHad = cms.vstring( 'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v1',
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v1',
    'HLT_Photon40_CaloIdL_RsqMR35_Rsq0p09_MR150_v1',
    'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v1',
    'HLT_Photon60_CaloIdL_MHT70_v4',
    'HLT_Photon70_CaloIdXL_MHT100_v4',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet25_v6',
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet30_v6' ),
  RPCMonitor = cms.vstring( 'AlCa_RPCMuonNoHits_v7',
    'AlCa_RPCMuonNoTriggers_v7',
    'AlCa_RPCMuonNormalisation_v7' ),
  SingleElectron = cms.vstring( 'HLT_Ele100_CaloIdVT_TrkIdT_v4',
    'HLT_Ele22_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele27_WP80_PFMT50_v10',
    'HLT_Ele27_WP80_v4',
    'HLT_Ele30_CaloIdVT_TrkIdT_v1',
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4',
    'HLT_Ele32_WP70_PFMT50_v10',
    'HLT_Ele32_WP70_v4',
    'HLT_Ele65_CaloIdVT_TrkIdT_v7',
    'HLT_Ele80_CaloIdVT_TrkIdT_v4' ),
  SingleMu = cms.vstring( 'HLT_IsoMu20_eta2p1_v1',
    'HLT_IsoMu24_eta2p1_v8',
    'HLT_IsoMu30_eta2p1_v8',
    'HLT_IsoMu34_eta2p1_v6',
    'HLT_IsoMu40_eta2p1_v3',
    'HLT_L1SingleMu12_v1',
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_L2Mu20_eta2p1_NoVertex_v1',
    'HLT_L2Mu30_NoVertex_NoBPTX3BX_NoHalo_v1',
    'HLT_Mu12_v13',
    'HLT_Mu15_eta2p1_v1',
    'HLT_Mu17_v1',
    'HLT_Mu24_eta2p1_v1',
    'HLT_Mu30_eta2p1_v1',
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v1',
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v1',
    'HLT_Mu40_eta2p1_v6',
    'HLT_Mu50_eta2p1_v3',
    'HLT_Mu5_v15',
    'HLT_Mu8_v13' ),
  Tau = cms.vstring( 'HLT_DoubleLooseIsoPFTau45_Trk5_eta2p1_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET70_v1',
    'HLT_LooseIsoPFTau35_Trk20_MET75_v1',
    'HLT_LooseIsoPFTau35_Trk20_v1' ),
  TauPlusX = cms.vstring( 'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20L1Jet_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele20_CaloIdVT_TrkIdT_LooseIsoPFTau20_v1',
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_L1ETM20_v1',
    'HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v1',
    'HLT_Mu18_eta2p1_LooseIsoPFTau20_v1' ),
  TestEnablesEcalHcalDT = cms.vstring( 'HLT_DTCalibration_v1',
    'HLT_EcalCalibration_v2',
    'HLT_HcalCalibration_v2' ),
  TestEnablesTracker = cms.vstring( 'HLT_TrackerCalibration_v2' )
)

GlobalTag = cms.ESSource( "PoolDBESSource",
  BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
  DBParameters = cms.PSet( 
    authenticationPath = cms.untracked.string( "." ),
    connectionRetrialTimeOut = cms.untracked.int32( 60 ),
    idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
    messageLevel = cms.untracked.int32( 0 ),
    enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
    enableConnectionSharing = cms.untracked.bool( True ),
    enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
    connectionTimeOut = cms.untracked.int32( 0 ),
    connectionRetrialPeriod = cms.untracked.int32( 10 )
  ),
  toGet = cms.VPSet( 
  ),
  connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG" ),
  globaltag = cms.string( "GR_H_V26::All" )
)
HepPDTESSource = cms.ESSource( "HepPDTESSource",
  pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" )
)
eegeom = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "EcalMappingRcd" ),
  firstValid = cms.vuint32( 1 )
)
es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
  fromDDD = cms.untracked.bool( False ),
  toGet = cms.untracked.vstring( 'GainWidths' )
)
hltESSBTagRecord = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "JetTagComputerRecord" ),
  firstValid = cms.vuint32( 1 )
)
hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
  firstValid = cms.vuint32( 1 )
)
hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
  firstValid = cms.vuint32( 1 )
)
magfield = cms.ESSource( "XMLIdealGeometryESSource",
  geomXMLFiles = cms.vstring( 'Geometry/CMSCommonData/data/normal/cmsextent.xml',
    'Geometry/CMSCommonData/data/cms.xml',
    'Geometry/CMSCommonData/data/cmsMagneticField.xml',
    'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml',
    'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml' ),
  rootNodeName = cms.string( "cmsMagneticField:MAGF" )
)

AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
AutoMagneticFieldESProducer = cms.ESProducer( "AutoMagneticFieldESProducer",
  label = cms.untracked.string( "" ),
  nominalCurrents = cms.untracked.vint32( -1, 0, 9558, 14416, 16819, 18268, 19262 ),
  valueOverride = cms.int32( -1 ),
  mapLabels = cms.untracked.vstring( '090322_3_8t',
    '0t',
    '071212_2t',
    '071212_3t',
    '071212_3_5t',
    '090322_3_8t',
    '071212_4t' )
)
CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  useRealWireGeometry = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  alignmentsLabel = cms.string( "" ),
  useGangedStripsInME1a = cms.bool( True ),
  debugV = cms.untracked.bool( False ),
  useOnlyWiresInME1a = cms.bool( False ),
  useDDD = cms.bool( False ),
  useCentreTIOffsets = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  SelectedCalos = cms.vstring( 'HCAL',
    'ZDC',
    'EcalBarrel',
    'EcalEndcap',
    'EcalPreshower',
    'TOWER' )
)
CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder" )
CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" )
)
CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" )
)
DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder" )
EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService" )
EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
EcalUnpackerWorkerESProducer = cms.ESProducer( "EcalUnpackerWorkerESProducer",
  CalibRHAlgo = cms.PSet( 
    flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 7, 7, 7, 8, 9 ),
    Type = cms.string( "EcalRecHitWorkerSimple" ),
    killDeadChannels = cms.bool( True ),
    ChannelStatusToBeExcluded = cms.vint32( 10, 11, 12, 13, 14 ),
    laserCorrection = cms.bool( False ),
    EBLaserMIN = cms.double( 0.5 ),
    EELaserMIN = cms.double( 0.5 ),
    EBLaserMAX = cms.double( 2.0 ),
    EELaserMAX = cms.double( 3.0 )
  ),
  ComponentName = cms.string( "" ),
  UncalibRHAlgo = cms.PSet(  Type = cms.string( "EcalUncalibRecHitWorkerWeights" ) ),
  DCCDataUnpacker = cms.PSet( 
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    tccUnpacking = cms.bool( False ),
    srpUnpacking = cms.bool( False ),
    syncCheck = cms.bool( False ),
    feIdCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    feUnpacking = cms.bool( True ),
    forceKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
  ),
  ElectronicsMapper = cms.PSet( 
    numbXtalTSamples = cms.uint32( 10 ),
    numbTriggerTSamples = cms.uint32( 1 )
  )
)
HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP" )
L1GtTriggerMaskAlgoTrigTrivialProducer = cms.ESProducer( "L1GtTriggerMaskAlgoTrigTrivialProducer",
  TriggerMask = cms.vuint32( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )
)
L1GtTriggerMaskTechTrigTrivialProducer = cms.ESProducer( "L1GtTriggerMaskTechTrigTrivialProducer",
  TriggerMask = cms.vuint32( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )
)
MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
MaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
OppositeMaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  useDDD = cms.untracked.bool( False ),
  compatibiltyWith11 = cms.untracked.bool( True )
)
SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  printDebug = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" ),
  APVGain = cms.VPSet( 
    cms.PSet(  Record = cms.string( "SiStripApvGainRcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    ),
    cms.PSet(  Record = cms.string( "SiStripApvGain2Rcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    )
  ),
  AutomaticNormalization = cms.bool( False )
)
SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
  appendToDataLabel = cms.string( "" ),
  PrintDebugOutput = cms.bool( False ),
  ThresholdForReducedGranularity = cms.double( 0.3 ),
  UseEmptyRunInfo = cms.bool( False ),
  ReduceGranularity = cms.bool( False ),
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiStripDetVOffRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripDetCablingRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadChannelRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadFiberRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadModuleRcd" ),
      tag = cms.string( "" )
    )
  )
)
SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 )
)
SlaveField0 = cms.ESProducer( "UniformMagneticFieldESProducer",
  ZFieldInTesla = cms.double( 0.0 ),
  label = cms.untracked.string( "slave_0" )
)
SlaveField20 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "2_0T" ) ),
  label = cms.untracked.string( "slave_20" )
)
SlaveField30 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_0T" ) ),
  label = cms.untracked.string( "slave_30" )
)
SlaveField35 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_5T" ) ),
  label = cms.untracked.string( "slave_35" )
)
SlaveField38 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_8T" ) ),
  label = cms.untracked.string( "slave_38" )
)
SlaveField40 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "4_0T" ) ),
  label = cms.untracked.string( "slave_40" )
)
SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "SteppingHelixPropagatorAny" )
)
StripCPEfromTrackAngleESProducer = cms.ESProducer( "StripCPEESProducer",
  TanDiffusionAngle = cms.double( 0.01 ),
  UncertaintyScaling = cms.double( 1.42 ),
  ThicknessRelativeUncertainty = cms.double( 0.02 ),
  MaybeNoiseThreshold = cms.double( 3.5 ),
  ComponentName = cms.string( "StripCPEfromTrackAngle" ),
  MinimumUncertainty = cms.double( 0.01 ),
  NoiseThreshold = cms.double( 2.3 )
)
TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  fromDDD = cms.bool( False )
)
TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" )
)
VBF0 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "0t" ),
  version = cms.string( "grid_1103l_071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_0" ),
  cacheLastVolume = cms.untracked.bool( True )
)
VBF20 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_2t" ),
  version = cms.string( "grid_1103l_071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_20" ),
  cacheLastVolume = cms.untracked.bool( True )
)
VBF30 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_3t" ),
  version = cms.string( "grid_1103l_071212_3t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_30" ),
  cacheLastVolume = cms.untracked.bool( True )
)
VBF35 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_3_5t" ),
  version = cms.string( "grid_1103l_071212_3_5t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_35" ),
  cacheLastVolume = cms.untracked.bool( True )
)
VBF38 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32( 14100, 14200, 17600, 17800, 17900, 18100, 18300, 18400, 18600, 23100, 23300, 23400, 23600, 23800, 23900, 24100, 28600, 28800, 28900, 29100, 29300, 29400, 29600, 28609, 28809, 28909, 29109, 29309, 29409, 29609, 28610, 28810, 28910, 29110, 29310, 29410, 29610, 28611, 28811, 28911, 29111, 29311, 29411, 29611 ),
  overrideMasterSector = cms.bool( False ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble( 1.0, 1.0, 0.994, 1.004, 1.004, 1.005, 1.004, 1.004, 0.994, 0.965, 0.958, 0.958, 0.953, 0.958, 0.958, 0.965, 0.918, 0.924, 0.924, 0.906, 0.924, 0.924, 0.918, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991 ),
  label = cms.untracked.string( "090322_3_8t" ),
  version = cms.string( "grid_1103l_090322_3_8t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_38" ),
  cacheLastVolume = cms.untracked.bool( True )
)
VBF40 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_4t" ),
  version = cms.string( "grid_1103l_071212_4t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_40" ),
  cacheLastVolume = cms.untracked.bool( True )
)
ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" )
)
ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet( 
    kGood = cms.vuint32( 0 ),
    kProblematic = cms.vuint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
    kRecovered = cms.vuint32(  ),
    kTime = cms.vuint32(  ),
    kWeird = cms.vuint32(  ),
    kBad = cms.vuint32( 11, 12, 13, 14, 15, 16 )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet( 
    kGood = cms.vstring( 'kGood' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kTime = cms.vstring( 'kOutOfTime' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' )
  )
)
hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  SeverityLevels = cms.VPSet( 
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HSCP_R1R2',
  'HSCP_FracLeader',
  'HSCP_OuterEnergy',
  'HSCP_ExpFit',
  'ADCSaturationBit' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
  'HFDigiTime',
  'HBHEPulseShape',
  'HOBit',
  'HFInTimeWindow',
  'ZDCBit',
  'CalibrationBit',
  'TimingErrorBit' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HFLongShort',
  'HFS8S1Ratio',
  'HFPET' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellHot' ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
hcal_db_producer = cms.ESProducer( "HcalDbProducer" )
hltESPAK5CaloL1L2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPL1FastJetCorrectionESProducer',
    'hltESPL2RelativeCorrectionESProducer',
    'hltESPL3AbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
hltESPAK5CaloL2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPL2RelativeCorrectionESProducer',
    'hltESPL3AbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( '""oppositeToMomentum"' )
)
hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( '"oppositeToMomentum""' ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
hltESPChi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2EstimatorForRefit" )
)
hltESPChi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator" )
)
hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" )
)
hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" )
)
hltESPCkf3HitTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkf3HitTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPCkf3HitTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPCkf3HitTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPCkf3HitTrajectoryFilter" )
)
hltESPCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPCkfTrajectoryBuilderForHI = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilterForHI" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPCkfTrajectoryBuilderForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerForHI" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPCkfTrajectoryFilter" )
)
hltESPCkfTrajectoryFilterForHI = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minimumNumberOfHits = cms.int32( 6 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 11.0 )
  ),
  ComponentName = cms.string( "hltESPCkfTrajectoryFilterForHI" )
)
hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPESUnpackerWorker = cms.ESProducer( "ESUnpackerWorkerESProducer",
  RHAlgo = cms.PSet( 
    ESRecoAlgo = cms.int32( 0 ),
    Type = cms.string( "ESRecHitWorker" )
  ),
  DCCDataUnpacker = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) ),
  ComponentName = cms.string( "hltESPESUnpackerWorker" )
)
hltESPEcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  esMapping = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) )
)
hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" )
)
hltESPElectronChi2 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 2000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPElectronChi2" )
)
hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 10.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
hltESPGlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" )
hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
hltESPHIMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
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
    'TEC2_neg+TEC3_neg' ),
  ComponentName = cms.string( "hltESPHIMixedLayerPairs" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0060 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPHIPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
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
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPHIPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPHIPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPHIPixelLayerTriplets" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPHITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "Fake" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "Fake" ),
  ComponentName = cms.string( "hltESPHITTRHBuilderWithoutRefit" )
)
hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPRKFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKSmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
hltESPL1FastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( 'hltKT6CaloJets','rho' ),
  algorithm = cms.string( "AK5Calo" ),
  level = cms.string( "L1FastJet" )
)
hltESPL2RelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5Calo" ),
  level = cms.string( "L2Relative" )
)
hltESPL3AbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5Calo" ),
  level = cms.string( "L3Absolute" )
)
hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltSiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
hltESPMeasurementTrackerForHI = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( False ),
  Regional = cms.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltHISiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripRawToDigi' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltHISiStripClustersNonRegional" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TID = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerForHI" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
hltESPMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
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
    'TEC2_neg+TEC3_neg' ),
  ComponentName = cms.string( "hltESPMixedLayerPairs" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPMuTrackJpsiTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPMuTrackJpsiEffTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuTrackJpsiEffTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltESPMuTrackJpsiEffTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPMuTrackJpsiTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" )
)
hltESPMuTrackJpsiEffTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 9 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPMuTrackJpsiEffTrajectoryFilter" )
)
hltESPMuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPMuonCkfTrajectoryBuilderSeedHit = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryBuilderSeedHit" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( True ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPMuonCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 )
  ),
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryFilter" )
)
hltESPMuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer" )
hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  EdgeClusterErrorX = cms.double( 50.0 ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  UseErrorsFromTemplates = cms.bool( True ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  IrradiationBiasCorrection = cms.bool( False ),
  TanLorentzAnglePerTesla = cms.double( 0.106 ),
  inflate_errors = cms.bool( False ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  Alpha2Order = cms.bool( True )
)
hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
hltESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
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
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPPixelLayerTriplets" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPPixelLayerTripletsHITHB = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3' ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHB" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPPixelLayerTripletsHITHE = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHE" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.03 ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKSmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
hltESPSiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
hltESPSmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorOpposite" )
)
hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
hltESPSoftLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  ipSign = cms.string( "any" )
)
hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
hltESPStraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
  ComponentName = cms.string( "hltESPStraightLinePropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
hltESPTrackCounting3D1st = cms.ESProducer( "TrackCountingESProducer",
  deltaR = cms.double( -1.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  maximumDecayLength = cms.double( 5.0 ),
  nthTrack = cms.int32( 1 )
)
hltESPTrackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  deltaR = cms.double( -1.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  maximumDecayLength = cms.double( 5.0 ),
  nthTrack = cms.int32( 2 )
)
hltESPTrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  appendToDataLabel = cms.string( "" ),
  trackerGeometryLabel = cms.untracked.string( "" )
)
hltESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPTrajectoryBuilderL3 = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterL3" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPTrajectoryBuilderL3" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPTrajectoryBuilderForElectrons = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterForElectrons" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltESPTrajectoryBuilderForElectrons" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPElectronChi2" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( False )
)
hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedSeeds" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
hltESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPTrajectoryFilterIT" )
)
hltESPTrajectoryFilterL3 = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 1000000000 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPTrajectoryFilterL3" )
)
hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPTrajectoryFilterForElectrons = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    minPt = cms.double( 2.0 ),
    minHitsMinPt = cms.int32( -1 ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 3 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPTrajectoryFilterForElectrons" )
)
hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPbJetRegionalTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESPbJetRegionalTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryFilter" )
)
hltHIAllESPCkf3HitTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkf3HitTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPCkf3HitTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltHIAllESPCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltHIAllESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltHISiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltHISiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltHISiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltHIAllESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
hltHIAllESPMuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPMuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
hltHIAllESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 5 ),
  ComponentName = cms.string( "hltHIAllESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltIter1ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter1SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter1ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
hltIter1ESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter1ESPPixelLayerTriplets" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltIter1ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter1ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter1ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltIter1ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.2 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter1ESPTrajectoryFilterIT" )
)
hltIter2ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter2SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter2ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
hltIter2ESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2',
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
    'FPix1_neg+FPix2_neg' ),
  ComponentName = cms.string( "hltIter2ESPPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  ),
  TOB = cms.PSet(  )
)
hltIter2ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter2ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 2 ),
  ComponentName = cms.string( "hltIter2ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltIter2ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter2ESPTrajectoryFilterIT" )
)
hltIter3ESPLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg',
    'BPix2+FPix1_pos+FPix2_pos',
    'BPix2+FPix1_neg+FPix2_neg',
    'FPix1_pos+FPix2_pos+TEC1_pos',
    'FPix1_neg+FPix2_neg+TEC1_neg',
    'FPix2_pos+TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC2_neg+TEC3_neg',
    'BPix2+BPix3+TIB1',
    'BPix2+BPix3+TIB2',
    'BPix1+BPix3+TIB1',
    'BPix1+BPix3+TIB2',
    'BPix1+BPix2+TIB1',
    'BPix1+BPix2+TIB2' ),
  ComponentName = cms.string( "hltIter3ESPLayerTriplets" ),
  TEC = cms.PSet( 
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  ),
  FPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0051 )
  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet( 
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0060 ),
    useErrorsFromParam = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    skipClusters = cms.InputTag( "hltIter3ClustersRefRemoval" ),
    hitErrorRPhi = cms.double( 0.0027 )
  ),
  TIB = cms.PSet(  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ) ),
  TOB = cms.PSet(  )
)
hltIter3ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter3SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter3ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter3ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
hltIter3ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter3ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter3ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
hltIter3ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 0 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter3ESPTrajectoryFilterIT" )
)
hltIter4ESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  OnDemand = cms.bool( True ),
  Regional = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  stripClusterProducer = cms.string( "hltIter4SiStripClusters" ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltIter4ESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  skipClusters = cms.InputTag( "hltIter4ClustersRefRemoval" ),
  UseStripModuleQualityDB = cms.bool( True ),
  UseStripNoiseDB = cms.bool( False ),
  UseStripCablingDB = cms.bool( False )
)
hltIter4ESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  layerList = cms.vstring( 'TIB1+TIB2' ),
  ComponentName = cms.string( "hltIter4ESPPixelLayerPairs" ),
  TEC = cms.PSet(  ),
  FPix = cms.PSet(  ),
  TID = cms.PSet(  ),
  BPix = cms.PSet(  ),
  TIB = cms.PSet(  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ) ),
  TOB = cms.PSet(  )
)
hltIter4ESPTrajectoryBuilderIT = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilterName = cms.string( "hltIter4ESPTrajectoryFilterIT" ),
  maxCand = cms.int32( 1 ),
  ComponentName = cms.string( "hltIter4ESPTrajectoryBuilderIT" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
hltIter4ESPTrajectoryFilterIT = cms.ESProducer( "TrajectoryFilterESProducer",
  filterPset = cms.PSet( 
    minPt = cms.double( 0.3 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 0 ),
    maxNumberOfHits = cms.int32( 100 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 6 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  ),
  ComponentName = cms.string( "hltIter4ESPTrajectoryFilterIT" )
)
hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" )
)
preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  LorentzAngleDeconvMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  LorentzAnglePeakMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
sistripconn = cms.ESProducer( "SiStripConnectivity" )

FastTimerService = cms.Service( "FastTimerService",
  dqmPath = cms.untracked.string( "HLT/TimerService" ),
  useRealTimeClock = cms.untracked.bool( True ),
  dqmTimeResolution = cms.untracked.double( 1.0 ),
  enableDQMbyLumi = cms.untracked.bool( False ),
  enableTimingPaths = cms.untracked.bool( True ),
  enableTimingModules = cms.untracked.bool( True ),
  enableDQM = cms.untracked.bool( True ),
  dqmTimeRange = cms.untracked.double( 200.0 ),
  enableTimingSummary = cms.untracked.bool( True )
)
DQM = cms.Service( "DQM",
  publishFrequency = cms.untracked.double( 5.0 ),
  debug = cms.untracked.bool( False ),
  collectorPort = cms.untracked.int32( 9190 ),
  collectorHost = cms.untracked.string( "lxplus444.cern.ch" )
)
DQMStore = cms.Service( "DQMStore",
)
DTDataIntegrityTask = cms.Service( "DTDataIntegrityTask",
  processingMode = cms.untracked.string( "HLT" ),
  fedIntegrityFolder = cms.untracked.string( "DT/FEDIntegrity_EvF" ),
  getSCInfo = cms.untracked.bool( True )
)
FUShmDQMOutputService = cms.Service( "FUShmDQMOutputService",
  lumiSectionInterval = cms.untracked.int32( 0 ),
  compressionLevel = cms.int32( 1 ),
  initialMessageBufferSize = cms.untracked.int32( 1000000 ),
  lumiSectionsPerUpdate = cms.double( 1.0 ),
  useCompression = cms.bool( True )
)
MessageLogger = cms.Service( "MessageLogger",
  debugs = cms.untracked.PSet( 
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True ),
  ),
  cout = cms.untracked.PSet( 
    threshold = cms.untracked.string( "ERROR" ),
  ),
  cerr_stats = cms.untracked.PSet( 
    threshold = cms.untracked.string( "WARNING" ),
    output = cms.untracked.string( "cerr" ),
    optionalPSet = cms.untracked.bool( True )
  ),
  warnings = cms.untracked.PSet( 
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True ),
  ),
  statistics = cms.untracked.vstring( 'cerr' ),
  cerr = cms.untracked.PSet( 
    INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
    noTimeStamps = cms.untracked.bool( False ),
    FwkReport = cms.untracked.PSet( 
      reportEvery = cms.untracked.int32( 1 ),
      limit = cms.untracked.int32( 0 )
    ),
    default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
    Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
    FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
    FwkSummary = cms.untracked.PSet( 
      reportEvery = cms.untracked.int32( 1 ),
      limit = cms.untracked.int32( 10000000 )
    ),
    threshold = cms.untracked.string( "INFO" ),
  ),
  FrameworkJobReport = cms.untracked.PSet( 
    default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
    FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
  ),
  suppressWarning = cms.untracked.vstring( 'hltL3MuonsOIState',
    'hltPixelVertices3DbbPhi',
    'hltSiPixelDigis',
    'hltPixelTracksForHighMult',
    'hltSiPixelClusters',
    'hltLightPFTracks',
    'hltPixelTracks',
    'hltOnlineBeamSpot',
    'hltL3MuonsOIHit',
    'hltHITPixelTracksHE',
    'hltHITPixelTracksHB',
    'hltL3MuonsIOHit' ),
  errors = cms.untracked.PSet( 
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True ),
  ),
  fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
  infos = cms.untracked.PSet( 
    threshold = cms.untracked.string( "INFO" ),
    Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
    placeholder = cms.untracked.bool( True ),
  ),
  categories = cms.untracked.vstring( 'FwkJob',
    'FwkReport',
    'FwkSummary',
    'Root_NoDictionary' ),
  destinations = cms.untracked.vstring( 'warnings',
    'errors',
    'infos',
    'debugs',
    'cout',
    'cerr' ),
  threshold = cms.untracked.string( "INFO" ),
  suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot' )
)
MicroStateService = cms.Service( "MicroStateService",
)
ModuleWebRegistry = cms.Service( "ModuleWebRegistry",
)
PrescaleService = cms.Service( "PrescaleService",
  prescaleTable = cms.VPSet(  *(
    cms.PSet(  pathName = cms.string( "HLT_Activity_Ecal_SC7_v9" ),
      prescales = cms.vuint32( 150, 100, 75, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFJet40_v1" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFJet80_v1" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFJet140_v1" ),
      prescales = cms.vuint32( 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFJet200_v1" ),
      prescales = cms.vuint32( 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFJet260_v1" ),
      prescales = cms.vuint32( 14, 14, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFJet320_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFJet400_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MonoCentralPFJet80L1FastJet_PFMHTWOM95_NHEF95_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJetAve40_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJetAve80_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJetAve140_v1" ),
      prescales = cms.vuint32( 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJetAve200_v1" ),
      prescales = cms.vuint32( 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJetAve260_v1" ),
      prescales = cms.vuint32( 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJetAve320_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJetAve400_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiJet80_DiJet60_DiJet20_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJet40L1FastJet_PFMHTWOM65_M800VBF_ALLJETS_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiPFJet40L1FastJet_PFMHTWOM65_M600VBF_LEADINGJETS_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiJet40Eta2p6_L1FastJet_BTagIP3D_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiJet80Eta2p6_L1FastJet_BTagIP3DLoose_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Jet60Eta1p7_Jet53Eta1p7_L1FastJet_DiBTagIP3D_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Jet80Eta1p7_Jet70Eta1p7_L1FastJet_DiBTagIP3D_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Jet160Eta2p4_Jet120Eta2p4_L1FastJet_DiBTagIP3DLoose_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_QuadJet50_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_QuadJet60_DiJet20_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_QuadJet70_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_QuadJet80_L1FastJet_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_QuadJet90_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_QuadL1FastJet_BTagIP_VBF_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_SixJet35_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_SixJet45_L1FastJet_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_SixJet50_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_EightJet35_L1FastJet_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_EightJet40_L1FastJet_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_ExclDiJet80_HFAND_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_JetE30_NoBPTX_v9" ),
      prescales = cms.vuint32( 60, 30, 24, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_JetE30_NoBPTX3BX_NoHalo_v11" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_JetE50_NoBPTX3BX_NoHalo_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_JetE70_NoBPTX3BX_NoHalo_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT200_AlphaT0p57_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT200_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT250_AlphaT0p55_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT250_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_ChgFraction10_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT250_L1FastJet_SingleDisplacedPFJet60_v1" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT250_L1FastJet_SingleDisplacedPFJet60_ChgFraction10_v1" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT300_AlphaT0p53_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT300_AlphaT0p54_v6" ),
      prescales = cms.vuint32( 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT300_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT350_L1FastJet_v4" ),
      prescales = cms.vuint32( 4000, 600, 600, 600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT350_AlphaT0p52_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT350_AlphaT0p53_v11" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT400_L1FastJet_v4" ),
      prescales = cms.vuint32( 1000, 400, 400, 400, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT400_AlphaT0p51_v11" ),
      prescales = cms.vuint32( 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT400_AlphaT0p52_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT450_AlphaT0p51_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT450_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT500_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT550_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HT750_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT350_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT650_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT650_DiCentralPFJet80_CenPFJet40_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT700_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT750_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFMHT150_v18" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFMHT180_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DiCentralPFJet50_PFMHT80_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET80_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET80_Track50_dEdx3p6_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET80_Track60_dEdx3p7_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET120_v8" ),
      prescales = cms.vuint32( 8, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET120_HBHENoiseCleaned_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET200_v8" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET200_HBHENoiseCleaned_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET300_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET300_HBHENoiseCleaned_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET400_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_MET400_HBHENoiseCleaned_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1SingleMuOpen_v5" ),
      prescales = cms.vuint32( 600, 600, 600, 600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1SingleMu12_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L2Mu20_eta2p1_NoVertex_v1" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L2Mu20_NoVertex_NoBPTX3BX_NoHalo_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L2Mu30_NoVertex_NoBPTX3BX_NoHalo_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleDisplacedMu4_DiPFJet40Neutral_L1FastJet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu5_v15" ),
      prescales = cms.vuint32( 320, 640, 640, 640, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu8_v13" ),
      prescales = cms.vuint32( 40, 40, 40, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu12_v13" ),
      prescales = cms.vuint32( 70, 70, 70, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu17_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu15_eta2p1_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu24_eta2p1_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu30_eta2p1_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu40_eta2p1_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu50_eta2p1_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu20_eta2p1_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu24_eta2p1_v8" ),
      prescales = cms.vuint32( 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu30_eta2p1_v8" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu34_eta2p1_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu40_eta2p1_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Iso10Mu17_eta2p1_TriCentralPFJet30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu40_eta2p1_Track50_dEdx3p6_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu40_eta2p1_Track60_dEdx3p7_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L2DoubleMu23_NoVertex_v9" ),
      prescales = cms.vuint32( 20, 20, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu4_Jpsi_Displaced_v6" ),
      prescales = cms.vuint32( 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu4_JpsiTk_Displaced_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu4_Dimuon4_Bs_Barrel_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu4_Dimuon6_Bs_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu3p5_LowMass_Displaced_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon0_Jpsi_v11" ),
      prescales = cms.vuint32( 200, 160, 120, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon0_Jpsi_NoVertexing_v8" ),
      prescales = cms.vuint32( 200, 160, 120, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon0_Upsilon_v11" ),
      prescales = cms.vuint32( 200, 160, 120, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon0_PsiPrime_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon5_Upsilon_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon5_PsiPrime_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon5_Jpsi_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon8_Upsilon_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon9_PsiPrime_v6" ),
      prescales = cms.vuint32( 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon9_Jpsi_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Dimuon3p5_SameSign_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Tau2Mu_RegPixTrack_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu13_Mu8_v12" ),
      prescales = cms.vuint32( 40, 30, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu17_Mu8_v12" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu17_TkMu8_v5" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu22_TkMu8_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu22_TkMu22_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_TripleMu5_v14" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu5_IsoMu5_v13" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu5_L2Mu3_Jpsi_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu5_Track2_Jpsi_v14" ),
      prescales = cms.vuint32( 6, 6, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu5_Track3p5_Jpsi_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon20_CaloIdVL_IsoL_v10" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon20_R9Id_Photon18_R9Id_v8" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon26_Photon18_v8" ),
      prescales = cms.vuint32( 600, 450, 340, 340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon26_R9Id85_Photon18_R9Id85_Mass60_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_Mass60_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon26_CaloId10_Iso50_Photon18_R9Id85_Mass60_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon26_CaloId10_Iso50_Photon18_CaloId10_Iso50_Mass60_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass60_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v1" ),
      prescales = cms.vuint32( 1600, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon30_CaloIdVL_v9" ),
      prescales = cms.vuint32( 7000, 5600, 4200, 4200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon30_CaloIdVL_IsoL_v12" ),
      prescales = cms.vuint32( 2500, 2000, 1500, 1500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon36_Photon22_v2" ),
      prescales = cms.vuint32( 300, 240, 180, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon36_R9Id85_Photon22_R9Id85_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v1" ),
      prescales = cms.vuint32( 500, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon50_CaloIdVL_v5" ),
      prescales = cms.vuint32( 900, 720, 540, 540, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon50_CaloIdVL_IsoL_v10" ),
      prescales = cms.vuint32( 330, 270, 200, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon60_CaloIdL_MHT70_v4" ),
      prescales = cms.vuint32( 3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon60_CaloIdL_FJHT300_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon70_CaloIdXL_MHT100_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon70_CaloIdXL_FJHT400_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon70_CaloIdXL_FJHT500_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon75_CaloIdVL_v8" ),
      prescales = cms.vuint32( 150, 120, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon75_CaloIdVL_IsoL_v11" ),
      prescales = cms.vuint32( 60, 45, 35, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon90_CaloIdVL_v5" ),
      prescales = cms.vuint32( 75, 60, 45, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon90_CaloIdVL_IsoL_v8" ),
      prescales = cms.vuint32( 20, 15, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet25_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet30_v6" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon135_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon150_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon160_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon250_NoHE_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon300_NoHE_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoublePhoton43_HEVT_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoublePhoton48_HEVT_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoublePhoton70_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoublePhoton80_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele8_CaloIdL_CaloIsoVL_v11" ),
      prescales = cms.vuint32( 30, 30, 30, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele17_CaloIdL_CaloIsoVL_v11" ),
      prescales = cms.vuint32( 110, 110, 110, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele22_CaloIdL_CaloIsoVL_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4" ),
      prescales = cms.vuint32( 1250, 1000, 750, 750, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_WP80_v4" ),
      prescales = cms.vuint32( 200, 160, 120, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_WP80_PFMT50_v10" ),
      prescales = cms.vuint32( 100, 80, 60, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele30_CaloIdVT_TrkIdT_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele32_WP70_v4" ),
      prescales = cms.vuint32( 25, 20, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele32_WP70_PFMT50_v10" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v4" ),
      prescales = cms.vuint32( 250, 150, 150, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele65_CaloIdVT_TrkIdT_v7" ),
      prescales = cms.vuint32( 30, 25, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele80_CaloIdVT_TrkIdT_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele100_CaloIdVT_TrkIdT_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleEle33_CaloIdL_v8" ),
      prescales = cms.vuint32( 50, 40, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleEle33_CaloIdT_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_LooseIsoPFTau35_Trk20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_LooseIsoPFTau35_Trk20_MET70_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_LooseIsoPFTau35_Trk20_MET75_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleLooseIsoPFTau45_Trk5_eta2p1_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet20_L1FastJet_Mu5_v1" ),
      prescales = cms.vuint32( 60, 60, 60, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet40_L1FastJet_Mu5_v1" ),
      prescales = cms.vuint32( 30, 30, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet70_L1FastJet_Mu5_v1" ),
      prescales = cms.vuint32( 10, 8, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BTagMu_DiJet110_L1FastJet_Mu5_v1" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BTagMu_Jet300_L1FastJet_Mu5_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu12_DoubleCentralJet65_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu15_eta2p1_L1ETM20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu24_eta2p1_CentralPFJet30_CentralPFJet25_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu24_eta2p1_PFJet30_PFJet25_Deta3_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu24_eta2p1_PFJet30_PFJet25_Deta3_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_PFMHT20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_WP80_PFJet30_PFJet25_Deta3_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_PFMHT20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Iso10Mu20_eta2p1_CentralPFJet30_BTagIPIter_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Iso10Mu20_eta2p1_CentralPFJet30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Iso10Mu20_eta2p1_DiCentralPFJet30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Iso10Mu20_eta2p1_TriCentralPFJet30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Iso10Mu20_eta2p1_QuadCentralPFJet30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu20_eta2p1_QuadCentralPFJet30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu20_eta2p1_TriCentralPFJet30_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu30_Ele30_CaloIdL_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu15_eta2p1_L1ETM20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_L1ETM20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu17_eta2p1_DiCentralPFJet30_PFHT350_PFMHT40_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu20_eta2p1_CentralPFJet80_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu18_eta2p1_LooseIsoPFTau20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20L1Jet_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele20_CaloIdVT_TrkIdT_LooseIsoPFTau20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu8_Mass8_PFHT225_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu8_Mass8_PFHT175_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT350_Mu15_PFMET45_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT350_Mu15_PFMET50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT400_Mu5_PFMET45_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT400_Mu5_PFMET50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu40_PFHT350_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu60_PFHT350_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu40_FJHT200_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v9" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu5_Ele8_CaloIdT_TrkIdT_v5" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v10" ),
      prescales = cms.vuint32( 1500, 1200, 900, 900, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v10" ),
      prescales = cms.vuint32( 150, 120, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v10" ),
      prescales = cms.vuint32( 10, 8, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v4" ),
      prescales = cms.vuint32( 60, 60, 60, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele25_CaloIdVT_TrkIdT_QuadCentralPFJet30_v4" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_v4" ),
      prescales = cms.vuint32( 200, 120, 120, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_DiCentralPFJet30_v4" ),
      prescales = cms.vuint32( 60, 60, 60, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_QuadCentralPFJet30_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_BTagIPIter_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele27_WP80_CentralPFJet80_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele30_CaloIdVT_TrkIdT_PFJet100_PFJet25_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele30_CaloIdVT_TrkIdT_PFJet150_PFJet25_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT175_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT225_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_RsqMR40_Rsq0p04_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_RsqMR55_Rsq0p09_MR150_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_RsqMR60_Rsq0p09_MR150_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu12_RsqMR30_Rsq0p04_MR200_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu12_RsqMR40_Rsq0p04_MR200_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon40_CaloIdL_RsqMR35_Rsq0p09_MR150_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoublePhoton40_CaloIdL_Rsq0p035_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoublePhoton40_CaloIdL_Rsq0p06_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu22_Photon22_CaloIdL_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu14_Mass8_PFMET40_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleMu14_Mass8_PFMET50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT350_PFMET100_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_PFHT400_PFMET100_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BeamGas_HF_Beam1_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BeamGas_HF_Beam2_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_BeamHalo_v9" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1Tech_CASTOR_HaloMuon_v2" ),
      prescales = cms.vuint32( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1Tech_DT_GlobalOR_v2" ),
      prescales = cms.vuint32( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoTrackHE_v11" ),
      prescales = cms.vuint32( 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_IsoTrackHB_v10" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_GlobalRunHPDNoise_v6" ),
      prescales = cms.vuint32( 1500, 1500, 1500, 1500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 40 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1Tech_HBHEHO_totalOR_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1Tech_HCAL_HF_single_channel_v2" ),
      prescales = cms.vuint32( 500, 500, 500, 500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_ZeroBias_v5" ),
      prescales = cms.vuint32( 50, 50, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Physics_v3" ),
      prescales = cms.vuint32( 8000, 8000, 8000, 8000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 80 )
    ),
    cms.PSet(  pathName = cms.string( "DST_Physics_v3" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DTCalibration_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_EcalCalibration_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_HcalCalibration_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_TrackerCalibration_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_Random_v1" ),
      prescales = cms.vuint32( 600, 600, 600, 600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 10000 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1SingleMuOpen_AntiBPTX_v4" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1TrackerCosmics_v5" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_LogMonitor_v1" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_DTErrors_v2" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLT_L1DoubleJet36Central_v5" ),
      prescales = cms.vuint32( 6000, 6000, 6000, 18000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_EcalPi0EBonly_v1" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_EcalPi0EEonly_v1" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_EcalEtaEBonly_v1" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_EcalEtaEEonly_v1" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_EcalPhiSym_v8" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_RPCMuonNoTriggers_v7" ),
      prescales = cms.vuint32( 9, 7, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_RPCMuonNoHits_v7" ),
      prescales = cms.vuint32( 9, 7, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_RPCMuonNormalisation_v7" ),
      prescales = cms.vuint32( 9, 7, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "AlCa_LumiPixels_v3" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "DQM_FEDIntegrity_v6" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 )
    ),
    cms.PSet(  pathName = cms.string( "AForPPOutput" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "DQMForPPOutput" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "ExpressForPPOutput" ),
      prescales = cms.vuint32( 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 )
    ),
    cms.PSet(  pathName = cms.string( "HLTMONOutput" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100 )
    )
) ),
  lvl1Labels = cms.vstring( '5e33',
    '4e33',
    '3e33',
    '2.5e33',
    '6000Hz',
    '5000Hz',
    '4000Hz',
    '3000Hz',
    '2000Hz',
    '1500Hz',
    '1000Hz',
    '500Hz',
    'EM1',
    'EM2',
    'Cosmics',
    'Cosmics + High Random' ),
  lvl1DefaultLabel = cms.untracked.string( "3e33" )
)
UpdaterService = cms.Service( "UpdaterService",
)

