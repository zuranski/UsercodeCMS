// Package:    DisplacedJetAnlzr
// Class:      DisplacedJetAnlzr
// 

//
// Original Author:  Andrzej Zuranski
//         Created:  Thu Feb 16 09:43:08 CST 2012


// system include files
#include <memory>

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

//File Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

//My Data Formats
#include "MyAnalysis/DisplacedJetAnlzr/interface/exotic.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/genjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjet.h"

//EDM Data Formats
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/ParticleFlowReco/interface/PFDisplacedVertex.h"

//Transient Tracks
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

//Vertex fitter
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexSmoother.h"
#include "RecoVertex/AdaptiveVertexFit/interface/AdaptiveVertexFitter.h"
#include "RecoVertex/ConfigurableVertexReco/interface/ConfigurableVertexReconstructor.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"

//Track Association
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorBase.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

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


      edm::ParameterSet vtxconfig_;
      edm::InputTag hlttag_;
      bool debugoutput,useTP;
      ConfigurableVertexReconstructor vtxmaker_;
      reco::RecoToSimCollection RecoToSimColl;

      // ----------member data ---------------------------
      TTree *tree;
      std::vector<std::string> triggers;
      std::vector<exotic> Xs;
      std::vector<genjet> gjets;
      std::vector<pfjet> pfjets;
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
vtxconfig_(iConfig.getParameter<edm::ParameterSet>("vertexreco")),
hlttag_(iConfig.getParameter<edm::InputTag>("hlttag")),
debugoutput(iConfig.getParameter<bool>("debugoutput")),
useTP(iConfig.getParameter<bool>("useTP")),
vtxmaker_(vtxconfig_) {
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

// Clear variables
   triggers.clear();Xs.clear();gjets.clear();pfjets.clear();

// Triggers


   HLTConfigProvider hltConfig;
   bool changed;
   hltConfig.init(iEvent.getRun(),iSetup,hlttag_.process(),changed);

   edm::Handle<edm::TriggerResults> hltResults;
   iEvent.getByLabel(hlttag_,hltResults);
   const std::vector< std::string > &trgNames = hltConfig.triggerNames();

   for (size_t i=0;i<hltResults->size();i++)
	if (hltResults->accept(i) && trgNames.at(i).find("DisplacedPFJet") != std::string::npos)
	 triggers.push_back(trgNames.at(i));

   // no DisplacedPFJet trigger fired.. so sad
   //if (triggers.size() == 0 ) return;

// generator information

  if (!iEvent.isRealData()){

  Handle<HepMCProduct> EvtHandle;
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

          gjets.push_back(gj);
        }

	if (debugoutput)
	  std::cout << X.lxy/10. << std::endl;

        Xs.push_back(X);
      }

    }
  }


// Trigger objects ... for later

// TransientTrack Builder

   edm::ESHandle<TransientTrackBuilder> theB;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);

// Reco to Sim Track association

   if(!iEvent.isRealData() && useTP){
     Handle<edm::View<reco::Track> > trackCollectionH;
     iEvent.getByLabel("generalTracks",trackCollectionH);
     edm::Handle<std::vector<TrackingParticle> > TPCollectionH ;
     try{
       iEvent.getByLabel(edm::InputTag("mergedtruth","MergedTrackTruth","HLT"),TPCollectionH);
       ESHandle<TrackAssociatorBase> myAssociator;
       iSetup.get<TrackAssociatorRecord>().get("TrackAssociatorByHits", myAssociator);
       RecoToSimColl = myAssociator->associateRecoToSim(trackCollectionH,TPCollectionH,&iEvent );
     } catch (...) {;}
   } 

// BeamSpot

   reco::BeamSpot BeamSpot;
   edm::Handle<reco::BeamSpot> BeamSpotH;
   iEvent.getByLabel("offlineBeamSpot",BeamSpotH);
   BeamSpot = *BeamSpotH;
   const reco::Vertex bs(BeamSpot.position(),BeamSpot.covariance3D()) ;

// Leading Primary Vertex

   edm::Handle<std::vector<reco::Vertex> > primaryVertices;
   iEvent.getByLabel("offlinePrimaryVertices",primaryVertices);
   const reco::Vertex &pv = primaryVertices->front();

