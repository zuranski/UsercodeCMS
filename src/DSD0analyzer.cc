//class DSD0Analyzer DSD0Analyzer.cc Analysis/DSD0Analyzer/src/DSD0Analyzer.cc
// Original Author:  Andrzej Zuranski,Address unknown,NONE,
//         Created:  Fri Dec 11 13:59:16 EST 2009

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Common/interface/EDProduct.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/Vector.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNames.h"
#include <TString.h>

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <iostream>
#include "TMath.h"
#include "TTree.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "RecoVertex/KalmanVertexFit/interface/SingleTrackVertexConstraint.h"

//GEN MC Matching
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"


class DSD0Analyzer : public edm::EDAnalyzer {
   public:
      explicit DSD0Analyzer(const edm::ParameterSet&);
      ~DSD0Analyzer();

   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      void printGenInfo(const edm::Event& iEvent);
      void loopKpi(const edm::Event& iEvent, const edm::EventSetup&, const reco::Vertex& RecVtx);
      void loopK3pi(const edm::Event& iEvent,const edm::EventSetup&, const reco::Vertex& RecVtx);
      void assignStableDaughters(const reco::Candidate* p, std::vector<int> & pids);
      void initialize();
      // ----------member data ---------------------------
      bool doGen, doK3pi, doKpi;
      double m_pi, m_K;
      std::vector<int> dScandsKpi;
      std::vector<int> dScandsK3pi;
      std::vector<reco::TransientTrack*> goodTracks;
      std::vector<reco::TransientTrack*> slowPiTracks;
      std::vector<reco::TransientTrack> t_tks;
      TTree *tree1,*tree2;
      

      //ntuple variables
      int NKpiCand,NK3piCand,trigflag[160],NKpiMC,NK3piMC;
       
      //run, event, lumi section
      int run_n,event_n,lumi;
 
      //Kpi & K3pi D0 D* vector vars
      std::vector<double> D0MassKpi,DSMassKpi,D0VtxProb,D0PtKpi,DSPtKpi,D0VtxPosx,D0VtxPosy,D0VtxPosz,D0Vtxerrx,D0Vtxerry;
      std::vector<double> D0Vtxerrz,D0etaKpi,D0phiKpi,DSetaKpi,DSphiKpi,D0MassK3pi1,DSMassK3pi1,D0VtxProb3,D0PtK3pi,DSPtK3pi;
      std::vector<double> D0VtxPosx3,D0VtxPosy3,D0VtxPosz3,D0Vtxerrx3,D0Vtxerry3,D0Vtxerrz3,D0etaK3pi,D0phiK3pi;
      std::vector<double> DSetaK3pi,DSphiK3pi,D0MassK3pi2,DSMassK3pi2;

      //primarty vtx vars
      double PVx,PVy,PVz,PVerrx,PVerry,PVerrz;
      double BSx,BSy,BSz,BSerrx,BSerry,BSerrz;
      //tracks
      int ntracks;

      //Kpi tracks vars
      std::vector<double> KpiTrkKnhits,KpiTrkpinhits,KpiTrkSnhits;
      std::vector<double> KpiTrkKchi2,KpiTrkpichi2,KpiTrkSchi2;
      std::vector<double> KpiTrkKpt,KpiTrkpipt,KpiTrkSpt;
      std::vector<double> KpiTrkKdxy,KpiTrkpidxy,KpiTrkSdxy;
      std::vector<double> KpiTrkKdz,KpiTrkpidz,KpiTrkSdz;
      std::vector<double> KpiTrkKeta,KpiTrkpieta,KpiTrkSeta;
      std::vector<double> KpiTrkKphi,KpiTrkpiphi,KpiTrkSphi;
      std::vector<double> KpiDSDeltaR;
      //MC
      std::vector<double> MCDsDeltaR;
      //K3pi tracks vars
      std::vector<double> K3piTrkKnhits,K3piTrk1pinhits,K3piTrk2pinhits,K3piTrk3pinhits,K3piTrkSnhits;
      std::vector<double> K3piTrkKchi2,K3piTrk1pichi2,K3piTrk2pichi2,K3piTrk3pichi2,K3piTrkSchi2;
      std::vector<double> K3piTrkKpt,K3piTrk1pipt,K3piTrk2pipt,K3piTrk3pipt,K3piTrkSpt;
      std::vector<double> K3piTrkKdxy,K3piTrk1pidxy,K3piTrk2pidxy,K3piTrk3pidxy,K3piTrkSdxy;
      std::vector<double> K3piTrkKdz,K3piTrk1pidz,K3piTrk2pidz,K3piTrk3pidz,K3piTrkSdz;
      std::vector<double> K3piTrkKeta,K3piTrk1pieta,K3piTrk2pieta,K3piTrk3pieta,K3piTrkSeta;
      std::vector<double> K3piTrkKphi,K3piTrk1piphi,K3piTrk2piphi,K3piTrk3piphi,K3piTrkSphi;
      std::vector<double> K3piDSDeltaR;
      //MC
      std::vector<double> MCDsDeltaR3;

};

DSD0Analyzer::DSD0Analyzer(const edm::ParameterSet& iConfig):
   doGen(iConfig.getParameter<bool>("doGen")),
   doK3pi(iConfig.getParameter<bool>("doK3pi")),
   doKpi(iConfig.getParameter<bool>("doKpi"))
{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   tree1 = fs->make<TTree>("tree1","tree1");
   tree2 = fs->make<TTree>("tree2","tree2");

}

DSD0Analyzer::~DSD0Analyzer(){}

