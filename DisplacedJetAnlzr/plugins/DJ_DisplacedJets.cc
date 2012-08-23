#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_DisplacedJets.h"


DJ_DisplacedJets::DJ_DisplacedJets(const edm::ParameterSet& iConfig) : 
patJetCollectionTag_(iConfig.getParameter<edm::InputTag>("patJetCollectionTag")),
useTrackingParticles_(iConfig.getParameter<bool>("useTrackingParticles")),
PromptTrackDxyCut_(iConfig.getParameter<double>("PromptTrackDxyCut")),
TrackPtCut_(iConfig.getParameter<double>("TrackPtCut")),
vtxconfig_(iConfig.getParameter<edm::ParameterSet>("vertexfitter")),
vtxfitter_(vtxconfig_) {

  produces <std::vector<djcandidate> > ("singlejet");
  produces <std::vector<djcandidate> > ("doublejet");

}

void
DJ_DisplacedJets::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   std::auto_ptr<std::vector<djcandidate> > singlejet ( new std::vector<djcandidate>() );
   std::auto_ptr<std::vector<djcandidate> > doublejet ( new std::vector<djcandidate>() );

   GetEventInfo(iEvent,iSetup);
   LoopPFJets(iEvent,iSetup,*singlejet.get(),*doublejet.get());

   iEvent.put(singlejet, "singlejet" );
   iEvent.put(doublejet, "doublejet" );

}


void DJ_DisplacedJets::GetEventInfo(const edm::Event& iEvent, const edm::EventSetup& iSetup){

// Vertices and tracks

   edm::Handle<reco::VertexCollection> recVtxs;
   iEvent.getByLabel("offlinePrimaryVertices", recVtxs); 
   pv = recVtxs->front();

   edm::Handle<edm::View<reco::Track> > generalTracks;
   iEvent.getByLabel("generalTracks",generalTracks);
// TransientTrack Builder
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);

// Reco to Sim Track association
   if(!iEvent.isRealData() && useTrackingParticles_){
     edm::Handle<std::vector<TrackingParticle> > TPCollectionH ;
     try{
       iEvent.getByLabel(edm::InputTag("mergedtruth","MergedTrackTruth","HLT"),TPCollectionH);
       edm::ESHandle<TrackAssociatorBase> myAssociator;
       iSetup.get<TrackAssociatorRecord>().get("TrackAssociatorByHits", myAssociator);
       RecoToSimColl = myAssociator->associateRecoToSim(generalTracks,TPCollectionH,&iEvent );
     } catch (...) {;}
   }

}

void DJ_DisplacedJets::DoVertexing(const edm::EventSetup& iSetup, djcandidate &djc, std::vector<reco::TransientTrack> disptrks){

  
  if (disptrks.size()<2) return;

  TransientVertex jvtx = vtxfitter_.vertex(disptrks);

  if (!jvtx.isValid()) return;
  if (jvtx.normalisedChiSquared()<0.) return;

  reco::Vertex vtx(jvtx);

    djc.vtxX = vtx.position().x();
    djc.vtxY = vtx.position().y();
    djc.vtxZ = vtx.position().z();

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
      djc.disptracks.at(i).vtxpt = p3.perp();
      djc.disptracks.at(i).vtxeta = p3.eta();
      djc.disptracks.at(i).vtxphi = p3.phi();
      djc.disptracks.at(i).vtxweight = jvtx.trackWeight(t_trk);

      if (jvtx.trackWeight(t_trk)>0.5){
        p4TrkSum += ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> >(p3.x(),p3.y(),p3.z(),0.1396);
        n+=1;
        charge+=t_trk.track().charge();
      }

      // hitPattern
      CheckHitPattern::Result res = checkHitPattern_.analyze(iSetup,t_trk.track(),jvtx.vertexState());
      djc.disptracks.at(i).nHitsInFrontOfVert = res.hitsInFrontOfVert;
      djc.disptracks.at(i).nMissHitsAfterVert = res.missHitsAfterVert;

    }

   
    float dR = deltaR(djc.eta,djc.phi,p4TrkSum.eta(),p4TrkSum.phi());
    djc.vtxchi2 = jvtx.normalisedChiSquared();
    djc.vtxmass = p4TrkSum.M();
    djc.vtxpt = p4TrkSum.Pt();
    djc.vtxdR = dR;
    djc.vtxN = n;
    djc.vtxCharge = charge;
    djc.lxy = lxy;
    djc.lxysig = sig;

      
    for (size_t i=0;i<djc.disptracks.size();i++){
      track t = djc.disptracks.at(i);
      edm::LogInfo("DJ_DisplacedJetsInfo")
      << "track" 
      << " pt: " << t.pt 
      << " ip2d: " << t.ip2d
      << " weight: " << t.vtxweight 
      << " lxy: " << t.lxy
      << " NbefVtx: " << t.nHitsInFrontOfVert
      << " NMissAftVtx: " << t.nMissHitsAfterVert
      << " guesslxy:  " << t.guesslxy;  
    }
       
     edm::LogInfo("DJ_DisplacedJetsInfo")
     << " VTX "
     << " chi2: " << djc.vtxchi2 
     << " vtxmass: " << djc.vtxmass 
     << " pt: " << djc.vtxpt 
     << " lxy: " << djc.lxy 
     << " nTrks: " << n
     << " charge: " << charge
     << " dR: " << dR
     << " mass " << djc.mass
     << " promptEfrac " << djc.PromptEnergyFrac; 

}


