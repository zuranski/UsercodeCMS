#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_GenEvent.h"

DJ_GenEvent::DJ_GenEvent(const edm::ParameterSet& iConfig) {
  produces <std::vector<int> >         ( "XpdgId"  );
  produces <std::vector<float> >         ( "XPt"  );
  produces <std::vector<float> >         ( "XPhi"  );
  produces <std::vector<float> >         ( "XEta"  );
  produces <std::vector<float> >         ( "XMass"  );
  produces <std::vector<int> >         ( "genqFlavor" );
  produces <std::vector<int> >         ( "genqNLep" );
  produces <std::vector<float> >         ( "genqPt"  );
  produces <std::vector<float> >         ( "genqEta"  );
  produces <std::vector<float> >         ( "genqPhi"  );
  produces <std::vector<float> >         ( "genqLxy"  );
  produces <std::vector<float> >         ( "genqCtau"  );
  produces <std::vector<float> >         ( "genqIP2d"  );
  produces <std::vector<float> >         ( "genqIP3d"  );
  produces <std::vector<float> >         ( "genqBlxyz"  );
  produces <std::vector<float> >         ( "genjetEnergy1"  );
  produces <std::vector<float> >         ( "genjetPt1"  );
  produces <std::vector<float> >         ( "genjetEta1"  );
  produces <std::vector<float> >         ( "genjetPhi1"  );
  produces <std::vector<float> >         ( "genjetLxy1"  );
  produces <std::vector<float> >         ( "genjetCtau1"  );
  produces <std::vector<float> >         ( "genjetAngle1"  );
  produces <std::vector<float> >         ( "genjetCorr1"  );
  produces <std::vector<float> >         ( "genjetEnergy2"  );
  produces <std::vector<float> >         ( "genjetPt2"  );
  produces <std::vector<float> >         ( "genjetEta2"  );
  produces <std::vector<float> >         ( "genjetPhi2"  );
  produces <std::vector<float> >         ( "genjetLxy2"  );
  produces <std::vector<float> >         ( "genjetCtau2"  );
  produces <std::vector<float> >         ( "genjetAngle2"  );
  produces <std::vector<float> >         ( "genjetCorr2"  );
  produces <std::vector<float> >         ( "SqPt"  );
  produces <std::vector<float> >         ( "SqPhi"  );
  produces <std::vector<float> >         ( "SqEta"  );
  produces <std::vector<float> >         ( "SqMass"  );
  produces <float>          ( "genHT"  );
  produces <float>          ( "HPt"  );
  produces <float>          ( "HPhi"  );
  produces <float>          ( "HEta"  );
  produces <float>          ( "HMass"  );
  produces <bool>          ( "SqSq"  );
}