void DSD0Analyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace reco;

  m_pi=0.13957018;
  m_K=0.493677;

  //clean vectors and vars
  initialize();

  //run, event, lumi section
  run_n = iEvent.id().run();
  event_n = iEvent.id().event();
  lumi = iEvent.luminosityBlock();

  //HLT trigger
  Handle<TriggerResults>  hltresults;
  InputTag tag("TriggerResults");
  iEvent.getByLabel(tag,hltresults);

  TriggerNames triggerNames_;
  triggerNames_.init(* hltresults);

  int ntrigs = hltresults->size();
  for (int itrig = 0; itrig != ntrigs; ++itrig){
    TString trigName=triggerNames_.triggerName(itrig);
    bool accept = hltresults->accept(itrig);
    if (accept){trigflag[itrig] = 1;}
    else {trigflag[itrig] = 0;}
  }
 
  //BeamSpot
  reco::BeamSpot vertexBeamSpot;
  edm::Handle<reco::BeamSpot> recoBeamSpotHandle;
  iEvent.getByType(recoBeamSpotHandle);
  vertexBeamSpot = *recoBeamSpotHandle;

  BSx=vertexBeamSpot.x0();
  BSy=vertexBeamSpot.y0();
  BSz=vertexBeamSpot.z0();
  BSerrx=vertexBeamSpot.x0Error();
  BSerry=vertexBeamSpot.y0Error();
  BSerrz=vertexBeamSpot.z0Error();

  // Primary Vtx with most tracks
  Handle<reco::VertexCollection> recVtxs;
  iEvent.getByLabel("offlinePrimaryVertices", recVtxs); //has a BeamSpot if no vtx found;

  size_t vtx_trk_size = (*recVtxs)[0].tracksSize();
  int VtxIn=0;
  for(size_t i = 0; i < recVtxs->size(); ++ i) {
    const Vertex &vtx = (*recVtxs)[i];
    if(vtx.tracksSize()>vtx_trk_size){
      VtxIn=i;
      vtx_trk_size=vtx.tracksSize();
    }
  }
  const Vertex& RecVtx = (*recVtxs)[VtxIn];

  PVx = RecVtx.x();
  PVy = RecVtx.y();
  PVz = RecVtx.z();
  PVerrx=RecVtx.xError();
  PVerry=RecVtx.yError();
  PVerrz=RecVtx.zError();

  Handle<TrackCollection> generalTracks;
  iEvent.getByLabel("generalTracks",generalTracks);

  edm::ESHandle<TransientTrackBuilder> theB;
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);
  t_tks = (*theB).build(generalTracks);

  // track selector
  for(size_t i=0;i<t_tks.size();i++){
    TransientTrack t_trk = t_tks.at(i);
    if( fabs(t_trk.track().eta())<2.4 && 
        fabs(t_trk.track().dxy(RecVtx.position()))<1. && 
        fabs(t_trk.track().dz(RecVtx.position()))<2. &&
        t_trk.track().normalizedChi2() < 4. &&
        t_trk.track().pt() > 0.15){
      slowPiTracks.push_back(&(t_tks.at(i)));
      if( (t_trk.track().numberOfValidHits() > 3) && (t_trk.track().pt() > 0.3) ){
        goodTracks.push_back(&(t_tks.at(i)));
      }
    }
  }
  ntracks = slowPiTracks.size();

  if(doGen)
    printGenInfo(iEvent);
  if(doKpi)
    loopKpi(iEvent,iSetup,RecVtx);
  cout << "Kpi done" << endl;
  if(doK3pi)
    loopK3pi(iEvent,iSetup,RecVtx); 
  cout << "K3pi done" << endl;
 
}

