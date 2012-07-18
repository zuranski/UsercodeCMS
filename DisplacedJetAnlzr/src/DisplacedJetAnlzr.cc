// Package:    DisplacedJetAnlzr
// Class:      DisplacedJetAnlzr
// 

//
// Original Author:  Andrzej Zuranski
//         Created:  Thu Feb 16 09:43:08 CST 2012


// system include files
#include <memory>
#include <bitset>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Trigger
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"

//File Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

//My Data Formats
#include "MyAnalysis/DisplacedJetAnlzr/interface/exotic.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/genjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjetpair.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/trgObj.h"

//EDM Data Formats
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/ParticleFlowReco/interface/PFDisplacedVertex.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

//Transient Tracks
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

//HitPattern
#include "PhysicsTools/RecoUtils/interface/CheckHitPattern.h"

//Vertex fitter
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexSmoother.h"
#include "RecoVertex/AdaptiveVertexFit/interface/AdaptiveVertexFitter.h"
#include "RecoVertex/ConfigurableVertexReco/interface/ConfigurableVertexFitter.h"
#include "RecoVertex/ConfigurableVertexReco/interface/ConfigurableVertexReconstructor.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"

//Track Association
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorBase.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"

// Other
#include "DataFormats/Math/interface/deltaR.h"

class DisplacedJetAnlzr : public edm::EDAnalyzer {
   public:
      explicit DisplacedJetAnlzr(const edm::ParameterSet&);
      ~DisplacedJetAnlzr();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      void GetMothers(const HepMC::GenParticle *p, std::vector<std::pair<int,double> > &moms);
      void ClearEventData();
      void GetTrigObjects(const edm::Event&);
      void GetGenInfo(const edm::Event&);
      void GetEventInfo(const edm::Event&, const edm::EventSetup&);
      void LoopCaloJets(const edm::Event&);
      void LoopPFJets(const edm::Event&, const edm::EventSetup&);
      void DoVertexing(const edm::EventSetup&, pfjet &pfj, std::vector<reco::TransientTrack> disptrks);

      edm::ParameterSet vtxconfig_;
      edm::InputTag hlttag_;
      bool debugoutput,useTP;
      //ConfigurableVertexFitter vtxfitter_;
      ConfigurableVertexReconstructor vtxfitter_;
      reco::RecoToSimCollection RecoToSimColl;

      // ----------member data ---------------------------
      TTree *tree;
      int run,event,lumi;
      bool trigHT,trigHTdj,trigHTdjpt;

      int nPV,nTrks;

      // Single Jet Quantities
      std::vector<float> jpt;
      std::vector<float> jeta;
      std::vector<float> jphi;
      std::vector<float> jmass;

      std::vector<exotic> Xs;
      std::vector<genjet> gjets;
      std::vector<pfjet> pfjets;
      std::vector<pfjetpair> pfjetpairs;
      std::vector<trgObj> trg1Objs;
      std::vector<trgObj> trg2Objs;

      // global edm objects
      reco::Vertex pv;
      edm::ESHandle<TransientTrackBuilder> theB;
      CheckHitPattern checkHitPattern_;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DisplacedJetAnlzr::DisplacedJetAnlzr(const edm::ParameterSet& iConfig) : 
vtxconfig_(iConfig.getParameter<edm::ParameterSet>("vertexfitter")),
hlttag_(iConfig.getParameter<edm::InputTag>("hlttag")),
debugoutput(iConfig.getParameter<bool>("debugoutput")),
useTP(iConfig.getParameter<bool>("useTP")),
vtxfitter_(vtxconfig_) {
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   tree = fs->make<TTree>("tree","tree");

}


DisplacedJetAnlzr::~DisplacedJetAnlzr()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DisplacedJetAnlzr::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   ClearEventData();
   GetGenInfo(iEvent);
   GetEventInfo(iEvent,iSetup);
   LoopCaloJets(iEvent);
   LoopPFJets(iEvent,iSetup);

   tree->Fill();

}


