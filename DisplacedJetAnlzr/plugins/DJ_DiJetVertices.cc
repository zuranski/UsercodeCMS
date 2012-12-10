#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_DiJetVertices.h"

DJ_DiJetVertices::DJ_DiJetVertices(const edm::ParameterSet& iConfig) : 
patJetCollectionTag_(iConfig.getParameter<edm::InputTag>("patJetCollectionTag")),
useTrackingParticles_(iConfig.getParameter<bool>("useTrackingParticles")),
PromptTrackDxyCut_(iConfig.getParameter<double>("PromptTrackDxyCut")),
TrackPtCut_(iConfig.getParameter<double>("TrackPtCut")),
TrackingEfficiencyFactor_(iConfig.getParameter<double>("TrackingEfficiencyFactor")),
vtxWeight_(iConfig.getParameter<double>("vtxWeight")),
vtxconfig_(iConfig.getParameter<edm::ParameterSet>("vertexfitter")),
vtxfitter_(vtxconfig_) {

   produces<std::vector<float> > ("dijetCorrPt");
   produces<std::vector<float> > ("dijetCorrEta");
   produces<std::vector<float> > ("dijetCorrPhi");
   produces<std::vector<float> > ("dijetCorrMass");
   produces<std::vector<int> > ("dijetNPromptTracks");
   produces<std::vector<int> > ("dijetNDispTracks");
   produces<std::vector<float> > ("dijetPromptEnergyFrac");
   produces<std::vector<float> > ("dijetLxy");
   produces<std::vector<float> > ("dijetLxysig");
   produces<std::vector<float> > ("dijetVtxX");
   produces<std::vector<float> > ("dijetVtxY");
   produces<std::vector<float> > ("dijetVtxZ");
   produces<std::vector<float> > ("dijetVtxChi2");
   produces<std::vector<float> > ("dijetVtxmass");
   produces<std::vector<float> > ("dijetVtxpt");
   produces<std::vector<int> > ("dijetVtxN");
   produces<std::vector<int> > ("dijetVtxN1");
   produces<std::vector<int> > ("dijetVtxN2");
   produces<std::vector<float> > ("dijetVtxdR");
   produces<std::vector<float> > ("dijetVtxCharge");
   produces<std::vector<float> > ("dijetPosip2dFrac");
   produces<std::vector<float> > ("dijetNAvgMissHitsAfterVert");
   produces<std::vector<float> > ("dijetNAvgHitsInFrontOfVert");
   produces<std::vector<float> > ("dijetExoVtxFrac");
   produces<std::vector<float> > ("dijetglxydistall");
   produces<std::vector<float> > ("dijetglxydistvtx");
   produces<std::vector<float> > ("dijetglxydistclr");
   produces<std::vector<float> > ("dijetglxyrmsall");
   produces<std::vector<float> > ("dijetglxyrmsvtx");
   produces<std::vector<float> > ("dijetglxyrmsclr");
   produces<std::vector<int> > ("dijetNclusters");
   produces<std::vector<int> > ("dijetbestclusterN");
   produces<std::vector<int> > ("dijetbestclusterN1");
   produces<std::vector<int> > ("dijetbestclusterN2");
   produces<std::vector<float> > ("dijetbestclusterlxy");

}