void DSD0Analyzer::loopKpi(const edm::Event& iEvent, const edm::EventSetup& iSetup, const reco::Vertex& RecVtx){

  using namespace std;
  using namespace reco;
  using namespace edm;

  for(size_t i=0;i<goodTracks.size();i++){  
 
    TransientTrack* trk1 = goodTracks.at(i);

    for(size_t j=i+1;j<goodTracks.size();j++){
    
      TransientTrack* trk2 = goodTracks.at(j);

      if(trk1->charge() == trk2->charge()) continue;

      math::XYZVector D0_p = trk1->track().momentum() + trk2->track().momentum();

      if(sqrt(D0_p.perp2()) < 3.) continue;

      for(size_t k=0;k<slowPiTracks.size();k++){

        TransientTrack* trkS = slowPiTracks.at(k);

        if(*trkS == *trk1 || *trkS == *trk2) continue;

        math::XYZVector DS_p = D0_p + trkS->track().momentum();
        if(sqrt(DS_p.perp2())<4.) continue;
   
        TransientTrack *K=0,*pi=0;

        // tag the tracks
        if(trk1->charge() == trkS->charge()){
          K = trk2;
          pi = trk1;
        }
        else{
          K = trk1;
          pi = trk2;
        }

        //before vertexing do loose preselection
        math::XYZTLorentzVector ip4_K(K->track().px(),K->track().py(),K->track().pz(),sqrt(pow(K->track().p(),2)+pow(m_K,2)));
        math::XYZTLorentzVector ip4_pi(pi->track().px(),pi->track().py(),pi->track().pz(),sqrt(pow(pi->track().p(),2)+pow(m_pi,2)));        

        math::XYZTLorentzVector ip4_D0 = ip4_K + ip4_pi;
        
        if( fabs(ip4_D0.M()-1.86484)  > 0.7) continue;

        math::XYZTLorentzVector p4_S(trkS->track().px(),trkS->track().py(),trkS->track().pz(),sqrt(pow(trkS->track().p(),2)+pow(m_pi,2)));
        math::XYZTLorentzVector ip4_DS = ip4_D0 + p4_S;
        if((ip4_DS.M() - ip4_D0.M()) > 0.3) continue;

        //now the time consuming vertexing

        vector<TransientTrack> tks;
        tks.push_back(*K);
        tks.push_back(*pi);
        KalmanVertexFitter kalman(true);
        TransientVertex v = kalman.vertex(tks);
        if(!v.isValid() || !v.hasRefittedTracks()) continue;
        double vtxProb =TMath::Prob( (Double_t) v.totalChiSquared(), (Int_t) v.degreesOfFreedom());
        TransientTrack K_f = v.refittedTrack(*K);
        TransientTrack pi_f = v.refittedTrack(*pi);        


        math::XYZTLorentzVector p4_K(K_f.track().px(),K_f.track().py(),K_f.track().pz(),sqrt(pow(K_f.track().p(),2)+pow(m_K,2)));
        math::XYZTLorentzVector p4_pi(pi_f.track().px(),pi_f.track().py(),pi_f.track().pz(),sqrt(pow(pi_f.track().p(),2)+pow(m_pi,2)));

        math::XYZTLorentzVector d0_p4 = p4_K + p4_pi;
        double d0mass = d0_p4.M();
        if(fabs(d0mass - 1.86484)>0.3) continue;
   
        math::XYZTLorentzVector dS_p4 = d0_p4 + p4_S;
        double dsmass = dS_p4.M();
        if( (dsmass - d0mass) > 0.18) continue;

        if(doGen){
        
          Handle<GenParticleCollection> genParticles;
          iEvent.getByLabel("genParticles",genParticles);
        
          double dR = 99.;
 
          for(size_t i=0; i<dScandsKpi.size();i++){
            const GenParticle & ds = genParticles->at(dScandsKpi.at(i));
            double delta_R = deltaR(dS_p4.eta(),dS_p4.phi(),ds.eta(),ds.phi());
            if(delta_R < 0.15 && delta_R < dR)
              dR = delta_R;
          }

          MCDsDeltaR.push_back(dR);
        }

        D0VtxProb.push_back(vtxProb);
        D0MassKpi.push_back(d0_p4.M());
        DSMassKpi.push_back(dS_p4.M());
        D0PtKpi.push_back(d0_p4.Pt());
        DSPtKpi.push_back(dS_p4.Pt());
        D0etaKpi.push_back(d0_p4.eta());
        D0phiKpi.push_back(d0_p4.phi());
        DSetaKpi.push_back(dS_p4.eta());
        DSphiKpi.push_back(dS_p4.phi());

        D0VtxPosx.push_back(v.position().x());
        D0VtxPosy.push_back(v.position().y());
        D0VtxPosz.push_back(v.position().z());
        D0Vtxerrx.push_back(v.positionError().cxx());
        D0Vtxerry.push_back(v.positionError().cyy());
        D0Vtxerrz.push_back(v.positionError().czz());

        KpiTrkKdxy.push_back(K_f.track().dxy(RecVtx.position()));
        KpiTrkpidxy.push_back(pi_f.track().dxy(RecVtx.position()));
        KpiTrkSdxy.push_back(trkS->track().dxy(RecVtx.position()));

        KpiTrkKdz.push_back(K_f.track().dz(RecVtx.position()));
        KpiTrkpidz.push_back(pi_f.track().dz(RecVtx.position()));
        KpiTrkSdz.push_back(trkS->track().dz(RecVtx.position()));

        KpiTrkKnhits.push_back(K->track().numberOfValidHits());
        KpiTrkpinhits.push_back(pi->track().numberOfValidHits());
        KpiTrkSnhits.push_back(trkS->track().numberOfValidHits());

        KpiTrkKchi2.push_back(K->track().normalizedChi2());
        KpiTrkpichi2.push_back(pi->track().normalizedChi2());
        KpiTrkSchi2.push_back(trkS->track().normalizedChi2());

        KpiDSDeltaR.push_back(deltaR(d0_p4.eta(),d0_p4.phi(),trkS->track().eta(),trkS->track().phi()));

        KpiTrkKpt.push_back(K_f.track().pt());
        KpiTrkpipt.push_back(pi_f.track().pt());
        KpiTrkSpt.push_back(trkS->track().pt());

        KpiTrkKeta.push_back(K_f.track().eta());
        KpiTrkpieta.push_back(pi_f.track().eta());
        KpiTrkSeta.push_back(trkS->track().eta());

        KpiTrkKphi.push_back(K_f.track().phi());
        KpiTrkpiphi.push_back(pi_f.track().phi());
        KpiTrkSphi.push_back(trkS->track().phi());

        NKpiCand++;

      }
    } 
  }

  if(NKpiCand>0) 
    tree1->Fill();

}