void DisplacedJetAnlzr::ClearEventData(){

   trigHT=false,trigHTdj=false,trigHTdjpt=false;
   nPV = 0; nTrks = 0;
   jpt.clear();jeta.clear();jphi.clear();jmass.clear();
   Xs.clear();gjets.clear();
   pfjets.clear();pfjetpairs.clear();
   trg1Objs.clear();trg2Objs.clear();

}

void DisplacedJetAnlzr::GetEventInfo(const edm::Event& iEvent, const edm::EventSetup& iSetup){

// Run/Event/Lumi
   run = iEvent.id().run();
   event = iEvent.id().event();
   lumi = iEvent.luminosityBlock();

// Triggers

   HLTConfigProvider hltConfig;
   bool changed;
   hltConfig.init(iEvent.getRun(),iSetup,hlttag_.process(),changed);

   edm::Handle<edm::TriggerResults> hltResults;
   iEvent.getByLabel(hlttag_,hltResults);
   const std::vector< std::string > &trigNames = hltConfig.triggerNames();

   std::string mytrigNames[3] = {"HLT_HT250_v","HLT_HT250_DoubleDisplacedJet60_v","HLT_HT250_DoubleDisplacedJet60_PromptTrack_v"};

   for (size_t i=0;i<hltResults->size();i++){
        if (!hltResults->accept(i)) continue;
        if (trigNames.at(i).find(mytrigNames[0]) != std::string::npos) trigHT = true;     
        if (trigNames.at(i).find(mytrigNames[1]) != std::string::npos) trigHTdj = true;
        if (trigNames.at(i).find(mytrigNames[2]) != std::string::npos) trigHTdjpt = true;     
   }

// Vertices and tracks

   edm::Handle<reco::VertexCollection> recVtxs;
   iEvent.getByLabel("offlinePrimaryVertices", recVtxs); 
   pv = recVtxs->front();
   nPV = recVtxs->size();

   edm::Handle<edm::View<reco::Track> > generalTracks;
   iEvent.getByLabel("generalTracks",generalTracks);

   nTrks = generalTracks->size();

// TransientTrack Builder
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);

// Reco to Sim Track association
   if(!iEvent.isRealData() && useTP){
     edm::Handle<std::vector<TrackingParticle> > TPCollectionH ;
     try{
       iEvent.getByLabel(edm::InputTag("mergedtruth","MergedTrackTruth","HLT"),TPCollectionH);
       edm::ESHandle<TrackAssociatorBase> myAssociator;
       iSetup.get<TrackAssociatorRecord>().get("TrackAssociatorByHits", myAssociator);
       RecoToSimColl = myAssociator->associateRecoToSim(generalTracks,TPCollectionH,&iEvent );
     } catch (...) {;}
   }

}

void DisplacedJetAnlzr::LoopCaloJets(const edm::Event& iEvent){

// Get Calo jets
   edm::Handle<reco::CaloJetCollection> jetsh;
   iEvent.getByLabel("CaloJetSelected",jetsh);

   for(reco::CaloJetCollection::const_iterator j=jetsh->begin(); j!=jetsh->end();++j){

     jpt.push_back(j->pt());
     jeta.push_back(j->eta());
     jphi.push_back(j->phi());
     jmass.push_back(j->mass());
     
   }
}

