#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_KShorts.h"

DJ_KShorts::DJ_KShorts(const edm::ParameterSet& iConfig) : 
patJetCollectionTag_(iConfig.getParameter<edm::InputTag>("patJetCollectionTag")),
PromptTrackDxyCut_(iConfig.getParameter<double>("PromptTrackDxyCut")),
TrackPtCut_(iConfig.getParameter<double>("TrackPtCut")){

   produces<std::vector<float> > ("ksPt");
   produces<std::vector<float> > ("ksEta");
   produces<std::vector<float> > ("ksPhi");
   produces<std::vector<float> > ("ksMass");
   produces<std::vector<float> > ("ksJetPt");
   produces<std::vector<float> > ("ksTrk1Pt");
   produces<std::vector<float> > ("ksTrk2Pt");
   produces<std::vector<float> > ("ksTrk1IP3d");
   produces<std::vector<float> > ("ksTrk2IP3d");
   produces<std::vector<float> > ("ksTrk1IP2d");
   produces<std::vector<float> > ("ksTrk2IP2d");
   produces<std::vector<float> > ("ksTrk1IP3dsig");
   produces<std::vector<float> > ("ksTrk2IP3dsig");
   produces<std::vector<float> > ("ksTrk1IP2dsig");
   produces<std::vector<float> > ("ksTrk2IP2dsig");
   produces<std::vector<float> > ("ksChi2");
   produces<std::vector<float> > ("ksLxy");
   produces<std::vector<float> > ("ksLxysig");
   produces<std::vector<float> > ("ksLxyz");
   produces<std::vector<float> > ("ksLxyzsig");
   produces<std::vector<float> > ("ksCtau");
   produces<std::vector<float> > ("kscolin");
   produces<std::vector<float> > ("ksIP3d");
   produces<std::vector<float> > ("ksIP3dsig");
   produces<std::vector<float> > ("ksIP2d");
   produces<std::vector<float> > ("ksIP2dsig");

}