// PFJets

   edm::Handle<reco::PFJetCollection> pfjetsh;
   iEvent.getByLabel("ak5PFJets",pfjetsh);

   for (reco::PFJetCollection::const_iterator j = pfjetsh->begin(); j != pfjetsh->end();++j){

     if (j->pt()<50 || fabs(j->eta())>2) continue;

     pfjet pfj;

     pfj.energy = j->energy();
     pfj.pt = j->pt();
     pfj.eta = j->eta();
     pfj.phi = j->phi();

     double lxy = -1;
     for (size_t i=0;i<gjets.size();i++){
       if (deltaR(pfj.eta,pfj.phi,gjets.at(i).eta,gjets.at(i).phi) < 0.3 ){
         lxy = gjets.at(i).lxy/10.;
         break;
       }
     }
     if (debugoutput){
       std::cout << "===============================================" << std::endl;
       std::cout << "pfjet: " << lxy << " " <<  pfj.pt << std::endl;
     }

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

     reco::TrackRefVector jtrks = j->getTrackRefs();
     std::vector<reco::TransientTrack> goodtrks;
     std::vector<track> tracks_;

     // track selection before vertexing

     for (size_t i=0;i<jtrks.size();i++){
	
	const reco::Track *trk = jtrks[i].get();

        if (jtrks[i]->pt() < 1.) continue;
        if (jtrks[i]->normalizedChi2() > 10) continue;
        if (jtrks[i]->numberOfValidHits() < 5) continue;

        track track_;

        track_.pt = trk->pt();
        track_.eta = trk->eta();
	track_.phi = trk->phi();
	track_.chi2 = trk->normalizedChi2();
	track_.nHits = trk->numberOfValidHits();
	track_.nPixHits = trk->hitPattern().numberOfValidPixelHits();
	track_.algo = trk->algo();

        reco::TransientTrack t_trk = theB->build(*jtrks[i].get());
        Measurement1D ip2d = IPTools::signedTransverseImpactParameter(t_trk,direction,pv).second;
        Measurement1D ip3d = IPTools::signedImpactParameter3D(t_trk,direction,pv).second;

	track_.ip2d = ip2d.value();
	track_.ip2dsig = ip2d.significance();
	track_.ip3d = ip3d.value();
	track_.ip3dsig = ip3d.significance();
	track_.vtxweight = -1;

        if (fabs(ip2d.value())<0.0) continue;
	
        edm::RefToBase<reco::Track> ref_trk(jtrks[i]); 
        if(RecoToSimColl.find(ref_trk) != RecoToSimColl.end()){
          TrackingParticleRef tp = RecoToSimColl[ref_trk].begin()->first;
          const TrackingVertex  *tv = tp->parentVertex().get();
          track_.lxy = tv->position().pt();
        } else {
          track_.lxy = -1;
        }

        if (debugoutput){
          std::cout << "track pt: " << track_.pt \
          << " algo: " << track_.algo \
          << " ip2d: " << track_.ip2d \
          << " lxy:  " << track_.lxy << std::endl;  
        }

        tracks_.push_back(track_);
        goodtrks.push_back(t_trk);
     }

     pfj.vtxchi2 = -1;
     pfj.vtxmass = -1;
     pfj.vtxpt = -1;
     pfj.lxy = -1;
     pfj.lxysig = -1;
     pfj.ntracks = goodtrks.size();

     if (goodtrks.size()>1){
       
       double maxshift =0.0005;
       unsigned int maxstep = 30;
       double maxlpshift = 0.1;
       double weightThreshold = 0.5;
       double sigmacut = 10.;
       double Tini = 256.;
       double ratio = 0.25;
       static AdaptiveVertexFitter avf(
         GeometricAnnealing ( sigmacut, Tini, ratio ), 
         DefaultLinearizationPointFinder(),
         KalmanVertexUpdator<5>(), 
         KalmanVertexTrackCompatibilityEstimator<5>(), 
         KalmanVertexSmoother() );
       avf.setParameters ( maxshift, maxlpshift, maxstep, weightThreshold );
    
       TransientVertex jvtx = avf.vertex(goodtrks);

       if (jvtx.isValid()){

	 reco::Vertex vtx(jvtx);

         ROOT::Math::SVector<double,3> vector(vtx.position().x() - pv.x(),vtx.position().y()-pv.y(),0);
         double lxy = ROOT::Math::Mag(vector);
	 reco::Candidate::CovarianceMatrix matrix = vtx.covariance() + pv.covariance();
	 double err = sqrt(ROOT::Math::Similarity(matrix,vector))/lxy;
	 double sig = lxy/err;

         ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> > p4TrkSum;
	 for (size_t i=0;i<goodtrks.size();i++){
	   reco::TransientTrack t_trk = goodtrks.at(i);
           GlobalVector p3 = t_trk.trajectoryStateClosestToPoint(jvtx.position()).momentum();

           // update track parameters after succesful vtx fit
	   tracks_.at(i).pt = p3.perp();
	   tracks_.at(i).eta = p3.eta();
	   tracks_.at(i).phi = p3.phi();
	   tracks_.at(i).vtxweight = jvtx.trackWeight(t_trk);

	   p4TrkSum += jvtx.trackWeight(t_trk) * ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> >(p3.x(),p3.y(),p3.z(),0.1396);
         }


	 pfj.vtxchi2 = jvtx.normalisedChiSquared();
	 pfj.vtxmass = p4TrkSum.M();
	 pfj.vtxpt = p4TrkSum.Pt();
         pfj.lxy = lxy;
	 pfj.lxysig = sig;

	 if (debugoutput){
           std::cout << "chi2: " << pfj.vtxchi2 \
    	   << " vtxmass: " << pfj.vtxmass \
 	   << " lxy: " << lxy \
	   << " sig: " << sig \
	   << " ntrks: " << pfj.ntracks << std::endl;
         }
       } else {
         if (debugoutput)
           std::cout << "Vertex Fit Failed!!" << std::endl;
       }
     }

     pfj.tracks = tracks_;
     pfjets.push_back(pfj);

   }


   tree->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedJetAnlzr::beginJob()
{
tree->Branch("triggers",&triggers);
tree->Branch("Xs",&Xs);
tree->Branch("gjets",&gjets);
tree->Branch("pfjets",&pfjets);
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