// TODO
/*
void DisplacedJetAnlzr::GetTrigObjects(const edm::Event& iEvent){
// Trigger objects 

   edm::Handle<trigger::TriggerEvent> triggerEvent;
   iEvent.getByLabel(edm::InputTag("hltTriggerSummaryAOD","",hlttag_.process()) ,triggerEvent);

   if ( triggerEvent.isValid() ){

    const trigger::TriggerObjectCollection & triggerObjects = triggerEvent -> getObjects();
    trigger::size_type filter1_idx = triggerEvent -> filterIndex (edm::InputTag("hlt1DisplacedHT250L1FastJetL3Filter","",hlttag_.process()) ) ;   
    trigger::size_type filter2_idx = triggerEvent -> filterIndex (edm::InputTag("hlt1PFDisplacedJetsPt50","",hlttag_.process()) ) ;   
    trigger::size_type n_filters    = triggerEvent -> sizeFilters();

    if ( filter1_idx < n_filters ) {
      const trigger::Keys & triggerKeys ( triggerEvent -> filterKeys ( filter1_idx ) );
      const int nkeys = triggerKeys.size();

      for (int ikey = 0; ikey < nkeys; ++ikey ) {
	const trigger::TriggerObject& tO = triggerObjects[ triggerKeys [ ikey ] ];

	trgObj tO_;
	tO_.pt = tO.pt();
        tO_.eta = tO.eta();
        tO_.phi = tO.phi();
        tO_.energy = tO.energy();
        tO_.id = tO.id();

	trg1Objs.push_back(tO_);

        if (debugoutput){
          std::cout << "trigger 1 Object: " <<  tO.pt() << " eta: " << tO.eta() << " phi: "<< tO.phi() << std::endl;
        }
      }
    }
    if ( filter2_idx < n_filters ) {
      const trigger::Keys & triggerKeys ( triggerEvent -> filterKeys ( filter2_idx ) );
      const int nkeys = triggerKeys.size();

      for (int ikey = 0; ikey < nkeys; ++ikey ) {
	const trigger::TriggerObject& tO = triggerObjects[ triggerKeys [ ikey ] ];

	trgObj tO_;
	tO_.pt = tO.pt();
        tO_.eta = tO.eta();
        tO_.phi = tO.phi();
        tO_.energy = tO.energy();
        tO_.id = tO.id();

	trg2Objs.push_back(tO_);

        if (debugoutput){
          std::cout << "trigger 2 Object: " <<  tO.pt() << " eta: " << tO.eta() << " phi: "<< tO.phi() << std::endl;
        }
      }
    }
  }

}
*/

void DisplacedJetAnlzr::GetGenInfo(const edm::Event& iEvent){
// generator information

  if (iEvent.isRealData()) return;

  try{

  edm::Handle<edm::HepMCProduct> EvtHandle;
  iEvent.getByLabel("generator",EvtHandle);

  //get HepMC event
  const HepMC::GenEvent* Evt = EvtHandle->GetEvent();

  for(HepMC::GenEvent::particle_const_iterator p = Evt->particles_begin(); p != Evt->particles_end(); ++p){
    if((abs((*p)->pdg_id()) == 6000111 || abs((*p)->pdg_id()) == 6000112 ) && (*p)->status()==3){ // Exotics found

      exotic X;
      HepMC::GenParticle *exo = *p;
      HepMC::GenVertex *Xvtx = exo->end_vertex();

      reco::Candidate::LorentzVector exop4( exo->momentum() );
      X.pt = exop4.pt();
      X.phi = exop4.phi();
      X.eta = exop4.eta();
      X.mass = exop4.mass();

      for(HepMC::GenVertex::particles_out_const_iterator pout = Xvtx->particles_out_const_begin(); pout != Xvtx->particles_out_const_end(); pout++){
        if ((*pout)->pdg_id()>6) continue;
 
        genjet gj;
        HepMC::GenParticle *q = *pout;

        reco::Candidate::LorentzVector qp4(q->momentum());
        gj.pt = qp4.pt();
        gj.phi = qp4.phi();
        gj.eta = qp4.eta();
        reco::Candidate::LorentzVector qx4(q->end_vertex()->position());
        double lxy = qx4.Pt();
        gj.lxy = lxy;
        X.lxy = lxy;
        X.ctau = qx4.P()*exop4.mass()/exop4.P();

        if (debugoutput)
          std::cout << "Lxy: " << gj.lxy/10. << " pt: " << gj.pt << " eta: " << gj.eta << " phi: " << gj.phi << std::endl;

        gjets.push_back(gj);
      }

      Xs.push_back(X);
    }

  }

  } catch (...) {;}
  
}