void DSD0Analyzer::loopK3pi(const edm::Event& iEvent, const edm::EventSetup& iSetup, const reco::Vertex& RecVtx){

  using namespace std;
  using namespace reco;
  using namespace edm;

  int n1=0,n2=0,n3=0;

  for(size_t i=0;i<goodTracks.size();i++){
     
    TransientTrack* trk1 = goodTracks.at(i);

    for(size_t j=i+1;j<goodTracks.size();j++){

      TransientTrack* trk2 = goodTracks.at(j);

      for(size_t k=j+1;k<goodTracks.size();k++){

        TransientTrack* trk3 = goodTracks.at(k);
        if( fabs( trk1->charge() + trk2->charge() + trk3->charge() ) == 3. ) continue;

        for(size_t l=k+1;l<goodTracks.size();l++){

          TransientTrack* trk4 = goodTracks.at(l);

          if( (trk1->charge() + trk2->charge() + trk3->charge() + trk4->charge()) != 0) continue;

          math::XYZVector D0_p = trk1->track().momentum() + trk2->track().momentum() + trk3->track().momentum() + trk4->track().momentum();

          if(sqrt(D0_p.perp2()) < 3.) continue;

          for(size_t s=0;s<slowPiTracks.size();s++){

            TransientTrack* trkS = slowPiTracks.at(s);

            if(fabs(trkS->charge())!=1) continue;
            if(*trkS == *trk1 || *trkS == *trk2 || *trkS == *trk3 || *trkS == *trk4) continue;
  
            n1++;

            math::XYZVector DS_p = D0_p + trkS->track().momentum();
            if(sqrt(DS_p.perp2())<4.) continue;

            n2++;

            // match K and 1pi charge with -Spi charge
            TransientTrack *K=0,*pi1=0,*pi2=0,*pi3=0;
            if(trk1->charge() == trkS->charge()){ 
              pi2=trk1;
              if(trk2->charge() == trkS->charge()){
                pi3 = trk2;
                K = trk3;
                pi1 = trk4;
              }
              else{
                K = trk2;
                if(trk3->charge() == trkS->charge()){
                  pi3 = trk3;
                  pi1 = trk4;
                }
                else{
                  pi1 = trk3;
                  pi3 = trk4;
                }
              }
            }
            else{
              K=trk1;
              if(trk2->charge() == trkS->charge()){
                pi2 = trk2;
                if(trk3->charge() == trkS->charge()){
                  pi3 = trk3;
                  pi1 = trk4;
                }
                else{
                  pi1 = trk3;
                  pi3 = trk4;
                }
              }
              else{
                pi1 = trk2;
                pi2 = trk3;
                pi3 = trk4;
              }
            }

            //before vertexing do loose preselection
            math::XYZTLorentzVector ip4_K(K->track().px(),K->track().py(),K->track().pz(),sqrt(pow(K->track().p(),2)+pow(m_K,2)));
            math::XYZTLorentzVector ip4_1pi(pi1->track().px(),pi1->track().py(),pi1->track().pz(),sqrt(pow(pi1->track().p(),2)+pow(m_pi,2)));
            math::XYZTLorentzVector ip4_K_(pi1->track().px(),pi1->track().py(),pi1->track().pz(),sqrt(pow(pi1->track().p(),2)+pow(m_K,2)));
            math::XYZTLorentzVector ip4_1pi_(K->track().px(),K->track().py(),K->track().pz(),sqrt(pow(K->track().p(),2)+pow(m_pi,2)));
            math::XYZTLorentzVector ip4_2pi(pi2->track().px(),pi2->track().py(),pi2->track().pz(),sqrt(pow(pi2->track().p(),2)+pow(m_pi,2)));
            math::XYZTLorentzVector ip4_3pi(pi3->track().px(),pi3->track().py(),pi3->track().pz(),sqrt(pow(pi3->track().p(),2)+pow(m_pi,2)));            

            math::XYZTLorentzVector ip4_D0 = ip4_K + ip4_1pi + ip4_2pi + ip4_3pi;
            math::XYZTLorentzVector ip4_D0_ = ip4_K_ + ip4_1pi_ + ip4_2pi + ip4_3pi;           
 
            double md0=0;
            if(  fabs(ip4_D0.M()-1.86484) < fabs(ip4_D0_.M()-1.86484)){
              md0 = ip4_D0.M();
            }
            else {
              md0 = ip4_D0_.M();
              ip4_D0 = ip4_D0_;
            }

            if( fabs(md0-1.86484)  > 0.7) continue; 
           
            math::XYZTLorentzVector p4_S(trkS->track().px(),trkS->track().py(),trkS->track().pz(),sqrt(pow(trkS->track().p(),2)+pow(m_pi,2)));
            math::XYZTLorentzVector ip4_DS = ip4_D0 + p4_S;
            if((ip4_DS.M() - ip4_D0.M()) > 0.3) continue;

            n3++;
            // now the time consuming vertexing
            vector<TransientTrack> tks;
            tks.push_back(*K);
            tks.push_back(*pi1);
            tks.push_back(*pi2);
            tks.push_back(*pi3);
            KalmanVertexFitter kalman(true);
            TransientVertex v = kalman.vertex(tks);
            if(!v.isValid() || !v.hasRefittedTracks()) continue;
            double vtxProb = TMath::Prob( (Double_t) v.totalChiSquared(), (Int_t) v.degreesOfFreedom());
            TransientTrack K_f = v.refittedTrack(*K);
            TransientTrack pi1_f = v.refittedTrack(*pi1);
            TransientTrack pi2_f = v.refittedTrack(*pi2);
            TransientTrack pi3_f = v.refittedTrack(*pi3);

            math::XYZTLorentzVector p4_K(K_f.track().px(),K_f.track().py(),K_f.track().pz(),sqrt(pow(K_f.track().p(),2)+pow(m_K,2)));
            math::XYZTLorentzVector p4_1pi(pi1_f.track().px(),pi1_f.track().py(),pi1_f.track().pz(),sqrt(pow(pi1_f.track().p(),2)+pow(m_pi,2)));
            math::XYZTLorentzVector p4_K_(pi1_f.track().px(),pi1_f.track().py(),pi1_f.track().pz(),sqrt(pow(pi1_f.track().p(),2)+pow(m_K,2)));
            math::XYZTLorentzVector p4_1pi_(K_f.track().px(),K_f.track().py(),K_f.track().pz(),sqrt(pow(K_f.track().p(),2)+pow(m_pi,2)));
            math::XYZTLorentzVector p4_2pi(pi2_f.track().px(),pi2_f.track().py(),pi2_f.track().pz(),sqrt(pow(pi2_f.track().p(),2)+pow(m_pi,2)));
            math::XYZTLorentzVector p4_3pi(pi3_f.track().px(),pi3_f.track().py(),pi3_f.track().pz(),sqrt(pow(pi3_f.track().p(),2)+pow(m_pi,2)));


            math::XYZTLorentzVector p4_D0 = p4_K + p4_1pi + p4_2pi + p4_3pi;
            math::XYZTLorentzVector p4_D0_ = p4_K_ + p4_1pi_ + p4_2pi + p4_3pi;
 
            double d0mass1 = p4_D0.M();
            double d0mass2 = p4_D0_.M();
            double d0mass = fabs(d0mass1-1.86484)<fabs(d0mass2-1.86484) ? d0mass1 : d0mass2;
            if(fabs(d0mass - 1.86484)>0.3) continue;

            math::XYZTLorentzVector p4_DS = p4_D0 + p4_S;
            math::XYZTLorentzVector p4_DS_ = p4_D0_ + p4_S;
            double dsmass1 = p4_DS.M();
            double dsmass2 = p4_DS_.M();
            if( (dsmass1 - d0mass1) > 0.18 && (dsmass2 - d0mass2) > 0.18) continue;

            if(doGen){

              Handle<GenParticleCollection> genParticles;
              iEvent.getByLabel("genParticles",genParticles);

              double dR = 99.;

              for(size_t i=0; i<dScandsK3pi.size();i++){
                const GenParticle & ds = genParticles->at(dScandsK3pi.at(i));
                double delta_R = deltaR(p4_DS.eta(),p4_DS.phi(),ds.eta(),ds.phi());
                if(delta_R < 0.15 && delta_R < dR)
                  dR = delta_R;
              }

              MCDsDeltaR3.push_back(dR);
            }

            D0VtxProb3.push_back(vtxProb);

            D0MassK3pi1.push_back(p4_D0.M());
            DSMassK3pi1.push_back(p4_DS.M());
            D0PtK3pi.push_back(p4_D0.Pt());
            DSPtK3pi.push_back(p4_DS.Pt());
            D0etaK3pi.push_back(p4_D0.eta());
            D0phiK3pi.push_back(p4_D0.phi());
            DSetaK3pi.push_back(p4_DS.eta());
            DSphiK3pi.push_back(p4_DS.phi());

            D0MassK3pi2.push_back(p4_D0_.M());
            DSMassK3pi2.push_back(p4_DS_.M());

            D0VtxPosx3.push_back(v.position().x());
            D0VtxPosy3.push_back(v.position().y());
            D0VtxPosz3.push_back(v.position().z());
            D0Vtxerrx3.push_back(v.positionError().cxx());
            D0Vtxerry3.push_back(v.positionError().cyy());
            D0Vtxerrz3.push_back(v.positionError().czz());

            K3piTrkKdxy.push_back(K_f.track().dxy(RecVtx.position()));
            K3piTrk1pidxy.push_back(pi1_f.track().dxy(RecVtx.position()));
            K3piTrk2pidxy.push_back(pi2_f.track().dxy(RecVtx.position()));
            K3piTrk3pidxy.push_back(pi3_f.track().dxy(RecVtx.position()));
            K3piTrkSdxy.push_back(trkS->track().dxy(RecVtx.position()));

            K3piTrkKdz.push_back(K_f.track().dz(RecVtx.position()));
            K3piTrk1pidz.push_back(pi1_f.track().dz(RecVtx.position()));
            K3piTrk2pidz.push_back(pi2_f.track().dz(RecVtx.position()));
            K3piTrk3pidz.push_back(pi3_f.track().dz(RecVtx.position()));
            K3piTrkSdz.push_back(trkS->track().dz(RecVtx.position()));

            K3piTrkKnhits.push_back(K->track().numberOfValidHits());
            K3piTrk1pinhits.push_back(pi1->track().numberOfValidHits());
            K3piTrk2pinhits.push_back(pi2->track().numberOfValidHits());
            K3piTrk3pinhits.push_back(pi3->track().numberOfValidHits());
            K3piTrkSnhits.push_back(trkS->track().numberOfValidHits());

            K3piTrkKchi2.push_back(K->track().normalizedChi2());
            K3piTrk1pichi2.push_back(pi1->track().normalizedChi2());
            K3piTrk2pichi2.push_back(pi2->track().normalizedChi2());
            K3piTrk3pichi2.push_back(pi3->track().normalizedChi2());
            K3piTrkSchi2.push_back(trkS->track().normalizedChi2());

            K3piDSDeltaR.push_back(deltaR(p4_D0.eta(),p4_D0.phi(),trkS->track().eta(),trkS->track().phi()));

            K3piTrkKpt.push_back(K_f.track().pt());
            K3piTrk1pipt.push_back(pi1_f.track().pt());
            K3piTrk2pipt.push_back(pi2_f.track().pt());
            K3piTrk3pipt.push_back(pi3_f.track().pt());
            K3piTrkSpt.push_back(trkS->track().pt());

            K3piTrkKeta.push_back(K_f.track().eta());
            K3piTrk1pieta.push_back(pi1_f.track().eta());
            K3piTrk2pieta.push_back(pi2_f.track().eta());
            K3piTrk3pieta.push_back(pi3_f.track().eta());
            K3piTrkSeta.push_back(trkS->track().eta());

            K3piTrkKphi.push_back(K_f.track().phi());
            K3piTrk1piphi.push_back(pi1_f.track().phi());
            K3piTrk2piphi.push_back(pi2_f.track().phi());
            K3piTrk3piphi.push_back(pi3_f.track().phi());
            K3piTrkSphi.push_back(trkS->track().phi());

            NK3piCand++; 



          }
        }
      }
    }
  }

  if(NK3piCand>0)
    tree2->Fill();

}