void DJ_GenEvent::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<std::vector<int> > XpdgId ( new std::vector<int> );
  std::auto_ptr<std::vector<float> > XPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > XPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > XEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > XMass ( new std::vector<float> );
  std::auto_ptr<std::vector<int> > genqFlavor ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > genqNLep ( new std::vector<int> );
  std::auto_ptr<std::vector<float> > genqPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqLxy ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqCtau ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqIP2d ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqIP3d ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqBlxyz ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEnergy1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPt1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEta1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPhi1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetLxy1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCtau1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetAngle1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCorr1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEnergy2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPt2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEta2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPhi2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetLxy2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCtau2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetAngle2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCorr2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > SqPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > SqPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > SqEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > SqMass ( new std::vector<float> );
  std::auto_ptr<float> genHT ( new float() );
  std::auto_ptr<float> HPt ( new float() );
  std::auto_ptr<float> HPhi ( new float() );
  std::auto_ptr<float> HEta ( new float() );
  std::auto_ptr<float> HMass ( new float() );
  std::auto_ptr<bool> SqSq( new bool(true) );

  try {

    edm::Handle<reco::GenParticleCollection> genParticles;
    iEvent.getByLabel("genParticles",genParticles);

    std::vector<const reco::Candidate*> exo;

    for (unsigned int i = 0; i < genParticles->size(); i++) {
      reco::GenParticleRef p(genParticles,i);
      if (p->status()!=3) continue; //not decaying particles

      int pdgId=abs(p->pdgId());
      // Higgs
      if (pdgId==35) {
        *HPt.get()=p->pt();
        *HPhi.get()=p->phi();
        *HEta.get()=p->eta();
        *HMass.get()=p->mass();
      }
      /*
      if (abs(pdgId)>1000000) {
        std::cout << pdgId << ": " ; 
        for (unsigned int i=0;i<p->numberOfDaughters();i++)
	  std::cout << p->daughter(i)->pdgId() << " " ;
        std::cout << std::endl;
      }
      */
      // squarks
      if ((pdgId>1000000 && pdgId<1000005) || (pdgId>2000000 && pdgId<2000005)) {
        if (p->pdgId()<0) *SqSq.get()=false;
        SqPt->push_back(p->pt());
        SqPhi->push_back(p->phi());
        SqEta->push_back(p->eta());
        SqMass->push_back(p->mass());
      }


      if (pdgId!=6001114 && pdgId!=6002114 && pdgId!=6003114      // emu
      && pdgId!=6001113 && pdgId!=6002113 && pdgId!=6003113 && pdgId!=1000022) continue;
      exo.push_back(p.get());
      XpdgId->push_back(pdgId);
      XPt->push_back(p->pt());
      XPhi->push_back(p->phi());
      XEta->push_back(p->eta());
      XMass->push_back(p->mass());

      unsigned int nDau = p->numberOfDaughters();
      for (unsigned int i = 0; i < nDau; i++) {
        const reco::Candidate* dau = p->daughter(i);
        if (abs(dau->pdgId()>1000000)) continue;
        float lxy = (dau->daughter(0)->vertex()-dau->vertex()).Rho();
        float lxyz = (dau->daughter(0)->vertex()-dau->vertex()).R();
	float dPhi = deltaPhi(dau->phi(),p->phi());
	float dR = deltaR(dau->eta(),dau->phi(),p->eta(),p->phi());
	float ipxy=lxy*fabs(sin(dPhi));
	float ipxyz=lxyz*fabs(sin(dR));
        genqFlavor->push_back(abs(dau->pdgId()));
        genqPt->push_back(dau->pt());
        genqPhi->push_back(dau->phi());
        genqEta->push_back(dau->eta());
        genqLxy->push_back(lxy);
        genqCtau->push_back(lxyz*p->mass()/p->p());
	genqIP2d->push_back(ipxy);
	genqIP3d->push_back(ipxyz);
	

        int nleptons = -1;
        float blxyz = -1.;

        if (abs(dau->pdgId())==5) {

  	  // find B-mesons or B-baryons
	  std::vector<const reco::Candidate*> Bs;
          FindBDaughter(dau,Bs);
          std::sort(Bs.begin(),Bs.end());
	  Bs.erase(std::unique(Bs.begin(),Bs.end()),Bs.end());

	  // get the correct B wrt quark or antiquark
	  std::vector<const reco::Candidate*> B = FindB(Bs,dau->pdgId());	

	  if (B.size()>0){ 
	    const reco::Candidate* b = B.at(0);
  	    std::vector<int> pids;
            assignStableDaughters(b,pids);
  	    int nel=std::count(pids.begin(),pids.end(),11);
	    int nmu=std::count(pids.begin(),pids.end(),13);
	    int ntau=std::count(pids.begin(),pids.end(),15);
	    nleptons = nel+nmu+ntau;
	    if (b->daughter(0)->numberOfDaughters()>0)
	      blxyz = (dau->daughter(0)->vertex() - b->daughter(0)->daughter(0)->vertex()).R();
	    else
	      blxyz = (dau->daughter(0)->vertex() - b->daughter(0)->vertex()).R();
          }
        }

	genqNLep->push_back(nleptons);
	genqBlxyz->push_back(blxyz);

      }
    }

    if (exo.size()==2){
      const reco::Candidate* exo1=exo.at(0);
      const reco::Candidate* exo2=exo.at(1);
      float exo1lxy = (exo1->daughter(0)->daughter(0)->vertex()-exo1->daughter(0)->vertex()).Rho();
      float exo2lxy = (exo2->daughter(0)->daughter(0)->vertex()-exo1->daughter(0)->vertex()).Rho();
      float exo1ctau = (exo1->daughter(0)->daughter(0)->vertex()-exo1->daughter(0)->vertex()).R()*exo1->mass()/exo1->p();
      float exo2ctau = (exo2->daughter(0)->daughter(0)->vertex()-exo1->daughter(0)->vertex()).R()*exo2->mass()/exo2->p();

      edm::Handle<reco::GenJetCollection> genJets;
      iEvent.getByLabel("ak5GenJets",genJets);
    

      *genHT.get()=0;
      for (unsigned int i=0; i<genJets->size();i++) {

	const reco::GenJet &j = genJets->at(i);
        if (fabs(j.eta())<3 && j.pt()>40) *genHT.get()+=j.pt();

        if (j.pt()<20) continue;
        if (fabs(j.eta())>2) continue;

        //std::cout << "===============================" << std::endl;
        //std::cout << j->pt() <<  " " << j->eta() << " " << j->phi() << " " << j->getGenConstituents().size() << std::endl; 

	// check if that's a hadronic jet
	int nconst=0;
        std::vector<const reco::GenParticle*> constituents = j.getGenConstituents();
        // that's a lepton
        if (constituents.at(0)->pt() > 0.5*j.pt()) continue;
        for (unsigned k = 0; k<constituents.size(); k++){
          const reco::GenParticle* p=constituents.at(k);
	  if (p->pt()<1) continue;
	  nconst+=1;
        }

        float exo1Frac=0;
        float exo2Frac=0;
        float pFrac=0;
	float totPt=0;

        for (unsigned k = 0; k<constituents.size(); k++){
          const reco::GenParticle* p=constituents.at(k);
	  if (p->pt()<1) continue;
	  //std::cout << p->pdgId() << " " << p->pt() << std::endl;
          const reco::Candidate* mom=deepMother(p);
          totPt+=p->pt();
          if (mom==exo1) exo1Frac+=p->pt();
          else if (mom==exo2) exo2Frac+=p->pt();
          else pFrac+=p->pt();
        }
        exo1Frac/=totPt;
        exo2Frac/=totPt;
        pFrac/=totPt;
	//std::cout << XpdgId->at(0) << " " << XpdgId->at(1) << std::endl;
        //std::cout << exo1Frac << " " << exo2Frac << " " << pFrac << std::endl;
      
        if (exo1Frac>0.5){

	  reco::Candidate::LorentzVector pP4;
          pP4 = j.physicsP4(exo1->daughter(0)->daughter(0)->vertex(),j,j.vertex());
          float cos = (pP4.px()*j.px()+pP4.py()*j.py()+pP4.pz()*j.pz())/(pP4.P()*j.p());
          float appAngle = acos(cos)*180/3.14159265359; 
          float correction = pP4.pt()/j.pt();

          genjetEnergy1->push_back(j.energy());
          genjetPt1->push_back(j.pt());
          genjetEta1->push_back(j.eta());
          genjetPhi1->push_back(j.phi());
          genjetLxy1->push_back(exo1lxy);
          genjetCtau1->push_back(exo1ctau);
          genjetAngle1->push_back(appAngle);
          genjetCorr1->push_back(correction);

        } else if (exo2Frac>0.5){

	  reco::Candidate::LorentzVector pP4;
          pP4 = j.physicsP4(exo2->daughter(0)->daughter(0)->vertex(),j,j.vertex());
          float cos = (pP4.px()*j.px()+pP4.py()*j.py()+pP4.pz()*j.pz())/(pP4.P()*j.p());
          float appAngle = acos(cos)*180/3.14159265359;
          float correction = pP4.pt()/j.pt();
 
          genjetEnergy2->push_back(j.energy());
          genjetPt2->push_back(j.pt());
          genjetEta2->push_back(j.eta());
          genjetPhi2->push_back(j.phi());
          genjetLxy2->push_back(exo2lxy);
          genjetCtau2->push_back(exo2ctau);
          genjetAngle2->push_back(appAngle);
          genjetCorr2->push_back(correction);
        }
      
      }
    }
  } catch (cms::Exception &e) {
    edm::LogError("DJ_GenEvent") << e.what();
  }

  iEvent.put( XpdgId,   "XpdgId"   );
  iEvent.put( XPt,   "XPt"   );
  iEvent.put( XPhi,   "XPhi"   );
  iEvent.put( XEta,   "XEta"   );
  iEvent.put( XMass,   "XMass"   );
  iEvent.put( genqFlavor,   "genqFlavor"   );
  iEvent.put( genqNLep,   "genqNLep"   );
  iEvent.put( genqPt,   "genqPt"   );
  iEvent.put( genqEta,   "genqEta"   );
  iEvent.put( genqPhi,   "genqPhi"   );
  iEvent.put( genqLxy,   "genqLxy"   );
  iEvent.put( genqCtau,   "genqCtau"   );
  iEvent.put( genqIP2d,   "genqIP2d"   );
  iEvent.put( genqIP3d,   "genqIP3d"   );
  iEvent.put( genqBlxyz,   "genqBlxyz"   );
  iEvent.put( genjetEnergy1,   "genjetEnergy1"   );
  iEvent.put( genjetPt1,   "genjetPt1"   );
  iEvent.put( genjetEta1,   "genjetEta1"   );
  iEvent.put( genjetPhi1,   "genjetPhi1"   );
  iEvent.put( genjetLxy1,   "genjetLxy1"   );
  iEvent.put( genjetCtau1,   "genjetCtau1"   );
  iEvent.put( genjetAngle1,   "genjetAngle1"   );
  iEvent.put( genjetCorr1,   "genjetCorr1"   );
  iEvent.put( genjetEnergy2,   "genjetEnergy2"   );
  iEvent.put( genjetPt2,   "genjetPt2"   );
  iEvent.put( genjetEta2,   "genjetEta2"   );
  iEvent.put( genjetPhi2,   "genjetPhi2"   );
  iEvent.put( genjetLxy2,   "genjetLxy2"   );
  iEvent.put( genjetCtau2,   "genjetCtau2"   );
  iEvent.put( genjetAngle2,   "genjetAngle2"   );
  iEvent.put( genjetCorr2,   "genjetCorr2"   );
  iEvent.put( SqPt,   "SqPt"   );
  iEvent.put( SqPhi,   "SqPhi"   );
  iEvent.put( SqEta,   "SqEta"   );
  iEvent.put( SqMass,   "SqMass"   );
  iEvent.put( genHT,   "genHT"   );
  iEvent.put( HPt,   "HPt"   );
  iEvent.put( HEta,   "HEta"   );
  iEvent.put( HPhi,   "HPhi"   );
  iEvent.put( HMass,   "HMass"   );
  iEvent.put( SqSq,   "SqSq"   );

}