void DisplacedJetAnlzr::DoVertexing(const edm::EventSetup& iSetup, pfjet &pfj, std::vector<reco::TransientTrack> disptrks){

  
  if (disptrks.size()<2) return;

  std::vector<TransientVertex> jvtxs = vtxfitter_.vertices(disptrks);

  for (unsigned int i=0;i<jvtxs.size();i++){

    if (!jvtxs[i].isValid()) continue;
    if (jvtxs[i].normalisedChiSquared()<0.) continue;

    TransientVertex jvtx = jvtxs[i];
    reco::Vertex vtx(jvtxs[i]);

    pfj.vtxX = vtx.position().x();
    pfj.vtxY = vtx.position().y();
    pfj.vtxZ = vtx.position().z();

    ROOT::Math::SVector<double,3> vector(vtx.position().x() - pv.x(),vtx.position().y()-pv.y(),0);
    double lxy = ROOT::Math::Mag(vector);
    reco::Candidate::CovarianceMatrix matrix = vtx.covariance() + pv.covariance();
    double err = sqrt(ROOT::Math::Similarity(matrix,vector))/lxy;
    double sig = lxy/err;
    int n=0;
    int charge=0;

    ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> > p4TrkSum;
    for (size_t i=0;i<disptrks.size();i++){
      reco::TransientTrack t_trk = disptrks.at(i);
      GlobalVector p3 = t_trk.trajectoryStateClosestToPoint(jvtx.position()).momentum();

      // update track parameters after succesful vtx fit
      pfj.disptracks.at(i).vtxpt = p3.perp();
      pfj.disptracks.at(i).vtxeta = p3.eta();
      pfj.disptracks.at(i).vtxphi = p3.phi();
      pfj.disptracks.at(i).vtxweight = jvtx.trackWeight(t_trk);

      if (jvtx.trackWeight(t_trk)>0.5){
        p4TrkSum += ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> >(p3.x(),p3.y(),p3.z(),0.1396);
        n+=1;
        charge+=t_trk.track().charge();
      }

      // hitPattern
      CheckHitPattern::Result res = checkHitPattern_.analyze(iSetup,t_trk.track(),jvtx.vertexState());
      pfj.disptracks.at(i).nHitsInFrontOfVert = res.hitsInFrontOfVert;
      pfj.disptracks.at(i).nMissHitsAfterVert = res.missHitsAfterVert;

    }

   
    float dR = deltaR(pfj.eta,pfj.phi,p4TrkSum.eta(),p4TrkSum.phi());
    pfj.vtxchi2 = jvtx.normalisedChiSquared();
    pfj.vtxmass = p4TrkSum.M();
    pfj.vtxpt = p4TrkSum.Pt();
    pfj.vtxdR = dR;
    pfj.vtxN = n;
    pfj.vtxCharge = charge;
    pfj.lxy = lxy;
    pfj.lxysig = sig;

    if (debugoutput){
      
      for (size_t i=0;i<pfj.disptracks.size();i++){
        track t = pfj.disptracks.at(i);
           std::cout << "track pt: " << t.pt 
           //<< " algo: " << t.algo 
           << " ip2d: " << t.ip2d
           << " weight: " << t.vtxweight 
           //<< " pdgid: " << t.pdgid
           //<< " exo: " << t.exo
           << " lxy: " << t.lxy
           << " NbefVtx: " << t.nHitsInFrontOfVert
           << " NMissAftVtx: " << t.nMissHitsAfterVert
           << " guesslxy:  " << t.guesslxy << std::endl;  
       }
       
       std::cout << "chi2: " << pfj.vtxchi2 
       << " vtxmass: " << pfj.vtxmass 
       << " pt: " << pfj.vtxpt 
       << " lxy: " << pfj.lxy 
       << " nTrks: " << n
       << " charge: " << charge
       << " dR: " << dR
       << " mass " << pfj.mass
       << " truelxy: " << pfj.truelxy
       << " promptEfrac " << pfj.PromptEnergyFrac << std::endl; 
    }

    // pick only the first vertex
    break;

  }

}


