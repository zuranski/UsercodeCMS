#include "UsercodeCMS/DisplacedJetAnlzr/interface/DJ_JetVertices.h"

DJ_JetVertices::DJ_JetVertices(const edm::ParameterSet& iConfig) : 
patJetCollectionTag_(iConfig.getParameter<edm::InputTag>("patJetCollectionTag")),
useTrackingParticles_(iConfig.getParameter<bool>("useTrackingParticles")),
PromptTrackDxyCut_(iConfig.getParameter<double>("PromptTrackDxyCut")),
TrackPtCut_(iConfig.getParameter<double>("TrackPtCut")),
TrackingEfficiencyFactor_(iConfig.getParameter<double>("TrackingEfficiencyFactor")),
vtxWeight_(iConfig.getParameter<double>("vtxWeight")),
PV_(iConfig.getParameter<unsigned int>("PV")),
vtxconfig_(iConfig.getParameter<edm::ParameterSet>("vertexfitter")),
vtxfitter_(vtxconfig_) {

   produces<std::vector<float> > ("jetCorrPt");
   produces<std::vector<float> > ("jetCorrEta");
   produces<std::vector<float> > ("jetCorrPhi");
   produces<std::vector<float> > ("jetCorrMass");
   produces<std::vector<int> > ("jetNPromptTracks");
   produces<std::vector<int> > ("jetNDispTracks");
   produces<std::vector<float> > ("jetPromptEnergyFrac");
   produces<std::vector<float> > ("jetLxy");
   produces<std::vector<float> > ("jetLxysig");
   produces<std::vector<float> > ("jetVtxX");
   produces<std::vector<float> > ("jetVtxY");
   produces<std::vector<float> > ("jetVtxZ");
   produces<std::vector<float> > ("jetVtxChi2");
   produces<std::vector<float> > ("jetVtxmass");
   produces<std::vector<float> > ("jetVtxpt");
   produces<std::vector<int> > ("jetVtxN");
   produces<std::vector<float> > ("jetVtxdR");
   produces<std::vector<float> > ("jetVtxCharge");
   produces<std::vector<float> > ("jetTrkAvgPt");
   produces<std::vector<float> > ("jetPosip2dFrac");
   produces<std::vector<float> > ("jetNAvgMissHitsAfterVert");
   produces<std::vector<float> > ("jetNAvgHitsInFrontOfVert");
   produces<std::vector<float> > ("jetExoVtxFrac");
   produces<std::vector<float> > ("jetglxydistall");
   produces<std::vector<float> > ("jetglxydistvtx");
   produces<std::vector<float> > ("jetglxydistclr");
   produces<std::vector<float> > ("jetglxyrmsall");
   produces<std::vector<float> > ("jetglxyrmsvtx");
   produces<std::vector<float> > ("jetglxyrmsclr");
   produces<std::vector<int> > ("jetNclusters");
   produces<std::vector<int> > ("jetbestclusterN");
   produces<std::vector<float> > ("jetbestclusterlxy");

}

