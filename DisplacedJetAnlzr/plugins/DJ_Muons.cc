#include "UsercodeCMS/DisplacedJetAnlzr/interface/DJ_Muons.h"
#include "DataFormats/MuonReco/interface/MuonCocktails.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonPFIsolation.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include <iostream>
#include <DataFormats/TrackReco/interface/Track.h>
#include "TLorentzVector.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"

DJ_Muons::DJ_Muons(const edm::ParameterSet& iConfig) :
inputTag (iConfig.getParameter<edm::InputTag>("InputTag")),
prefix   (iConfig.getParameter<std::string>  ("Prefix")),
suffix   (iConfig.getParameter<std::string>  ("Suffix")),
maxSize  (iConfig.getParameter<unsigned int> ("MaxSize")),
muonIso  (iConfig.getParameter<double>       ("MuonIso")),                                 // threshold for "passIso" and "passCTIso"
muonID   (iConfig.getParameter<std::string>  ("MuonID")),                                  // threshold for "passID"
beamSpotCorr      (iConfig.getParameter<bool>("BeamSpotCorr")),
vtxInputTag       (iConfig.getParameter<edm::InputTag>("VertexInputTag"))                  // collection of primary vertices to be used.
{
  produces <std::vector<double> > ( prefix + "Eta"                     + suffix );
  produces <std::vector<double> > ( prefix + "Phi"                     + suffix );
  produces <std::vector<double> > ( prefix + "Pt"                      + suffix );
  produces <std::vector<double> > ( prefix + "TrkEta"                  + suffix );
  produces <std::vector<double> > ( prefix + "TrkPhi"                  + suffix );
  produces <std::vector<double> > ( prefix + "TrkPt"                   + suffix );
  produces <std::vector<double> > ( prefix + "P"                       + suffix );
  produces <std::vector<double> > ( prefix + "Energy"                  + suffix );
  produces <std::vector<int> >    ( prefix + "Charge"                  + suffix );
  produces <std::vector<int> >    ( prefix + "TrkHits"                 + suffix );
  produces <std::vector<int> >    ( prefix + "TrkHitsTrackerOnly"      + suffix );
  produces <std::vector<int> >    ( prefix + "GlobalTrkValidHits"      + suffix );
  produces <std::vector<int> >    ( prefix + "PixelHits"               + suffix );
  produces <std::vector<int> >    ( prefix + "TrkPixelHits"            + suffix );
  produces <std::vector<int> >    ( prefix + "SegmentMatches"          + suffix );
  produces <std::vector<int> >    ( prefix + "StationMatches"          + suffix );
  produces <std::vector<double> > ( prefix + "TrkValidFractionOfHits"  + suffix );
  produces <std::vector<double> > ( prefix + "TrkD0"                   + suffix );
  produces <std::vector<double> > ( prefix + "TrkD0Error"              + suffix );
  produces <std::vector<double> > ( prefix + "TrkDz"                   + suffix );
  produces <std::vector<double> > ( prefix + "TrkDzError"              + suffix );
  produces <std::vector<double> > ( prefix + "TrkVx"                   + suffix );
  produces <std::vector<double> > ( prefix + "TrkVy"                   + suffix );
  produces <std::vector<double> > ( prefix + "TrkVz"                   + suffix );
  produces <std::vector<double> > ( prefix + "TrackChi2"               + suffix );
  produces <std::vector<double> > ( prefix + "GlobalChi2"              + suffix );
  produces <std::vector<double> > ( prefix + "TrkIso"                  + suffix );
  produces <std::vector<double> > ( prefix + "TrackerIsoSumPT"         + suffix );
  produces <std::vector<double> > ( prefix + "EcalIso"                 + suffix );
  produces <std::vector<double> > ( prefix + "HcalIso"                 + suffix );
  produces <std::vector<double> > ( prefix + "HOIso"                   + suffix );
  produces <std::vector<double> > ( prefix + "EcalVetoIso"             + suffix );
  produces <std::vector<double> > ( prefix + "HcalVetoIso"             + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR03ChargedHadron"   + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR03ChargedParticle" + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR03NeutralHadron"   + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR03Photon"          + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR03NeutralHadronHT" + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR03PhotonHT"        + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR03PU"              + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR04ChargedHadron"   + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR04ChargedParticle" + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR04NeutralHadron"   + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR04Photon"          + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR04NeutralHadronHT" + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR04PhotonHT"        + suffix );
  produces <std::vector<double> > ( prefix + "PFIsoR04PU"              + suffix );
  produces <std::vector<int> >    ( prefix + "PassID"                  + suffix );
  produces <std::vector<int> >    ( prefix + "VtxIndex"                + suffix );
  produces <std::vector<double> > ( prefix + "VtxDistXY"               + suffix );
  produces <std::vector<double> > ( prefix + "VtxDistZ"                + suffix );
  produces <std::vector<int> >    ( prefix + "BestTrackVtxIndex"      + suffix );
  produces <std::vector<double> > ( prefix + "BestTrackVtxDistXY"     + suffix );
  produces <std::vector<double> > ( prefix + "BestTrackVtxDistZ"      + suffix );
  produces <std::vector<double> > ( prefix + "PrimaryVertexDXY"        + suffix );
  produces <std::vector<double> > ( prefix + "PrimaryVertexDXYError"   + suffix );
  produces <std::vector<double> > ( prefix + "BeamSpotDXY"             + suffix );
  produces <std::vector<double> > ( prefix + "BeamSpotDXYError"        + suffix );
  produces <std::vector<int> >    ( prefix + "IsGlobal"                + suffix );
  produces <std::vector<int> >    ( prefix + "IsTracker"               + suffix );
  //
  // New variables added based on CMSSW 52X recommendations for LooseMuon and TightMuon Definitions
  // https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Basline_muon_selections_for_2012
  produces <std::vector<int> >     ( prefix + "IsPF"                       + suffix );
  produces <std::vector<int> >     ( prefix + "TrackLayersWithMeasurement" + suffix );   

  produces <std::vector<double> > ( prefix + "CosmicCompatibility"     + suffix );
  produces <std::vector<double> > ( prefix + "TimeCompatibility"       + suffix );
  produces <std::vector<double> > ( prefix + "BackToBackCompatibility" + suffix );
  produces <std::vector<double> > ( prefix + "OverlapCompatibility"    + suffix );
}


void DJ_Muons::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  std::auto_ptr<std::vector<double> >  eta                     ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  phi                     ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pt                      ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkEta                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkPhi                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkPt                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  p                       ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  energy                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     charge                  ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     trkHits                 ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     trkHitsTrackerOnly      ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     GlobaltrkValidHits      ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     pixelHits               ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     trkPixelHits            ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     segmentMatches          ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     stationMatches          ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     Valid                   ( new std::vector<int>()     );
  std::auto_ptr<std::vector<double> >  trkValidFractionOfHits  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkD0                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkD0Error              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkDz                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkDzError              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkVx                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkVy                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkVz                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trackChi2               ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  globalChi2              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkIso                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trackerIsoSumPT         ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ecalIso                 ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  hcalIso                 ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  hoIso                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ecalVetoIso             ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  hcalVetoIso             ( new std::vector<double>()  );
  //
  std::auto_ptr<std::vector<double> >  pfisor03chargedhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03chargedparticle ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03neutralhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03photon          ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03neutralhadronht ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03photonht        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03pu              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04chargedhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04chargedparticle ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04neutralhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04photon          ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04neutralhadronht ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04photonht        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04pu              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     passID                  ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     vtxIndex                ( new std::vector<int>()     );
  std::auto_ptr<std::vector<double> >  vtxDistXY               ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  vtxDistZ                ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     bestTrackVtxIndex       ( new std::vector<int>()     );
  std::auto_ptr<std::vector<double> >  bestTrackVtxDistXY      ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  bestTrackVtxDistZ       ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  primaryVertexDXY        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  primaryVertexDXYError   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  beamspotDXY             ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  beamspotDXYError        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     IsGlobal                ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     IsTracker               ( new std::vector<int>()     );
  //
  // New variables added based on CMSSW 52X recommendations for LooseMuon and TightMuon Definitions
  // https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Basline_muon_selections_for_2012 
  std::auto_ptr<std::vector<int> >     isPF                       ( new std::vector<int>()    );
  std::auto_ptr<std::vector<int> >     trackLayersWithMeasurement ( new std::vector<int>()    );   
  //
  std::auto_ptr<std::vector<double> >  cosmicCompatibility     ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  timeCompatibility       ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  backToBackCompatibility ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  overlapCompatibility    ( new std::vector<double> () );
  
  //-----------------------------------------------------------------
  edm::Handle<std::vector<pat::Muon> > muons;
  iEvent.getByLabel(inputTag, muons);
  
  edm::Handle<reco::VertexCollection> primaryVertices;
  iEvent.getByLabel(vtxInputTag,primaryVertices);
  
  edm::Handle<reco::BeamSpot> beamSpot;
  iEvent.getByLabel("offlineBeamSpot", beamSpot );


  if(muons.isValid())
    {
      edm::LogInfo("DJ_MuonsInfo") << "Total # Muons: " << muons->size();
      
      size_t iMuon = 0;
    
      for( std::vector<pat::Muon>::const_iterator it = muons->begin(); it != muons->end(); ++it )
	{
	  // exit from loop when you reach the required number of muons
	  if(eta->size() >= maxSize)
	    break;
	  
	  //if muon is neither global nor tracker muon, continue.
	  if( !it->isGlobalMuon() && !it->isTrackerMuon() ) continue;
	  // if muonPt is less than 25GeV, continue.
	  if( it->pt()<25 ) continue;

	  double trkd0   = it->track()->d0();
	  
	  if( beamSpotCorr && beamSpot.isValid() )
	    {
	      trkd0   = -(it->track()   ->dxy( beamSpot->position()));
	    }
	  
	  else if( beamSpotCorr && !beamSpot.isValid() ) edm::LogError("DJ_MuonsError") << "Error! Can't get the offlineBeamSpot";
	  
	  // Vertex association 
	  //-- using pat::muon::track()
	  double minVtxDist3D = 9999.;
	  int    vtxIndex_    = -1;
	  double vtxDistXY_   = -9999.;
	  double vtxDistZ_    = -9999.;
	  //-- using reco::muon::muonBestTrack() - 2012 recommendation  
	  double bt_minVtxDist3D = 9999.;
	  int    bt_vtxIndex_    = -1;
	  double bt_vtxDistXY_   = -9999.;
	  double bt_vtxDistZ_    = -9999.;

	  if(primaryVertices.isValid())
	    {
	      edm::LogInfo("DJ_MuonsInfo") << "Total # Primary Vertices: " << primaryVertices->size();
	      
	      for( reco::VertexCollection::const_iterator v_it=primaryVertices->begin() ; v_it!=primaryVertices->end() ; ++v_it )
		{
		  //-- using pat::muon::track()
		  double distXY = it->track()->dxy(v_it->position());
		  double distZ  = it->track()->dz(v_it->position());
		  double dist3D = sqrt(pow(distXY,2) + pow(distZ,2));
		  if( dist3D < minVtxDist3D ){
		    minVtxDist3D = dist3D;
		    vtxIndex_    = int(std::distance(primaryVertices->begin(),v_it));
		    vtxDistXY_   = distXY;
		    vtxDistZ_    = distZ;
		  }
		  //-- using reco::muon::muonBestTrack() - 2012 recommendation    
		  if( (it->muonBestTrack()).isNonnull() ){
		    double bt_distXY = it->muonBestTrack()->dxy(v_it->position());
		    double bt_distZ  = it->muonBestTrack()->dz(v_it->position());
		    double bt_dist3D = sqrt( pow(bt_distXY,2) + pow(bt_distZ,2) );
		    if( bt_dist3D < bt_minVtxDist3D ){
		      bt_minVtxDist3D = bt_dist3D;
		      bt_vtxIndex_    = int(std::distance(primaryVertices->begin(),v_it));
		      bt_vtxDistXY_   = bt_distXY;
		      bt_vtxDistZ_    = bt_distZ;
		    }
		  }
		  
		}//loop over primaryVertices
	    }
	  else
	    {
	      edm::LogError("DJ_MuonsError") << "Error! Can't get the product " << vtxInputTag;
	    }

	  eta->push_back( it->eta() );
	  phi->push_back( it->phi() );
	  pt ->push_back( it->pt()  );
	  p  ->push_back( it->p()   );
	  
	  trkPt  -> push_back ( it->track()->pt()  );
	  trkEta -> push_back ( it->track()->eta() );
	  trkPhi -> push_back ( it->track()->phi() );
	  
	  charge            ->push_back( it->charge() );
	  trkHits           ->push_back( it->track()->numberOfValidHits() );
	  trkHitsTrackerOnly->push_back( it->track()->hitPattern().numberOfValidTrackerHits() );

	  if( it->isGlobalMuon() )
	    {
	      GlobaltrkValidHits->push_back( it->globalTrack()->hitPattern().numberOfValidMuonHits()  );
	      pixelHits         ->push_back( it->globalTrack()->hitPattern().numberOfValidPixelHits() );	    
	      globalChi2        ->push_back( it->globalTrack()->normalizedChi2()                      );
	    }
	  else
	    {
	      GlobaltrkValidHits->push_back( -1 );//inner track does not have muon hits by definition.
	      pixelHits         ->push_back( -1 );//inner track pixel hit count is stored at "innerTrackPixelHits".
	      globalChi2        ->push_back( -1 );//inner track Chi squared is already stored at  "trackChi2".
	    }

	  trkPixelHits->push_back(it->track()->hitPattern().numberOfValidPixelHits());
       
	  segmentMatches  ->push_back(it->numberOfMatches());
	  stationMatches  ->push_back(it->numberOfMatchedStations());
	  
	  trkValidFractionOfHits->push_back( it->track()->validFraction() );

	  trkD0     ->push_back( trkd0                         );
	  trkD0Error->push_back( it->track()->d0Error()        );
	  trkDz     ->push_back( it->track()->dz()             );
	  trkDzError->push_back( it->track()->dzError()        );
	  trkVx     ->push_back( it->track()->vx()             );
	  trkVy     ->push_back( it->track()->vy()             );
	  trkVz     ->push_back( it->track()->vz()             );
	  trackChi2 ->push_back( it->track()->normalizedChi2() );

	  // New variables added based on CMSSW 52X recommendations for LooseMuon and TightMuon Definitions
	  // https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Basline_muon_selections_for_2012 	  
	  isPF                       ->push_back( it->isPFMuon()       );
	  trackLayersWithMeasurement ->push_back( it->track()->hitPattern().trackerLayersWithMeasurement() );
	  
	  energy->push_back( it->energy() );
	  //
	  // 2011 isolation parameters..
	  // See: http://cmslxr.fnal.gov/lxr/source/DataFormats/MuonReco/interface/MuonIsolation.h?v=CMSSW_5_3_3_cand1#019
	  trkIso         ->push_back( it->trackIso()           );
	  trackerIsoSumPT->push_back( it->isolationR03().sumPt );
	  ecalIso        ->push_back( it->isolationR03().emEt  );
	  hcalIso        ->push_back( it->isolationR03().hadEt );
	  hoIso          ->push_back( it->isolationR03().hoEt  );
	  //
	  ecalVetoIso    ->push_back( it->isolationR03().emVetoEt  );
	  hcalVetoIso    ->push_back( it->isolationR03().hadVetoEt );
	  //
	  // Adding PF isolation for 2012..
	  //https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId
	  //The PF based isolation can be accessed by the reco::Muon using the following methods
	  //const MuonPFIsolation& pfIsolationR03() /// Cone of 0.3
	  //const MuonPFIsolation& pfIsolationR04() /// Cone of 0.4-Suggested  
	  //http://cmssdt.cern.ch/SDT/doxygen/CMSSW_5_2_5_patch3/doc/html/df/d33/structreco_1_1MuonPFIsolation.html
	  // "Inner Veto Cone" and "Iso Particle Pt Threshold" descriptions are here: 
	  // http://cmslxr.fnal.gov/lxr/source/RecoMuon/MuonIsolation/python/muonPFIsolationValues_cff.py?v=CMSSW_5_2_4
	  pfisor03chargedhadron  ->push_back( it->pfIsolationR03().sumChargedHadronPt              );
	  pfisor03chargedparticle->push_back( it->pfIsolationR03().sumChargedParticlePt            );
          pfisor03neutralhadron  ->push_back( it->pfIsolationR03().sumNeutralHadronEt              );
          pfisor03photon         ->push_back( it->pfIsolationR03().sumPhotonEt                     );
          pfisor03neutralhadronht->push_back( it->pfIsolationR03().sumNeutralHadronEtHighThreshold );
          pfisor03photonht       ->push_back( it->pfIsolationR03().sumPhotonEtHighThreshold        );
          pfisor03pu             ->push_back( it->pfIsolationR03().sumPUPt                         );
	  pfisor04chargedhadron  ->push_back( it->pfIsolationR04().sumChargedHadronPt              );
	  pfisor04chargedparticle->push_back( it->pfIsolationR04().sumChargedParticlePt            );
          pfisor04neutralhadron  ->push_back( it->pfIsolationR04().sumNeutralHadronEt              );
          pfisor04photon         ->push_back( it->pfIsolationR04().sumPhotonEt                     );
          pfisor04neutralhadronht->push_back( it->pfIsolationR04().sumNeutralHadronEtHighThreshold );
          pfisor04photonht       ->push_back( it->pfIsolationR04().sumPhotonEtHighThreshold        );
          pfisor04pu             ->push_back( it->pfIsolationR04().sumPUPt                         );

	  passID                 ->push_back( (it->muonID(muonID)) ?  1 : 0 );
	  IsGlobal               ->push_back( (it->isGlobalMuon()) ?  1 : 0 );
	  IsTracker              ->push_back( (it->isTrackerMuon()) ? 1 : 0 );
	  vtxIndex               ->push_back( vtxIndex_                     );
	  vtxDistXY              ->push_back( vtxDistXY_                    );
	  vtxDistZ               ->push_back( vtxDistZ_                     );
	  bestTrackVtxIndex      ->push_back( bt_vtxIndex_                  );
	  bestTrackVtxDistXY     ->push_back( bt_vtxDistXY_                 );
	  bestTrackVtxDistZ      ->push_back( bt_vtxDistZ_                  );
	  primaryVertexDXY       ->push_back( it->dB()                      );
	  primaryVertexDXYError  ->push_back( it->edB()                     );
	  beamspotDXY            ->push_back( it->dB(pat::Muon::BS2D)       );
	  beamspotDXYError       ->push_back( it->edB(pat::Muon::BS2D)      );
	  
	  // See https://indico.cern.ch/getFile.py/access?contribId=7&resId=0&materialId=slides&confId=102306
	  // and https://indico.cern.ch/getFile.py/access?contribId=5&resId=0&materialId=slides&confId=128840
	  cosmicCompatibility    ->push_back( it->userFloat("cosmicCompatibility")     );
	  timeCompatibility      ->push_back( it->userFloat("timeCompatibility")       );
	  backToBackCompatibility->push_back( it->userFloat("backToBackCompatibility") );
	  overlapCompatibility   ->push_back( it->userFloat("overlapCompatibility")    );
	  
	  iMuon++;

	}//end of loop over muons
    }
  else
    {
      edm::LogError("DJ_MuonsError") << "Error! Can't get the product " << inputTag;
    }
  
  //-----------------------------------------------------------------
  // put vectors in the event
  iEvent.put( eta,                        prefix + "Eta"                         + suffix );
  iEvent.put( phi,                        prefix + "Phi"                         + suffix );
  iEvent.put( pt,                         prefix + "Pt"                          + suffix );
  iEvent.put( trkEta,                     prefix + "TrkEta"                      + suffix );
  iEvent.put( trkPhi,                     prefix + "TrkPhi"                      + suffix );
  iEvent.put( trkPt,                      prefix + "TrkPt"                       + suffix );
  iEvent.put( p,                          prefix + "P"                           + suffix );
  iEvent.put( energy,                     prefix + "Energy"                      + suffix );
  iEvent.put( charge,                     prefix + "Charge"                      + suffix );
  iEvent.put( trkHits,                    prefix + "TrkHits"                     + suffix );
  iEvent.put( trkHitsTrackerOnly,         prefix + "TrkHitsTrackerOnly"          + suffix );
  iEvent.put( GlobaltrkValidHits,         prefix + "GlobalTrkValidHits"          + suffix );
  iEvent.put( pixelHits,                  prefix + "PixelHits"                   + suffix );
  iEvent.put( trkPixelHits,               prefix + "TrkPixelHits"                + suffix );
  iEvent.put( segmentMatches,             prefix + "SegmentMatches"              + suffix );
  iEvent.put( stationMatches,             prefix + "StationMatches"              + suffix );
  iEvent.put( trkValidFractionOfHits,     prefix + "TrkValidFractionOfHits"      + suffix );
  iEvent.put( trkD0,                      prefix + "TrkD0"                       + suffix );
  iEvent.put( trkD0Error,                 prefix + "TrkD0Error"                  + suffix );
  iEvent.put( trkDz,                      prefix + "TrkDz"                       + suffix );
  iEvent.put( trkDzError,                 prefix + "TrkDzError"                  + suffix );
  iEvent.put( trkVx,                      prefix + "TrkVx"                       + suffix );
  iEvent.put( trkVy,                      prefix + "TrkVy"                       + suffix );
  iEvent.put( trkVz,                      prefix + "TrkVz"                       + suffix );
  iEvent.put( trackChi2,                  prefix + "TrackChi2"                   + suffix );
  iEvent.put( globalChi2,                 prefix + "GlobalChi2"                  + suffix );
  iEvent.put( trkIso,                     prefix + "TrkIso"                      + suffix );
  iEvent.put( trackerIsoSumPT,            prefix + "TrackerIsoSumPT"             + suffix );
  iEvent.put( ecalIso,                    prefix + "EcalIso"                     + suffix );
  iEvent.put( hcalIso,                    prefix + "HcalIso"                     + suffix );
  iEvent.put( hoIso,                      prefix + "HOIso"                       + suffix );
  iEvent.put( ecalVetoIso,                prefix + "EcalVetoIso"                 + suffix );
  iEvent.put( hcalVetoIso,                prefix + "HcalVetoIso"                 + suffix );
  iEvent.put( pfisor03chargedhadron,      prefix + "PFIsoR03ChargedHadron"       + suffix );
  iEvent.put( pfisor03chargedparticle,    prefix + "PFIsoR03ChargedParticle"     + suffix );
  iEvent.put( pfisor03neutralhadron,      prefix + "PFIsoR03NeutralHadron"       + suffix );
  iEvent.put( pfisor03photon,             prefix + "PFIsoR03Photon"              + suffix );
  iEvent.put( pfisor03neutralhadronht,    prefix + "PFIsoR03NeutralHadronHT"     + suffix );
  iEvent.put( pfisor03photonht,           prefix + "PFIsoR03PhotonHT"            + suffix );
  iEvent.put( pfisor03pu,                 prefix + "PFIsoR03PU"                  + suffix );
  iEvent.put( pfisor04chargedhadron,      prefix + "PFIsoR04ChargedHadron"       + suffix );
  iEvent.put( pfisor04chargedparticle,    prefix + "PFIsoR04ChargedParticle"     + suffix );
  iEvent.put( pfisor04neutralhadron,      prefix + "PFIsoR04NeutralHadron"       + suffix );
  iEvent.put( pfisor04photon,             prefix + "PFIsoR04Photon"              + suffix );
  iEvent.put( pfisor04neutralhadronht,    prefix + "PFIsoR04NeutralHadronHT"     + suffix );
  iEvent.put( pfisor04photonht,           prefix + "PFIsoR04PhotonHT"            + suffix );
  iEvent.put( pfisor04pu,                 prefix + "PFIsoR04PU"                  + suffix );
  iEvent.put( passID,                     prefix + "PassID"                      + suffix );
  iEvent.put( IsGlobal,                   prefix + "IsGlobal"                    + suffix );
  iEvent.put( IsTracker,                  prefix + "IsTracker"                   + suffix );
  iEvent.put( vtxIndex,                   prefix + "VtxIndex"                    + suffix );
  iEvent.put( vtxDistXY,                  prefix + "VtxDistXY"                   + suffix );
  iEvent.put( vtxDistZ,                   prefix + "VtxDistZ"                    + suffix );
  iEvent.put( bestTrackVtxIndex,          prefix + "BestTrackVtxIndex"           + suffix );
  iEvent.put( bestTrackVtxDistXY,         prefix + "BestTrackVtxDistXY"          + suffix );
  iEvent.put( bestTrackVtxDistZ,          prefix + "BestTrackVtxDistZ"           + suffix );
  iEvent.put( primaryVertexDXY,           prefix + "PrimaryVertexDXY"            + suffix );
  iEvent.put( primaryVertexDXYError,      prefix + "PrimaryVertexDXYError"       + suffix );
  iEvent.put( beamspotDXY,                prefix + "BeamSpotDXY"                 + suffix );
  iEvent.put( beamspotDXYError,           prefix + "BeamSpotDXYError"            + suffix );
  iEvent.put( isPF,                       prefix + "IsPF"                        + suffix );
  iEvent.put( trackLayersWithMeasurement, prefix + "TrackLayersWithMeasurement"  + suffix );
  //
  
  iEvent.put( cosmicCompatibility,     prefix + "CosmicCompatibility"     + suffix );
  iEvent.put( timeCompatibility,       prefix + "TimeCompatibility"       + suffix );
  iEvent.put( backToBackCompatibility, prefix + "BackToBackCompatibility" + suffix );
  iEvent.put( overlapCompatibility,    prefix + "OverlapCompatibility"    + suffix );
}