void DisplacedJetAnlzr::LoopPFJets(const edm::Event& iEvent, const edm::EventSetup& iSetup){

   edm::Handle<reco::PFJetCollection> pfjetsh;
   iEvent.getByLabel("PFJetSelected",pfjetsh);

   std::vector<std::vector<reco::TransientTrack> > PFJetDispTracks;
   std::vector<reco::PFJet> PFJetDisp;

   for (reco::PFJetCollection::const_iterator j = pfjetsh->begin(); j != pfjetsh->end();++j){

     pfjet pfj;

     pfj.energy = j->energy();
     pfj.pt = j->pt();
     pfj.eta = j->eta();
     pfj.phi = j->phi();
     pfj.mass = j->mass();
     pfj.truelxy = -1;

     float dR=999.;
     float lxy = -1.; 
     for (size_t i=0;i<gjets.size();i++){
       double dRcurrent = deltaR(pfj.eta,pfj.phi,gjets.at(i).eta,gjets.at(i).phi);
       if (dRcurrent < dR ){
         dR = dRcurrent;
         lxy = gjets.at(i).lxy/10.;
       }
     }
     if (dR<0.35) pfj.truelxy = lxy;

     pfj.chgHadFrac = j->chargedHadronEnergyFraction();
     pfj.chgHadN = j->chargedHadronMultiplicity();
     pfj.neuHadFrac = j->neutralHadronEnergyFraction();
     pfj.neuHadN = j->neutralMultiplicity();
     pfj.phFrac = j->photonEnergyFraction();
     pfj.phN = j->photonMultiplicity();
     pfj.eleFrac = j->electronEnergyFraction();
     pfj.eleN = j->electronMultiplicity();
     pfj.muFrac = j->muonEnergyFraction();
     pfj.muN = j->muonMultiplicity();

     GlobalVector direction(j->px(), j->py(), j->pz());
     direction = direction.unit();

     reco::TrackRefVector jtrks = j->getTrackRefs();
     std::vector<reco::TransientTrack> disptrks;
     std::vector<track> tracks_;

     // a la HLT variables:
     int nPromptTracks = 0;
     double PromptEnergy = 0.;

     // track selection before vertexing

     for (size_t i=0;i<jtrks.size();i++){
	
	const reco::Track *trk = jtrks[i].get();

	if(!jtrks[i]->quality(reco::TrackBase::highPurity)) continue;
        if (jtrks[i]->pt() < 1.) continue;

        reco::TransientTrack t_trk = theB->build(*jtrks[i].get());
        Measurement1D ip2d = IPTools::signedTransverseImpactParameter(t_trk,direction,pv).second;
        Measurement1D ip3d = IPTools::signedImpactParameter3D(t_trk,direction,pv).second;

        if (fabs(ip2d.value())<0.05){ 
          nPromptTracks += 1; 
          PromptEnergy += sqrt(0.1396*0.1396 + trk->p()*trk->p());
          continue;
        }

	double dphi = trk->phi() - j->phi();
	double r = 100*3.3*trk->pt()/3.8;
	double guesslxy = ip2d.value()/sin(dphi)*(1-2.5*fabs(ip2d.value())/r);

        track track_;

        track_.pt = trk->pt();
        track_.eta = trk->eta();
	track_.phi = trk->phi();
	track_.chi2 = trk->normalizedChi2();
	track_.nHits = trk->numberOfValidHits();
	track_.nPixHits = trk->hitPattern().numberOfValidPixelHits();
	track_.algo = trk->algo();
	track_.charge = trk->charge();

	track_.guesslxy = guesslxy;
	track_.ip2d = ip2d.value();
	track_.ip2dsig = ip2d.significance();
	track_.ip3d = ip3d.value();
	track_.ip3dsig = ip3d.significance();
	track_.vtxpt = -1;
	track_.vtxeta = -1;
	track_.vtxphi = -1;
	track_.vtxweight = -1;
        track_.vlxy = -1;
        track_.lxy = -1;
	track_.pdgid = 0;
        track_.momid = 0;
	track_.exo = 0;
	track_.nHitsInFrontOfVert = -1;
	track_.nMissHitsAfterVert = -1;


	// Track Truth
        edm::RefToBase<reco::Track> ref_trk(jtrks[i]); 
        if(RecoToSimColl.find(ref_trk) != RecoToSimColl.end()){
          TrackingParticleRef tp = RecoToSimColl[ref_trk].begin()->first;
	 
	  if (tp->genParticle().size()>0){
	    std::vector<std::pair<int,double> > moms;
  	    const HepMC::GenParticle *gp = tp->genParticle().at(0).get();
	    moms.push_back(std::pair<int,double> (gp->pdg_id(),gp->production_vertex()->position().perp()));
	    GetMothers(gp,moms);
	    track_.pdgid = moms.front().first;
            track_.lxy = moms.front().second/10.;
            track_.momid = moms.at(1).first;
	    if (moms.back().first == 6000111 || moms.back().first==6000112)
	      track_.exo = moms.back().first;
          }
          const TrackingVertex  *tv = tp->parentVertex().get();
	  ROOT::Math::SVector<double,3> vector(tv->position().x() - pv.x(),tv->position().y()-pv.y(),0);
          track_.vlxy = ROOT::Math::Mag(vector); 
        }

        tracks_.push_back(track_);
        disptrks.push_back(t_trk);
     }

//!!!!!!!!!!!!!! temporary
//     if (nPromptTracks>=5) continue;
//     if (PromptEnergy/pfj.energy>0.2) continue;
//!!!!!!!!!!!!!!

     // a la HLT variables
     pfj.nPrompt = nPromptTracks;
     pfj.PromptEnergyFrac = PromptEnergy/pfj.energy;
     pfj.nDispTracks = disptrks.size();

     // unless Vtx failes..  
     pfj.vtxchi2 = -1;
     pfj.vtxmass = -1;
     pfj.vtxpt = -1;
     pfj.vtxdR = -1;
     pfj.vtxCharge = -999;
     pfj.vtxN = -1;
     pfj.lxy = -1;
     pfj.lxysig = -1;

     pfj.disptracks = tracks_;
     pfjets.push_back(pfj);
     PFJetDispTracks.push_back(disptrks);
     PFJetDisp.push_back(*j);

  }

  // single candidates
  for (unsigned int i=0;i<pfjets.size();i++){
    DoVertexing(iSetup,pfjets.at(i),PFJetDispTracks.at(i));
  }

std::cout << std::endl;
std::cout << std::endl;

  // double candidates
  if (pfjets.size()>1){
     for (size_t i=0;i<pfjets.size()-1;i++){
       for (size_t j=i+1;j<pfjets.size();j++){

         reco::PFJet j1 = PFJetDisp.at(i);
         reco::PFJet j2 = PFJetDisp.at(j);
         pfjet pfj1 = pfjets.at(i);
         pfjet pfj2 = pfjets.at(j);

         std::vector<reco::TransientTrack> disptrks = PFJetDispTracks.at(i);
         std::vector<reco::TransientTrack> disptrks2 = PFJetDispTracks.at(j);
         disptrks.insert(disptrks.end(),disptrks2.begin(),disptrks2.end());

         std::vector<track> tracks_ = pfj1.disptracks;
         std::vector<track> tracks2_ = pfj2.disptracks;
	 tracks_.insert(tracks_.end(),tracks2_.begin(),tracks2_.end());
	 pfjetpair pfj;

         pfj.chgHadN = pfj1.chgHadN + pfj2.chgHadN;
         pfj.neuHadN = pfj1.neuHadN + pfj2.neuHadN;
	 pfj.muN = pfj1.muN + pfj2.muN;
	 pfj.eleN = pfj1.eleN + pfj2.eleN;
	 pfj.phN = pfj1.phN + pfj2.phN;
         
         pfj.idx1 = i;
         pfj.idx2 = j;

         pfj.chgHadFrac = (pfj1.chgHadFrac*pfj1.energy + pfj2.chgHadFrac*pfj2.energy)/(pfj1.energy+pfj2.energy);
         pfj.neuHadFrac = (pfj1.neuHadFrac*pfj1.energy + pfj2.neuHadFrac*pfj2.energy)/(pfj1.energy+pfj2.energy);
         pfj.muFrac = (pfj1.muFrac*pfj1.energy + pfj2.muFrac*pfj2.energy)/(pfj1.energy+pfj2.energy);
         pfj.eleFrac = (pfj1.eleFrac*pfj1.energy + pfj2.eleFrac*pfj2.energy)/(pfj1.energy+pfj2.energy);
         pfj.phFrac = (pfj1.phFrac*pfj1.energy + pfj2.phFrac*pfj2.energy)/(pfj1.energy+pfj2.energy);

         reco::Candidate::LorentzVector p4 = j1.p4() + j2.p4();
         pfj.energy = pfj1.energy + pfj2.energy;
         pfj.pt = p4.pt();
         pfj.eta = p4.eta();
         pfj.phi = p4.phi();
         pfj.mass = p4.mass();

	 GlobalVector direction(p4.px(), p4.py(), p4.pz());
         direction = direction.unit();

	 for (unsigned int i=0;i<tracks_.size();i++){

	   Measurement1D ip2d = IPTools::signedTransverseImpactParameter(disptrks.at(i),direction,pv).second;	 
           Measurement1D ip3d = IPTools::signedImpactParameter3D(disptrks.at(i),direction,pv).second;
	   tracks_.at(i).ip2d = ip2d.value();
	   tracks_.at(i).ip2dsig = ip2d.significance();
	   tracks_.at(i).ip3d = ip3d.value();
	   tracks_.at(i).ip3dsig = ip3d.significance();
	   track t = tracks_.at(i);
	   double dphi = t.phi - p4.phi();
           double r = 100*3.3*t.pt/3.8;
           tracks_.at(i).guesslxy = t.ip2d/sin(dphi)*(1-2.5*fabs(t.ip2d)/r);
 
         }

         // a la HLT variables
         pfj.nPrompt = pfj1.nPrompt + pfj2.nPrompt;
         pfj.PromptEnergyFrac = (pfj1.PromptEnergyFrac*pfj1.energy + pfj2.PromptEnergyFrac*pfj2.energy)/pfj.energy;
         pfj.nDispTracks = disptrks.size();

         pfj.vtxchi2 = -1;
         pfj.vtxmass = -1;
         pfj.vtxpt = -1;
         pfj.vtxdR = -1;
         pfj.vtxCharge = -999;
         pfj.vtxN = -1;
         pfj.lxy = -1;
         pfj.lxysig = -1;

         pfj.truelxy = -1.;
         if (pfj1.truelxy == pfj2.truelxy) 
           pfj.truelxy = pfj1.truelxy;

         pfj.disptracks=tracks_;
         DoVertexing(iSetup,pfj,disptrks);
         pfjetpairs.push_back(pfj);
       }
     }
   }

}