void DSD0Analyzer::assignStableDaughters(const reco::Candidate* p, std::vector<int> & pids){

  for(size_t i=0;i<p->numberOfDaughters();i++){
    if(p->daughter(i)->status()==1)
      pids.push_back(abs(p->daughter(i)->pdgId()));
    else
     assignStableDaughters(p->daughter(i),pids);
  }
  return;
}


void DSD0Analyzer::printGenInfo(const edm::Event& iEvent){

  using namespace std;
  using namespace reco;
  using namespace edm;

  Handle<GenParticleCollection> genParticles;
  iEvent.getByLabel("genParticles",genParticles);

  for(size_t i=0;i<genParticles->size();i++){

    const GenParticle & p = (*genParticles)[i];

    if(fabs(p.pdgId())==413){ //D*

      for(size_t j=0;j<p.numberOfDaughters();j++){

        const Candidate* dau = p.daughter(j);

        if(fabs(dau->pdgId())==421){

          std::vector<int> d0dauspids;
          assignStableDaughters(dau,d0dauspids);
          int K_num=0,pi_num=0,ndau=d0dauspids.size();  

          while (!d0dauspids.empty()){
            int pid = d0dauspids.back();
            if(pid==321)
              K_num++;
            if(pid==211)
              pi_num++;
            d0dauspids.pop_back();
          }
 
          if(K_num==1 && pi_num==1 && ndau==2){
            dScandsKpi.push_back(i);
          }
          if(K_num==1 && pi_num==3 && ndau==4){
            dScandsK3pi.push_back(i);
          }
        }
      }
    }
  }
  NKpiMC=dScandsKpi.size();
  NK3piMC=dScandsK3pi.size();

}