const reco::Candidate* DJ_GenEvent::deepMother(const reco::Candidate* p){

  if (p->pdgId() == 0 or p->mother()==NULL) return p;
  if (p->mother()->pdgId() > 1000000)
    return p->mother();
  else 
    return deepMother(p->mother());

}

void DJ_GenEvent::FindBDaughter(const reco::Candidate* p, std::vector<const reco::Candidate*> & Bs){
 
  for(size_t i=0;i<p->numberOfDaughters();i++){
    const reco::Candidate* dau = p->daughter(i);
    if (dau->status()==1) continue;
    int pdgId = dau->pdgId();
    //std::cout << pdgId << std::endl;	
    if ((abs(pdgId)>500 && abs(pdgId)<600) || ( abs(pdgId)>5000 && abs(pdgId)<6000 )) {
      Bs.push_back(dau);
     } else {
      FindBDaughter(dau,Bs);
    }
  }
  return;

}

void DJ_GenEvent::assignStableDaughters(const reco::Candidate* p, std::vector<int> & pids){

  for(size_t i=0;i<p->numberOfDaughters();i++){
    const reco::Candidate* dau = p->daughter(i);
    if(dau->status()==1 && dau->pdgId() != 22)
      pids.push_back(abs(dau->pdgId()));
    else
     assignStableDaughters(dau,pids);
  }
  return;
}

template <typename T> int sgn(T val){
  return (T(0) < val) - (val < T(0));
}

std::vector<const reco::Candidate*> DJ_GenEvent::FindB(std::vector<const reco::Candidate*> Bs, int pdgId){

  std::vector<const reco::Candidate*> B;
  for (unsigned int i=0;i<Bs.size();i++){
    if (abs(Bs.at(i)->pdgId())<1000) // B-meson
      if (sgn(Bs.at(i)->pdgId())==-1*sgn(pdgId)) B.push_back(Bs.at(i));
      if (sgn(Bs.at(i)->pdgId())==sgn(pdgId)) B.push_back(Bs.at(i));
  }
  return B;
} 