void
DJ_JetVertices::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   std::auto_ptr<std::vector<float> > jetCorrPt ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetCorrEta ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetCorrPhi ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetCorrMass ( new std::vector<float> );
   std::auto_ptr<std::vector<int> > jetNPromptTracks ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > jetNDispTracks ( new std::vector<int> );
   std::auto_ptr<std::vector<float> > jetPromptEnergyFrac ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetLxy ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetLxysig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetVtxX ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetVtxY ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetVtxZ ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetVtxChi2 ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetVtxmass ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetVtxpt ( new std::vector<float> );
   std::auto_ptr<std::vector<int> > jetVtxN ( new std::vector<int> );
   std::auto_ptr<std::vector<float> > jetVtxdR ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetVtxCharge ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetTrkAvgPt ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetPosip2dFrac ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetNAvgMissHitsAfterVert ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetNAvgHitsInFrontOfVert ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetExoVtxFrac ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetglxydistall ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetglxydistvtx ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetglxydistclr ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetglxyrmsall ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetglxyrmsvtx ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > jetglxyrmsclr ( new std::vector<float> );
   std::auto_ptr<std::vector<int> > jetNclusters ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > jetbestclusterN ( new std::vector<int> );
   std::auto_ptr<std::vector<float> > jetbestclusterlxy ( new std::vector<float> );

   GetEventInfo(iEvent,iSetup);

   edm::Handle<std::vector<pat::Jet> > patJetsHandle;
   iEvent.getByLabel(patJetCollectionTag_,patJetsHandle);

   for (size_t i=0;i<patJetsHandle->size();i++){
     pat::Jet jet = patJetsHandle->at(i);
     reco::Candidate::LorentzVector p4 = jet.p4();

     GlobalVector direction(p4.px(), p4.py(), p4.pz());
     direction = direction.unit();

     //tracks selection
     reco::TrackRefVector jettrks = jet.associatedTracks();
     std::vector<reco::TransientTrack> trksToVertex;     
     std::vector<float> glxysToVertex;
     std::vector<float> ip2dsToVertex;
     
     int nPromptTracks=0;
     float PromptEnergy=0;
     float trkAvgPt=0;
     for (size_t j=0;j<jettrks.size();j++){
        
       const reco::TrackRef trk = jettrks[j];

       if (!trk->quality(reco::TrackBase::highPurity)) continue;
       if (trk->pt() < TrackPtCut_) continue;

       reco::TransientTrack t_trk = theB->build(trk);
       Measurement1D ip2d = IPTools::signedTransverseImpactParameter(t_trk,direction,pv).second;
       Measurement1D ip3d = IPTools::signedImpactParameter3D(t_trk,direction,pv).second;
        if (fabs(ip3d.value())<0.03) nPromptTracks+=1;
        if (fabs(ip2d.value())<PromptTrackDxyCut_){ 
          PromptEnergy += sqrt(0.1396*0.1396 + trk->p()*trk->p());
          continue;
        }

	// tracking inefficiency factor
	if (rand()/float(RAND_MAX) > TrackingEfficiencyFactor_) continue;

        trkAvgPt+=trk->pt();
        float r = 100*3.3*trk->pt()/3.8;
        float guesslxy = ip2d.value()/sin(trk->phi()-direction.phi())*(1-2.5*fabs(ip2d.value())/r);

        ip2dsToVertex.push_back(ip2d.value());
        glxysToVertex.push_back(fabs(guesslxy));
        trksToVertex.push_back(t_trk);

     }

     jetTrkAvgPt->push_back(trksToVertex.size()>0 ? trkAvgPt/trksToVertex.size() : -1);
     jetNPromptTracks->push_back(nPromptTracks);
     jetPromptEnergyFrac->push_back(PromptEnergy/jet.energy());
     jetNDispTracks->push_back(trksToVertex.size());

     bool goodVtx = false;
     TransientVertex jvtx = vtxfitter_.vertex(trksToVertex);
     reco::Vertex vtx(jvtx);
     if (jvtx.isValid() && 
          !vtx.isFake() &&
          (vtx.nTracks(vtxWeight_)>1) &&
          (vtx.normalizedChi2()>0) &&
          (vtx.normalizedChi2()<10)) goodVtx = true;

     ROOT::Math::SVector<double,3> vector(vtx.position().x() - pv.x(),vtx.position().y()-pv.y(),0);
     float lxy = ROOT::Math::Mag(vector);
     reco::Candidate::CovarianceMatrix matrix = vtx.covariance() + pv.covariance();
     float err = sqrt(ROOT::Math::Similarity(matrix,vector))/lxy;
     float sig = lxy/err;
     
     int n=vtx.nTracks(vtxWeight_);
     int charge=0;
     int nposip2d=0;
     int hitsInFrontOfVert=0;
     int missHitsAfterVert=0;
     int FromExo=0;
     std::vector<float> glxysVertex;
     ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > vtxP4;
 
     for (size_t j=0;j<trksToVertex.size();j++){
       reco::TransientTrack t_trk = trksToVertex[j];
       if (jvtx.trackWeight(t_trk)>vtxWeight_){
         GlobalVector p3 = t_trk.trajectoryStateClosestToPoint(jvtx.position()).momentum();
 	 vtxP4 += ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> >(p3.x(),p3.y(),p3.z(),0.13957018);
         charge+=t_trk.track().charge();
         if(ip2dsToVertex[j]>0) nposip2d+=1;
         // hitPattern
         CheckHitPattern::Result res = checkHitPattern_.analyze(iSetup,t_trk.track(),jvtx.vertexState());
         hitsInFrontOfVert += res.hitsInFrontOfVert;
         missHitsAfterVert += res.missHitsAfterVert;
         //glxys
         glxysVertex.push_back(glxysToVertex[j]);
         // tracks from Exotic
         edm::RefToBase<reco::Track> ref_trk = t_trk.trackBaseRef();
         if(RecoToSimColl.find(ref_trk) != RecoToSimColl.end()){
           TrackingParticleRef tp = RecoToSimColl[ref_trk].begin()->first;

           if (tp->genParticle().size()>0){
             std::vector<std::pair<int,double> > moms;
             const HepMC::GenParticle *gp = tp->genParticle().at(0).get();
             moms.push_back(std::pair<int,double> (gp->pdg_id(),gp->production_vertex()->position().perp()));
             GetMothers(gp,moms);
            if (moms.back().first == 6000111 || moms.back().first==6000112) FromExo+=1;
           } // genParticle found
         } // TrackAssociation  
       } // vtx tracks
     } // tracks to Vertex

     float dR = deltaR(direction.eta(),direction.phi(),vtxP4.eta(),vtxP4.phi());
     // corrected P4
     reco::Candidate::LorentzVector physicsP4;
     if (goodVtx){
       physicsP4 = jet.physicsP4(vtx.position(),jet,jet.vertex());
     }

     jetCorrPt->push_back(goodVtx ? physicsP4.Pt() : -1);
     jetCorrEta->push_back(goodVtx ? physicsP4.Eta() : -1);
     jetCorrPhi->push_back(goodVtx ? physicsP4.Phi() : -1);
     jetCorrMass->push_back(goodVtx ? physicsP4.M() : -1);

     jetLxy->push_back(goodVtx ? lxy : -1);
     jetLxysig->push_back(goodVtx ? sig : -1);
     jetVtxX->push_back(goodVtx ? (vtx.position().x()-pv.x()) : 999);
     jetVtxY->push_back(goodVtx ? (vtx.position().y()-pv.y()) : 999);
     jetVtxZ->push_back(goodVtx ? (vtx.position().z()-pv.z()) : 999);
     jetVtxChi2->push_back(goodVtx ? vtx.normalizedChi2() : -1);
     jetVtxmass->push_back(goodVtx ? vtxP4.M() : -1);
     jetVtxpt->push_back(goodVtx ? vtxP4.Pt() : -1);
     jetVtxdR->push_back(goodVtx ? dR : -1);
     jetVtxN->push_back(goodVtx ? n : -1);
     jetVtxCharge->push_back(goodVtx ? charge : 999);
     jetNAvgHitsInFrontOfVert->push_back(goodVtx ? hitsInFrontOfVert/float(n) : -1);
     jetNAvgMissHitsAfterVert->push_back(goodVtx ? missHitsAfterVert/float(n) : -1);
     jetExoVtxFrac->push_back(goodVtx ? FromExo/float(n) : -1);
     jetPosip2dFrac->push_back(goodVtx ? nposip2d/float(n) : -1);
 
     // do glxy stuff here
     helpers help;
     jetglxydistall->push_back(goodVtx ? help.AvgDistance(glxysToVertex,lxy) : -1);
     jetglxydistvtx->push_back(goodVtx ? help.AvgDistance(glxysVertex,lxy) : -1);
     jetglxyrmsall->push_back(goodVtx ? help.RMS(glxysToVertex,lxy) : -1);
     jetglxyrmsvtx->push_back(goodVtx ? help.RMS(glxysVertex,lxy) : -1);

     // clusters
     std::vector<std::vector<float> > clusters = help.clusters(glxysToVertex,0.15*lxy);
     std::vector<float> bestcluster = help.bestcluster(clusters,lxy);

     jetglxyrmsclr->push_back(goodVtx ? help.RMS(bestcluster,lxy) : -1);
     jetglxydistclr->push_back(goodVtx ? help.AvgDistance(bestcluster,lxy) : -1);
     jetNclusters->push_back(goodVtx ? help.Nclusters(clusters) : -1);
     jetbestclusterlxy->push_back(goodVtx ? ((bestcluster.size()>0) ? help.Avg(bestcluster)/lxy : -1) : -1);
     jetbestclusterN->push_back(goodVtx ? bestcluster.size() : -1);

   } // jet loop

  iEvent.put(jetCorrPt,"jetCorrPt");
  iEvent.put(jetCorrEta,"jetCorrEta");
  iEvent.put(jetCorrPhi,"jetCorrPhi");
  iEvent.put(jetCorrMass,"jetCorrMass");
  iEvent.put(jetNPromptTracks, "jetNPromptTracks");
  iEvent.put(jetNDispTracks, "jetNDispTracks");
  iEvent.put(jetPromptEnergyFrac, "jetPromptEnergyFrac");
  iEvent.put(jetVtxX,"jetVtxX");
  iEvent.put(jetVtxY,"jetVtxY");
  iEvent.put(jetVtxZ,"jetVtxZ");
  iEvent.put(jetLxy, "jetLxy");
  iEvent.put(jetLxysig, "jetLxysig");
  iEvent.put(jetVtxChi2,"jetVtxChi2");
  iEvent.put(jetVtxmass,"jetVtxmass");
  iEvent.put(jetVtxpt,"jetVtxpt");
  iEvent.put(jetVtxdR,"jetVtxdR");
  iEvent.put(jetVtxN,"jetVtxN");
  iEvent.put(jetVtxCharge,"jetVtxCharge");
  iEvent.put(jetTrkAvgPt,"jetTrkAvgPt");
  iEvent.put(jetPosip2dFrac,"jetPosip2dFrac");
  iEvent.put(jetNAvgHitsInFrontOfVert,"jetNAvgHitsInFrontOfVert");
  iEvent.put(jetNAvgMissHitsAfterVert,"jetNAvgMissHitsAfterVert");
  iEvent.put(jetExoVtxFrac,"jetExoVtxFrac");
  iEvent.put(jetglxydistall,"jetglxydistall");
  iEvent.put(jetglxydistvtx,"jetglxydistvtx");
  iEvent.put(jetglxydistclr,"jetglxydistclr");
  iEvent.put(jetglxyrmsall,"jetglxyrmsall");
  iEvent.put(jetglxyrmsvtx,"jetglxyrmsvtx");
  iEvent.put(jetglxyrmsclr,"jetglxyrmsclr");
  iEvent.put(jetNclusters,"jetNclusters");
  iEvent.put(jetbestclusterN,"jetbestclusterN");
  iEvent.put(jetbestclusterlxy,"jetbestclusterlxy");

}


void DJ_JetVertices::GetEventInfo(const edm::Event& iEvent, const edm::EventSetup& iSetup){

// Vertices and tracks

   edm::Handle<reco::VertexCollection> recVtxs;
   iEvent.getByLabel("offlinePrimaryVertices", recVtxs); 
   if (recVtxs->size()>PV_) 
     pv=recVtxs->at(PV_); 
   else
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

void DJ_JetVertices::GetMothers(const HepMC::GenParticle *gp, std::vector<std::pair<int,double> > &moms){

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