void DSD0Analyzer::initialize(){
//clearing the vectors
  //analysis
  dScandsKpi.clear();  dScandsK3pi.clear();  goodTracks.clear(); slowPiTracks.clear();
  //Kpi D* D0
  D0MassKpi.clear();  DSMassKpi.clear();  D0VtxProb.clear();  D0PtKpi.clear();  DSPtKpi.clear();  D0VtxPosx.clear();
  D0VtxPosy.clear();  D0VtxPosz.clear();  D0etaKpi.clear();  D0phiKpi.clear();  D0Vtxerrx.clear();  D0Vtxerry.clear();
  D0Vtxerrz.clear();  DSetaKpi.clear(); DSphiKpi.clear();
  //K3pi D* D0
  D0MassK3pi1.clear();  DSMassK3pi1.clear();  D0VtxProb3.clear();  D0PtK3pi.clear();  DSPtK3pi.clear();  D0VtxPosx3.clear();
  D0VtxPosy3.clear();  D0VtxPosz3.clear();  D0etaK3pi.clear();  D0phiK3pi.clear();  D0Vtxerrx3.clear();  D0Vtxerry3.clear(); 
  D0Vtxerrz3.clear(); DSetaK3pi.clear(); DSphiK3pi.clear();
  D0MassK3pi2.clear(); DSMassK3pi2.clear();
  //Kpi tracks
  KpiTrkKdxy.clear();  KpiTrkpidxy.clear();  KpiTrkSdxy.clear();
  KpiTrkKdz.clear();  KpiTrkpidz.clear();  KpiTrkSdz.clear();
  KpiTrkKpt.clear();  KpiTrkpipt.clear();  KpiTrkSpt.clear();
  KpiTrkKchi2.clear();  KpiTrkpichi2.clear();  KpiTrkSchi2.clear();
  KpiTrkKnhits.clear();  KpiTrkpinhits.clear();  KpiTrkSnhits.clear();
  KpiTrkKeta.clear();  KpiTrkpieta.clear();  KpiTrkSeta.clear();
  KpiTrkKphi.clear();  KpiTrkpiphi.clear();  KpiTrkSphi.clear();
  KpiDSDeltaR.clear(); 
  //MC
  MCDsDeltaR.clear();MCDsDeltaR3.clear();

  //K3pi tracks
  K3piTrkKdxy.clear();  K3piTrk1pidxy.clear();  K3piTrk2pidxy.clear();  K3piTrk3pidxy.clear();  K3piTrkSdxy.clear();
  K3piTrkKdz.clear();  K3piTrk1pidz.clear();  K3piTrk2pidz.clear();  K3piTrk3pidz.clear();  K3piTrkSdz.clear();
  K3piTrkKpt.clear();  K3piTrk1pipt.clear();  K3piTrk2pipt.clear();  K3piTrk3pipt.clear();  K3piTrkSpt.clear();
  K3piTrkKchi2.clear();  K3piTrk1pichi2.clear();  K3piTrk2pichi2.clear();  K3piTrk3pichi2.clear();  K3piTrkSchi2.clear();
  K3piTrkKnhits.clear();  K3piTrk1pinhits.clear();  K3piTrk2pinhits.clear();  K3piTrk3pinhits.clear();
  K3piTrkSnhits.clear();
  K3piTrkKeta.clear();  K3piTrk1pieta.clear();  K3piTrk2pieta.clear();  K3piTrk3pieta.clear();  K3piTrkSeta.clear();
  K3piTrkKphi.clear();  K3piTrk1piphi.clear();  K3piTrk2piphi.clear();  K3piTrk3piphi.clear();  K3piTrkSphi.clear();
  K3piDSDeltaR.clear(); 
  //MC ids
  //static variables
  for(int i=0;i<160;i++)
    trigflag[i]=0;
  PVx = PVy = PVz = PVerrx = PVerry = PVerrz = -99.;
  BSx = BSy = BSz = BSerrx = BSerry = BSerrz = -99.;
  ntracks = -99,NKpiCand=0,NK3piCand=0,NKpiMC=0,NK3piMC=0,run_n=0,event_n=0,lumi=0;
}