void DJ_DisplacedJets::LoopPFJets(const edm::Event& iEvent, const edm::EventSetup& iSetup, std::vector<djcandidate> &singlejet, std::vector<djcandidate> &doublejet){

   edm::Handle<std::vector<pat::Jet> > patJetsHandle;
   iEvent.getByLabel(patJetCollectionTag_,patJetsHandle);

   std::vector<std::vector<reco::TransientTrack> > PFJetDispTracks;
   std::vector<pat::Jet> PFJetDisp;

   for (std::vector<pat::Jet>::const_iterator j = patJetsHandle->begin(); j != patJetsHandle->end();++j){

     djcandidate djc;

     djc.idx1 = std::distance(patJetsHandle->begin(),j);
     djc.idx2 = djc.idx1;

     djc.energy = j->energy();
     djc.pt = j->pt();
     djc.eta = j->eta();
     djc.phi = j->phi();
     djc.mass = j->mass();

     djc.chgHadFrac = j->chargedHadronEnergyFraction();
     djc.chgHadN = j->chargedHadronMultiplicity();
     djc.neuHadFrac = j->neutralHadronEnergyFraction();
     djc.neuHadN = j->neutralMultiplicity();
     djc.phFrac = j->photonEnergyFraction();
     djc.phN = j->photonMultiplicity();
     djc.eleFrac = j->electronEnergyFraction();
     djc.eleN = j->electronMultiplicity();
     djc.muFrac = j->muonEnergyFraction();
     djc.muN = j->muonMultiplicity();

     GlobalVector direction(j->px(), j->py(), j->pz());
     direction = direction.unit();

     reco::TrackRefVector jtrks = j->associatedTracks();
     std::vector<reco::TransientTrack> disptrks;
     std::vector<track> tracks_;

     // a la HLT variables:
     int nPromptTracks = 0;
     double PromptEnergy = 0.;

     // track selection before vertexing

     for (size_t i=0;i<jtrks.size();i++){
	
	const reco::Track *trk = jtrks[i].get();

	if(!jtrks[i]->quality(reco::TrackBase::highPurity)) continue;
        if (jtrks[i]->pt() < TrackPtCut_) continue;

        reco::TransientTrack t_trk = theB->build(*jtrks[i].get());
        Measurement1D ip2d = IPTools::signedTransverseImpactParameter(t_trk,direction,pv).second;
        Measurement1D ip3d = IPTools::signedImpactParameter3D(t_trk,direction,pv).second;

        if (fabs(ip2d.value())<PromptTrackDxyCut_){ 
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
//     if (PromptEnergy/djc.energy>0.2) continue;
//!!!!!!!!!!!!!!

     // a la HLT variables
     djc.nPrompt = nPromptTracks;
     djc.PromptEnergyFrac = PromptEnergy/djc.energy;
     djc.nDispTracks = disptrks.size();

     // unless Vtx failes..  
     djc.vtxchi2 = -1;
     djc.vtxmass = -1;
     djc.vtxpt = -1;
     djc.vtxdR = -1;
     djc.vtxCharge = -999;
     djc.vtxN = -1;
     djc.lxy = -1;
     djc.lxysig = -1;
     djc.vtxX = -1;
     djc.vtxY = -1;
     djc.vtxZ = -1;

     djc.disptracks = tracks_;
     singlejet.push_back(djc);
     PFJetDispTracks.push_back(disptrks);
     PFJetDisp.push_back(*j);

  }

  // single candidates
  for (unsigned int i=0;i<singlejet.size();i++){
    DoVertexing(iSetup,singlejet.at(i),PFJetDispTracks.at(i));
  }

  // double candidates
  if (singlejet.size()>1){
     for (size_t i=0;i<singlejet.size()-1;i++){
       for (size_t j=i+1;j<singlejet.size();j++){

         pat::Jet j1 = PFJetDisp.at(i);
         pat::Jet j2 = PFJetDisp.at(j);
         djcandidate djc1 = singlejet.at(i);
         djcandidate djc2 = singlejet.at(j);

         std::vector<reco::TransientTrack> disptrks = PFJetDispTracks.at(i);
         std::vector<reco::TransientTrack> disptrks2 = PFJetDispTracks.at(j);
         disptrks.insert(disptrks.end(),disptrks2.begin(),disptrks2.end());

         std::vector<track> tracks_ = djc1.disptracks;
         std::vector<track> tracks2_ = djc2.disptracks;
	 tracks_.insert(tracks_.end(),tracks2_.begin(),tracks2_.end());
	 djcandidate djc;

         djc.chgHadN = djc1.chgHadN + djc2.chgHadN;
         djc.neuHadN = djc1.neuHadN + djc2.neuHadN;
	 djc.muN = djc1.muN + djc2.muN;
	 djc.eleN = djc1.eleN + djc2.eleN;
	 djc.phN = djc1.phN + djc2.phN;
         
         djc.idx1 = i;
         djc.idx2 = j;

         djc.chgHadFrac = (djc1.chgHadFrac*djc1.energy + djc2.chgHadFrac*djc2.energy)/(djc1.energy+djc2.energy);
         djc.neuHadFrac = (djc1.neuHadFrac*djc1.energy + djc2.neuHadFrac*djc2.energy)/(djc1.energy+djc2.energy);
         djc.muFrac = (djc1.muFrac*djc1.energy + djc2.muFrac*djc2.energy)/(djc1.energy+djc2.energy);
         djc.eleFrac = (djc1.eleFrac*djc1.energy + djc2.eleFrac*djc2.energy)/(djc1.energy+djc2.energy);
         djc.phFrac = (djc1.phFrac*djc1.energy + djc2.phFrac*djc2.energy)/(djc1.energy+djc2.energy);

         reco::Candidate::LorentzVector p4 = j1.p4() + j2.p4();
         djc.energy = djc1.energy + djc2.energy;
         djc.pt = p4.pt();
         djc.eta = p4.eta();
         djc.phi = p4.phi();
         djc.mass = p4.mass();

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
         djc.nPrompt = djc1.nPrompt + djc2.nPrompt;
         djc.PromptEnergyFrac = (djc1.PromptEnergyFrac*djc1.energy + djc2.PromptEnergyFrac*djc2.energy)/djc.energy;
         djc.nDispTracks = disptrks.size();

         djc.vtxchi2 = -1;
         djc.vtxmass = -1;
         djc.vtxpt = -1;
         djc.vtxdR = -1;
         djc.vtxCharge = -999;
         djc.vtxN = -1;
         djc.lxy = -1;
         djc.lxysig = -1;
         djc.vtxX = -1;
         djc.vtxY = -1;
         djc.vtxZ = -1;

         djc.disptracks=tracks_;
         DoVertexing(iSetup,djc,disptrks);
         doublejet.push_back(djc);
       }
     }
   }

}


void DJ_DisplacedJets::GetMothers(const HepMC::GenParticle *gp, std::vector<std::pair<int,double> > &moms){

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