void
DJ_KShorts::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   std::auto_ptr<std::vector<float> > ksPt ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksEta ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksPhi ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksMass ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksJetPt ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk1Pt ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk2Pt ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk1IP3d ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk2IP3d ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk1IP2d ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk2IP2d ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk1IP3dsig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk2IP3dsig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk1IP2dsig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksTrk2IP2dsig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksChi2 ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksLxy ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksLxysig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksLxyz ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksLxyzsig( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksCtau ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > kscolin ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksIP3d ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksIP3dsig ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksIP2d ( new std::vector<float> );
   std::auto_ptr<std::vector<float> > ksIP2dsig ( new std::vector<float> );

   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);

   edm::ESHandle<MagneticField> myMF;
   iSetup.get<IdealMagneticFieldRecord>().get(myMF);

   edm::Handle<reco::VertexCompositeCandidateCollection> theKs;
   iEvent.getByLabel( edm::InputTag("myV0Candidates:Kshort"), theKs );

   edm::Handle<std::vector<pat::Jet> > patJetsHandle;
   iEvent.getByLabel(patJetCollectionTag_,patJetsHandle);

   edm::Handle<reco::VertexCollection> recVtxs;
   iEvent.getByLabel("offlinePrimaryVertices", recVtxs);
   pv = recVtxs->front();

   for(size_t i=0;i<theKs->size();i++){
     const reco::VertexCompositeCandidate & Kscand = theKs->at(i);

     if (Kscand.numberOfDaughters()!=2) continue;
     if (Kscand.vertexNormalizedChi2()>7) continue;

     // only inside high pt jet cones
     pat::Jet jet;
     for (size_t i=0;i<patJetsHandle->size();i++){
       pat::Jet j = patJetsHandle->at(i);
       if (deltaR(j.eta(),j.phi(),Kscand.eta(),Kscand.phi())<0.5){
         jet=j;
         break;
       }
     }
     //if (jet.pt()==0) continue;

     // track quality cuts
     reco::TrackRef trk1 = (*(dynamic_cast<const reco::RecoChargedCandidate *> (Kscand.daughter(0))) ).track();
     reco::TrackRef trk2 = (*(dynamic_cast<const reco::RecoChargedCandidate *> (Kscand.daughter(1))) ).track();

     if (trk1->pt() < TrackPtCut_ or trk2->pt() < TrackPtCut_) continue;
     if (!trk1->quality(reco::TrackBase::highPurity)) continue;
     if (!trk2->quality(reco::TrackBase::highPurity)) continue;

     const GlobalVector v0Momentum(Kscand.px(),Kscand.py(),Kscand.pz());
     // track 3D impact parameter sig
     reco::TransientTrack t_trk1 = theB->build(trk1);
     reco::TransientTrack t_trk2 = theB->build(trk2);
     Measurement1D ip3d1 = IPTools::signedImpactParameter3D(t_trk1,v0Momentum,pv).second;
     Measurement1D ip3d2 = IPTools::signedImpactParameter3D(t_trk2,v0Momentum,pv).second;
     Measurement1D ip2d1 = IPTools::signedTransverseImpactParameter(t_trk1,v0Momentum,pv).second;
     Measurement1D ip2d2 = IPTools::signedTransverseImpactParameter(t_trk2,v0Momentum,pv).second;
     // displacement cut
     if ((ip3d1.significance() < 3) || (ip3d2.significance() < 3)) continue;


     // recompute lxy wrt PV
     ROOT::Math::SVector<double,3> v2D(Kscand.vx() - pv.x(),Kscand.vy()-pv.y(),0);
     ROOT::Math::SVector<double,3> v3D(Kscand.vx() - pv.x(),Kscand.vy()-pv.y(),Kscand.vz()-pv.z());
     double lxy = ROOT::Math::Mag(v2D);
     double lxyz = ROOT::Math::Mag(v3D);
     reco::Candidate::CovarianceMatrix matrix = Kscand.vertexCovariance() + pv.covariance();
     float errlxy = sqrt(ROOT::Math::Similarity(matrix,v2D))/lxy;
     float errlxyz = sqrt(ROOT::Math::Similarity(matrix,v3D))/lxyz;
     float lxysig = lxy/errlxy;
     float lxyzsig = lxyz/errlxyz;

     // displacement cut
     if(lxyzsig<5) continue;

     //collinearity
     float reducedlxyz= ( 
             Kscand.px()*(Kscand.vx()-pv.x())
            +Kscand.py()*(Kscand.vy()-pv.y())
            +Kscand.pz()*(Kscand.vz()-pv.z())            
     )/(Kscand.p());
     float colin=reducedlxyz/lxyz; 

     //Kinematic fit
     KinematicParticleFactoryFromTransientTrack pFactory;
     std::vector<RefCountedKinematicParticle> v0Particles;
 
     float piMass=0.13957018;
     float piSigma=piMass*1.e-6;
     v0Particles.push_back(pFactory.particle(t_trk1, piMass, t_trk1.chi2(), t_trk1.ndof(), piSigma));
     v0Particles.push_back(pFactory.particle(t_trk2, piMass, t_trk2.chi2(), t_trk2.ndof(), piSigma));

     KinematicParticleVertexFitter fitter;   							 
     RefCountedKinematicTree v0VertexFitTree=fitter.fit(v0Particles);
     if (v0VertexFitTree->isEmpty()) continue;
     RefCountedKinematicParticle v0FitKinematicParticle = v0VertexFitTree->currentParticle();     
     RefCountedKinematicVertex v0FitKinematicVertex = v0VertexFitTree->currentDecayVertex();

     KinematicState theCurrentKinematicState = v0FitKinematicParticle->currentState();
     FreeTrajectoryState theV0FTS = theCurrentKinematicState.freeTrajectoryState();
     //Neutral v0 candidate transient tracks
     reco::TransientTrack v0TT = (*theB).build(theV0FTS);

     // v0 IP
     Measurement1D v0IP3d = IPTools::signedImpactParameter3D(v0TT, v0Momentum, pv).second;
     Measurement1D v0IP2d = IPTools::signedTransverseImpactParameter(v0TT, v0Momentum, pv).second;
 
     // collinearity cut
     if(fabs(v0IP3d.significance())>3) continue;

     ksChi2->push_back(Kscand.vertexNormalizedChi2());
     ksLxy->push_back(lxy);
     ksLxyz->push_back(lxyz);
     ksLxysig->push_back(lxysig);
     ksLxyzsig->push_back(lxyzsig);
     ksCtau->push_back(lxyz*0.497614/Kscand.p());
     ksPt->push_back(Kscand.pt());
     ksPhi->push_back(Kscand.phi());
     ksEta->push_back(Kscand.eta());
     ksMass->push_back(Kscand.mass());
     ksJetPt->push_back(jet.pt());
     ksTrk1Pt->push_back(trk1->pt());
     ksTrk2Pt->push_back(trk2->pt());
     ksTrk1IP3d->push_back(ip3d1.value());
     ksTrk2IP3d->push_back(ip3d2.value());
     ksTrk1IP2d->push_back(ip2d1.value());
     ksTrk2IP2d->push_back(ip2d2.value());
     ksTrk1IP3dsig->push_back(ip3d1.significance());
     ksTrk2IP3dsig->push_back(ip3d2.significance());
     ksTrk1IP2dsig->push_back(ip2d1.significance());
     ksTrk2IP2dsig->push_back(ip2d2.significance());
     kscolin->push_back(colin);
     ksIP3d->push_back(v0IP3d.value());
     ksIP3dsig->push_back(v0IP3d.significance());
     ksIP2d->push_back(v0IP2d.value());
     ksIP2dsig->push_back(v0IP2d.significance());
   }


  iEvent.put(ksChi2,"ksChi2");
  iEvent.put(ksPt,"ksPt");
  iEvent.put(ksEta,"ksEta");
  iEvent.put(ksPhi,"ksPhi");
  iEvent.put(ksMass,"ksMass");
  iEvent.put(ksJetPt,"ksJetPt");
  iEvent.put(ksTrk1Pt,"ksTrk1Pt");
  iEvent.put(ksTrk2Pt,"ksTrk2Pt");
  iEvent.put(ksLxy,"ksLxy");
  iEvent.put(ksLxysig,"ksLxysig");
  iEvent.put(ksLxyz,"ksLxyz");
  iEvent.put(ksLxyzsig,"ksLxyzsig");
  iEvent.put(ksCtau,"ksCtau");
  iEvent.put(ksTrk1IP3d,"ksTrk1IP3d");
  iEvent.put(ksTrk2IP3d,"ksTrk2IP3d");
  iEvent.put(ksTrk1IP2d,"ksTrk1IP2d");
  iEvent.put(ksTrk2IP2d,"ksTrk2IP2d");
  iEvent.put(ksTrk1IP3dsig,"ksTrk1IP3dsig");
  iEvent.put(ksTrk2IP3dsig,"ksTrk2IP3dsig");
  iEvent.put(ksTrk1IP2dsig,"ksTrk1IP2dsig");
  iEvent.put(ksTrk2IP2dsig,"ksTrk2IP2dsig");
  iEvent.put(kscolin,"kscolin");
  iEvent.put(ksIP3d,"ksIP3d");
  iEvent.put(ksIP3dsig,"ksIP3dsig");
  iEvent.put(ksIP2d,"ksIP2d");
  iEvent.put(ksIP2dsig,"ksIP2dsig");

}