void
DJ_DiJetVertices::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
 
   std::auto_ptr<std::vector<float> > dijetCorrPt ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetCorrEta ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetCorrPhi ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetCorrMass ( new std::vector<float> );
   std::auto_ptr<std::vector<int> > dijetNPromptTracks ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > dijetNDispTracks ( new std::vector<int> );
   std::auto_ptr<std::vector<float> > dijetPromptEnergyFrac ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetLxy ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetLxysig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetVtxX ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetVtxY ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetVtxZ ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetVtxChi2 ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetVtxmass ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetVtxpt ( new std::vector<float> );
   std::auto_ptr<std::vector<int> > dijetVtxN ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > dijetVtxN1 ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > dijetVtxN2 ( new std::vector<int> );
   std::auto_ptr<std::vector<float> > dijetVtxdR ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetVtxCharge ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetPosip2dFrac ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetNAvgMissHitsAfterVert ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetNAvgHitsInFrontOfVert ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetExoVtxFrac ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetglxydistall ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetglxydistvtx ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetglxydistclr ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetglxyrmsall ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetglxyrmsvtx ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > dijetglxyrmsclr ( new std::vector<float> );
   std::auto_ptr<std::vector<int> > dijetNclusters ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > dijetbestclusterN ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > dijetbestclusterN1 ( new std::vector<int> );
   std::auto_ptr<std::vector<int> > dijetbestclusterN2 ( new std::vector<int> );
   std::auto_ptr<std::vector<float> > dijetbestclusterlxy ( new std::vector<float> );

   GetEventInfo(iEvent,iSetup);

   edm::Handle<std::vector<pat::Jet> > patJetsHandle;
   iEvent.getByLabel(patJetCollectionTag_,patJetsHandle);

   for (int i=0;i<int(patJetsHandle->size()-1);i++){
    for (size_t k=i+1;k<patJetsHandle->size();k++){
     pat::Jet jet1 = patJetsHandle->at(i);
     pat::Jet jet2 = patJetsHandle->at(k);
     reco::Candidate::LorentzVector p4 = jet1.p4() + jet2.p4();

     GlobalVector direction(p4.px(), p4.py(), p4.pz());
     direction = direction.unit();

     //tracks selection
     reco::TrackRefVector dijettrks = jet1.associatedTracks();
     reco::TrackRefVector dijettrks2 = jet2.associatedTracks();

     ////TO REMOVE
     std::vector<int> indices1(dijettrks.size());
     std::vector<int> indices2(dijettrks2.size());
     std::fill(indices1.begin(),indices1.end(),1);
     std::fill(indices2.begin(),indices2.end(),2);

     for(size_t j=0;j<dijettrks2.size();j++) dijettrks.push_back(dijettrks2[j]);
     //indices for jet1 and jet 2
     std::vector<int> indices(dijettrks.size());
     std::fill(indices.begin(),indices.end()-dijettrks2.size(),1);
     std::fill(indices.end()-dijettrks2.size(),indices.end(),2);

     std::vector<reco::TransientTrack> trksToVertex;     
     std::vector<int> indicesToVertex;
     std::vector<float> glxysToVertex;
     std::vector<float> ip2dsToVertex;
     
     int nPromptTracks=0;
     float PromptEnergy=0;
     for (size_t j=0;j<dijettrks.size();j++){
        
       const reco::TrackRef trk = dijettrks[j];

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

        float r = 100*3.3*trk->pt()/3.8;
        float guesslxy = ip2d.value()/sin(trk->phi()-direction.phi())*(1-2.5*fabs(ip2d.value())/r);

        ip2dsToVertex.push_back(ip2d.value());
        glxysToVertex.push_back(fabs(guesslxy));
        trksToVertex.push_back(t_trk);
        indicesToVertex.push_back(indices[j]);

     }

     dijetNPromptTracks->push_back(nPromptTracks);
     dijetPromptEnergyFrac->push_back(PromptEnergy/(jet1.energy()+jet2.energy()));
     dijetNDispTracks->push_back(trksToVertex.size());

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
     int VtxN1=0;
     int VtxN2=0;
     std::vector<float> glxysVertex;
     ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > vtxP4;
 
     for (size_t j=0;j<trksToVertex.size();j++){
       reco::TransientTrack t_trk = trksToVertex[j];
       if (jvtx.trackWeight(t_trk)>vtxWeight_){
         GlobalVector p3 = t_trk.trajectoryStateClosestToPoint(jvtx.position()).momentum();
 	 vtxP4 += ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> >(p3.x(),p3.y(),p3.z(),0.13957018);
         charge+=t_trk.track().charge();
         if (indicesToVertex[j] == 1) VtxN1+=1;
         if (indicesToVertex[j] == 2) VtxN2+=1;
         if (ip2dsToVertex[j]>0) nposip2d+=1;
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

     reco::Candidate::LorentzVector physicsP4;
     //reco::Candidate::LorentzVector physicsP41,physicsP42,physicsP43;
     if (goodVtx){
       // corrected P4
       physicsP4 = jet1.physicsP4(vtx.position(),jet1,jet1.vertex())
                                                 +jet2.physicsP4(vtx.position(),jet2,jet2.vertex());

       //physicsP41 = detectorP4(jet1,vtx,jvtx,0) + detectorP4(jet2,vtx,jvtx,0);
       //physicsP42 = detectorP4(jet1,vtx,jvtx,1) + detectorP4(jet2,vtx,jvtx,1);
       //physicsP43 = detectorP4(jet1,vtx,jvtx,2) + detectorP4(jet2,vtx,jvtx,2);
     }

     dijetCorrPt->push_back(goodVtx ? physicsP4.Pt() : -1);
     dijetCorrEta->push_back(goodVtx ? physicsP4.Eta() : -1);
     dijetCorrPhi->push_back(goodVtx ? physicsP4.Phi() : -1);
     dijetCorrMass->push_back(goodVtx ? physicsP4.M() : -1);

     dijetLxy->push_back(goodVtx ? lxy : -1);
     dijetLxysig->push_back(goodVtx ? sig : -1);
     dijetVtxX->push_back(goodVtx ? (vtx.position().x()-pv.x()) : 999);
     dijetVtxY->push_back(goodVtx ? (vtx.position().y()-pv.y()) : 999);
     dijetVtxZ->push_back(goodVtx ? (vtx.position().z()-pv.z()) : 999);
     dijetVtxChi2->push_back(goodVtx ? vtx.normalizedChi2() : -1);
     dijetVtxmass->push_back(goodVtx ? vtxP4.M() : -1);
     dijetVtxpt->push_back(goodVtx ? vtxP4.Pt() : -1);
     dijetVtxdR->push_back(goodVtx ? dR : -1);
     dijetVtxN->push_back(goodVtx ? n : -1);
     dijetVtxCharge->push_back(goodVtx ? charge : 999);
     dijetNAvgHitsInFrontOfVert->push_back(goodVtx ? hitsInFrontOfVert/float(n) : -1);
     dijetNAvgMissHitsAfterVert->push_back(goodVtx ? missHitsAfterVert/float(n) : -1);
     dijetExoVtxFrac->push_back(goodVtx ? FromExo/float(n) : -1);
     dijetPosip2dFrac->push_back(goodVtx ? nposip2d/float(n) : -1);
     dijetVtxN1->push_back(goodVtx ? VtxN1 : -1);
     dijetVtxN2->push_back(goodVtx ? VtxN2 : -1);
    
     // do glxy stuff here
     helpers help;
     dijetglxydistall->push_back(goodVtx ? help.AvgDistance(glxysToVertex,lxy) : -1);
     dijetglxydistvtx->push_back(goodVtx ? help.AvgDistance(glxysVertex,lxy) : -1);
     dijetglxyrmsall->push_back(goodVtx ? help.RMS(glxysToVertex,lxy) : -1);
     dijetglxyrmsvtx->push_back(goodVtx ? help.RMS(glxysVertex,lxy) : -1);

     // clusters
     std::vector<std::vector<float> > clusters = help.clusters(glxysToVertex,0.15*lxy);
     std::vector<float> bestcluster = help.bestcluster(clusters,lxy);

     int clrN1=0;
     int clrN2=0;
     for (size_t l=0;l<bestcluster.size();l++){
       float glxy = bestcluster[l];
       for (size_t m=0;m<glxysToVertex.size();m++)
         if(fabs(glxy-glxysToVertex[m])<1e-5){
           if (indicesToVertex[m]==1) clrN1++;
           else clrN2++;
           break;
       }
     }

     dijetglxyrmsclr->push_back(goodVtx ? help.RMS(bestcluster,lxy) : -1);
     dijetglxydistclr->push_back(goodVtx ? help.AvgDistance(bestcluster,lxy) : -1);
     dijetNclusters->push_back(goodVtx ? help.Nclusters(clusters) : -1);
     dijetbestclusterlxy->push_back(goodVtx ? ( (bestcluster.size()>0 ) ? help.Avg(bestcluster)/lxy : -1) : -1);
     dijetbestclusterN->push_back(goodVtx ? bestcluster.size() : -1);
     dijetbestclusterN1->push_back(goodVtx ? clrN1 : -1);
     dijetbestclusterN2->push_back(goodVtx ? clrN2 : -1);

   } 
  }// dijet loop

  iEvent.put(dijetCorrPt,"dijetCorrPt");
  iEvent.put(dijetCorrEta,"dijetCorrEta");
  iEvent.put(dijetCorrPhi,"dijetCorrPhi");
  iEvent.put(dijetCorrMass,"dijetCorrMass");
  iEvent.put(dijetNPromptTracks, "dijetNPromptTracks");
  iEvent.put(dijetNDispTracks, "dijetNDispTracks");
  iEvent.put(dijetPromptEnergyFrac, "dijetPromptEnergyFrac");
  iEvent.put(dijetVtxX,"dijetVtxX");
  iEvent.put(dijetVtxY,"dijetVtxY");
  iEvent.put(dijetVtxZ,"dijetVtxZ");
  iEvent.put(dijetLxy, "dijetLxy");
  iEvent.put(dijetLxysig, "dijetLxysig");
  iEvent.put(dijetVtxChi2,"dijetVtxChi2");
  iEvent.put(dijetVtxmass,"dijetVtxmass");
  iEvent.put(dijetVtxpt,"dijetVtxpt");
  iEvent.put(dijetVtxdR,"dijetVtxdR");
  iEvent.put(dijetVtxN,"dijetVtxN");
  iEvent.put(dijetVtxN1,"dijetVtxN1");
  iEvent.put(dijetVtxN2,"dijetVtxN2");
  iEvent.put(dijetVtxCharge,"dijetVtxCharge");
  iEvent.put(dijetPosip2dFrac,"dijetPosip2dFrac");
  iEvent.put(dijetNAvgHitsInFrontOfVert,"dijetNAvgHitsInFrontOfVert");
  iEvent.put(dijetNAvgMissHitsAfterVert,"dijetNAvgMissHitsAfterVert");
  iEvent.put(dijetExoVtxFrac,"dijetExoVtxFrac");
  iEvent.put(dijetglxydistall,"dijetglxydistall");
  iEvent.put(dijetglxydistvtx,"dijetglxydistvtx");
  iEvent.put(dijetglxydistclr,"dijetglxydistclr");
  iEvent.put(dijetglxyrmsall,"dijetglxyrmsall");
  iEvent.put(dijetglxyrmsvtx,"dijetglxyrmsvtx");
  iEvent.put(dijetglxyrmsclr,"dijetglxyrmsclr");
  iEvent.put(dijetNclusters,"dijetNclusters");
  iEvent.put(dijetbestclusterN,"dijetbestclusterN");
  iEvent.put(dijetbestclusterN1,"dijetbestclusterN1");
  iEvent.put(dijetbestclusterN2,"dijetbestclusterN2");
  iEvent.put(dijetbestclusterlxy,"dijetbestclusterlxy");

}


reco::Candidate::LorentzVector DJ_DiJetVertices::detectorP4(pat::Jet &jet, reco::Vertex &vtx, TransientVertex &tvtx, int CorrectTracks=0){

  reco::Candidate::LorentzVector P4;
  // correct track momentas with pca to the vertex
  const std::vector<reco::PFCandidatePtr> & parts = jet.getPFConstituents();
  for(std::vector<reco::PFCandidatePtr>::const_iterator part = parts.begin(); part!= parts.end(); ++part){
    const reco::PFCandidate *pfCand = part->get();
    if (pfCand->charge() == 0){
      P4 += reco::Jet::physicsP4(vtx.position(),*pfCand,pfCand->vertex());
    } else {
      if (CorrectTracks == 0) P4 += pfCand->p4();
      else if (CorrectTracks == 1) {
        P4 += reco::Jet::physicsP4(vtx.position(),*pfCand,pfCand->vertex());
      }
      else if (CorrectTracks == 2){
        if (pfCand->trackRef().isNull()) continue;
        reco::TransientTrack t_trk = theB->build(pfCand->trackRef());
        //const reco::Track *trk = pfCand->trackRef().get();
        GlobalVector p3 = t_trk.trajectoryStateClosestToPoint(tvtx.position()).momentum();
        P4 += ROOT::Math::LorentzVector<ROOT::Math::PxPyPzM4D<double> >(p3.x(),p3.y(),p3.z(),pfCand->mass());
      }
    }
  }

  return P4;
}

void DJ_DiJetVertices::GetEventInfo(const edm::Event& iEvent, const edm::EventSetup& iSetup){

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

void DJ_DiJetVertices::GetMothers(const HepMC::GenParticle *gp, std::vector<std::pair<int,double> > &moms){

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