void DisplacedJetAnlzr::GetMothers(const HepMC::GenParticle *gp, std::vector<std::pair<int,double> > &moms){

   HepMC::GenVertex *gv = gp->production_vertex();
   if(gv != 0 ){
     for(HepMC::GenVertex::particles_in_const_iterator mom = gv->particles_in_const_begin(); mom != gv->particles_in_const_end(); mom++){
	  moms.push_back(std::pair<int,double> ( (*mom)->pdg_id(), gv->position().perp() ));
          if (moms.back().first == 6000111 || moms.back().first == 6000112)
            return;
          GetMothers(*mom,moms);
	  break;
     }
   }      
   return ;
}

// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedJetAnlzr::beginJob()
{

tree->Branch("run",&run,"run/I");
tree->Branch("event",&event,"event/I");
tree->Branch("lumi",&lumi,"lumi/I");

tree->Branch("trigHT",&trigHT,"trigHT/O");
tree->Branch("trigHTdj",&trigHTdj,"trigHTdj/O");
tree->Branch("trigHTdjpt",&trigHTdjpt,"trigHTdjpt/O");

tree->Branch("nPV",&nPV,"nPV/I");
tree->Branch("nTrks",&nTrks,"nTrks/I");

tree->Branch("jpt",&jpt);
tree->Branch("jeta",&jeta);
tree->Branch("jphi",&jphi);
tree->Branch("jmass",&jmass);

tree->Branch("Xs",&Xs);
tree->Branch("gjets",&gjets);
tree->Branch("pfjets",&pfjets);
tree->Branch("pfjetpairs",&pfjetpairs);
tree->Branch("trg1Objs",&trg1Objs);
tree->Branch("trg2Objs",&trg2Objs);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
DisplacedJetAnlzr::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
DisplacedJetAnlzr::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DisplacedJetAnlzr::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
DisplacedJetAnlzr::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending to processes a luminosity block  ------------
void
DisplacedJetAnlzr::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DisplacedJetAnlzr::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedJetAnlzr);