void DSD0Analyzer::beginJob()
{
tree1->Branch("trigflag",&trigflag,"trigflag[160]/I");
tree2->Branch("trigflag",&trigflag,"trigflag[160]/I");
tree1->Branch("NKpiCand",&NKpiCand,"NKpiCand/I");
tree1->Branch("NKpiMC",&NKpiMC,"NKpiMC/I");
tree2->Branch("NK3piCand",&NK3piCand,"NK3piCand/I");
tree2->Branch("NK3piMC",&NK3piMC,"NK3piMC/I");

tree1->Branch("run_n",&run_n,"run_n/I");
tree1->Branch("event_n",&event_n,"event_n/I");
tree1->Branch("lumi",&lumi,"lumi/I");

tree2->Branch("run_n",&run_n,"run_n/I");
tree2->Branch("event_n",&event_n,"event_n/I");
tree2->Branch("lumi",&lumi,"lumi/I");

tree1->Branch("D0MassKpi",&D0MassKpi);
tree1->Branch("DSMassKpi",&DSMassKpi);
tree1->Branch("D0VtxProb",&D0VtxProb);
tree1->Branch("D0VtxPosx",&D0VtxPosx);
tree1->Branch("D0VtxPosy",&D0VtxPosy);
tree1->Branch("D0VtxPosz",&D0VtxPosz);
tree1->Branch("D0Vtxerrx",&D0Vtxerrx);
tree1->Branch("D0Vtxerry",&D0Vtxerry);
tree1->Branch("D0Vtxerrz",&D0Vtxerrz);
tree1->Branch("D0etaKpi",&D0etaKpi);
tree1->Branch("D0phiKpi",&D0phiKpi);
tree1->Branch("DSetaKpi",&DSetaKpi);
tree1->Branch("DSphiKpi",&DSphiKpi);

tree2->Branch("D0MassK3pi1",&D0MassK3pi1);
tree2->Branch("DSMassK3pi1",&DSMassK3pi1);
tree2->Branch("D0MassK3pi2",&D0MassK3pi2);
tree2->Branch("DSMassK3pi2",&DSMassK3pi2);
tree2->Branch("D0VtxProb3",&D0VtxProb3);
tree2->Branch("D0VtxPosx3",&D0VtxPosx3);
tree2->Branch("D0VtxPosy3",&D0VtxPosy3);
tree2->Branch("D0VtxPosz3",&D0VtxPosz3);
tree2->Branch("D0Vtxerrx3",&D0Vtxerrx3);
tree2->Branch("D0Vtxerry3",&D0Vtxerry3);
tree2->Branch("D0Vtxerrz3",&D0Vtxerrz3);
tree2->Branch("D0etaK3pi",&D0etaK3pi);
tree2->Branch("D0phiK3pi",&D0phiK3pi);
tree2->Branch("DSetaK3pi",&DSetaK3pi);
tree2->Branch("DSphiK3pi",&DSphiK3pi);

//tracks
tree1->Branch("ntracks",&ntracks,"ntracks/I");
tree2->Branch("ntracks",&ntracks,"ntracks/I");
//primary vertex
tree1->Branch("PVx",&PVx,"PVx/D");
tree1->Branch("PVy",&PVy,"PVy/D");
tree1->Branch("PVz",&PVz,"PVz/D");
tree1->Branch("PVerrx",&PVerrx,"PVerrx/D");
tree1->Branch("PVerry",&PVerry,"PVerry/D");
tree1->Branch("PVerrz",&PVerrz,"PVerrz/D");
tree1->Branch("BSx",&BSx,"BSx/D");
tree1->Branch("BSy",&BSy,"BSy/D");
tree1->Branch("BSz",&BSz,"BSz/D");
tree1->Branch("BSerrx",&BSerrx,"BSerrx/D");
tree1->Branch("BSerry",&BSerry,"BSerry/D");
tree1->Branch("BSerrz",&BSerrz,"BSerrz/D");

tree2->Branch("PVx",&PVx,"PVx/D");
tree2->Branch("PVy",&PVy,"PVy/D");
tree2->Branch("PVz",&PVz,"PVz/D");
tree2->Branch("PVerrx",&PVerrx,"PVerrx/D");
tree2->Branch("PVerry",&PVerry,"PVerry/D");
tree2->Branch("PVerrz",&PVerrz,"PVerrz/D");
tree2->Branch("BSx",&BSx,"BSx/D");
tree2->Branch("BSy",&BSy,"BSy/D");
tree2->Branch("BSz",&BSz,"BSz/D");
tree2->Branch("BSerrx",&BSerrx,"BSerrx/D");
tree2->Branch("BSerry",&BSerry,"BSerry/D");
tree2->Branch("BSerrz",&BSerrz,"BSerrz/D");
//Kpi tracks vars
tree1->Branch("KpiTrkKpt",&KpiTrkKpt);
tree1->Branch("KpiTrkpipt",&KpiTrkpipt);
tree1->Branch("KpiTrkSpt",&KpiTrkSpt);
tree1->Branch("D0PtKpi",&D0PtKpi);
tree1->Branch("DSPtKpi",&DSPtKpi);
tree1->Branch("KpiDSDeltaR",&KpiDSDeltaR);
tree1->Branch("KpiTrkKnhits",&KpiTrkKnhits);
tree1->Branch("KpiTrkpinhits",&KpiTrkpinhits);
tree1->Branch("KpiTrkSnhits",&KpiTrkSnhits);
tree1->Branch("KpiTrkKchi2",&KpiTrkKchi2);
tree1->Branch("KpiTrkpichi2",&KpiTrkpichi2);
tree1->Branch("KpiTrkSchi2",&KpiTrkSchi2);
tree1->Branch("KpiTrkKdxy",&KpiTrkKdxy);
tree1->Branch("KpiTrkpidxy",&KpiTrkpidxy);
tree1->Branch("KpiTrkSdxy",&KpiTrkSdxy);
tree1->Branch("KpiTrkKdz",&KpiTrkKdz);
tree1->Branch("KpiTrkpidz",&KpiTrkpidz);
tree1->Branch("KpiTrkSdz",&KpiTrkSdz);
tree1->Branch("KpiTrkKeta",&KpiTrkKeta);
tree1->Branch("KpiTrkpieta",&KpiTrkpieta);
tree1->Branch("KpiTrkSeta",&KpiTrkSeta);
tree1->Branch("KpiTrkKphi",&KpiTrkKphi);
tree1->Branch("KpiTrkpiphi",&KpiTrkpiphi);
tree1->Branch("KpiTrkSphi",&KpiTrkSphi);
//MC
tree1->Branch("MCDsDeltaR",&MCDsDeltaR);

//K3pi tracks vars
tree2->Branch("K3piTrkKpt",&K3piTrkKpt);
tree2->Branch("K3piTrk1pipt",&K3piTrk1pipt);
tree2->Branch("K3piTrk2pipt",&K3piTrk2pipt);
tree2->Branch("K3piTrk3pipt",&K3piTrk3pipt);
tree2->Branch("K3piTrkSpt",&K3piTrkSpt);

tree2->Branch("D0PtK3pi",&D0PtK3pi);
tree2->Branch("DSPtK3pi",&DSPtK3pi);
tree2->Branch("K3piDSDeltaR",&K3piDSDeltaR);

tree2->Branch("K3piTrkKnhits",&K3piTrkKnhits);
tree2->Branch("K3piTrk1pinhits",&K3piTrk1pinhits);
tree2->Branch("K3piTrk2pinhits",&K3piTrk2pinhits);
tree2->Branch("K3piTrk3pinhits",&K3piTrk3pinhits);
tree2->Branch("K3piTrkSnhits",&K3piTrkSnhits);

tree2->Branch("K3piTrkKchi2",&K3piTrkKchi2);
tree2->Branch("K3piTrk1pichi2",&K3piTrk1pichi2);
tree2->Branch("K3piTrk2pichi2",&K3piTrk2pichi2);
tree2->Branch("K3piTrk3pichi2",&K3piTrk3pichi2);
tree2->Branch("K3piTrkSchi2",&K3piTrkSchi2);

tree2->Branch("K3piTrkKdxy",&K3piTrkKdxy);
tree2->Branch("K3piTrk1pidxy",&K3piTrk1pidxy);
tree2->Branch("K3piTrk2pidxy",&K3piTrk2pidxy);
tree2->Branch("K3piTrk3pidxy",&K3piTrk3pidxy);
tree2->Branch("K3piTrkSdxy",&K3piTrkSdxy);

tree2->Branch("K3piTrkKdz",&K3piTrkKdz);
tree2->Branch("K3piTrk1pidz",&K3piTrk1pidz);
tree2->Branch("K3piTrk2pidz",&K3piTrk2pidz);
tree2->Branch("K3piTrk3pidz",&K3piTrk3pidz);
tree2->Branch("K3piTrkSdz",&K3piTrkSdz);

tree2->Branch("K3piTrkKeta",&K3piTrkKeta);
tree2->Branch("K3piTrk1pieta",&K3piTrk1pieta);
tree2->Branch("K3piTrk2pieta",&K3piTrk2pieta);
tree2->Branch("K3piTrk3pieta",&K3piTrk3pieta);
tree2->Branch("K3piTrkSeta",&K3piTrkSeta);

tree2->Branch("K3piTrkKphi",&K3piTrkKphi);
tree2->Branch("K3piTrk1piphi",&K3piTrk1piphi);
tree2->Branch("K3piTrk2piphi",&K3piTrk2piphi);
tree2->Branch("K3piTrk3piphi",&K3piTrk3piphi);
tree2->Branch("K3piTrkSphi",&K3piTrkSphi);
//MC
tree2->Branch("MCDsDeltaR3",&MCDsDeltaR3);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DSD0Analyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(DSD0Analyzer);
