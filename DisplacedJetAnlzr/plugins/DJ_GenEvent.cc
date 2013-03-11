#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_GenEvent.h"

DJ_GenEvent::DJ_GenEvent(const edm::ParameterSet& iConfig) {
  produces <std::vector<int> >         ( "XpdgId"  );
  produces <std::vector<int> >         ( "genqFlavor" );
  produces <std::vector<float> >         ( "genqPt"  );
  produces <std::vector<float> >         ( "genqEta"  );
  produces <std::vector<float> >         ( "genqPhi"  );
  produces <std::vector<float> >         ( "genqLxy"  );
  produces <std::vector<float> >         ( "genqCtau"  );
  produces <std::vector<float> >         ( "genjetPt1"  );
  produces <std::vector<float> >         ( "genjetEta1"  );
  produces <std::vector<float> >         ( "genjetPhi1"  );
  produces <std::vector<float> >         ( "genjetLxy1"  );
  produces <std::vector<float> >         ( "genjetCtau1"  );
  produces <std::vector<float> >         ( "genjetPt2"  );
  produces <std::vector<float> >         ( "genjetEta2"  );
  produces <std::vector<float> >         ( "genjetPhi2"  );
  produces <std::vector<float> >         ( "genjetLxy2"  );
  produces <std::vector<float> >         ( "genjetCtau2"  );
  produces <float>          ( "genHT"  );
  produces <float>          ( "HPt"  );
}

void DJ_GenEvent::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<std::vector<int> > XpdgId ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > genqFlavor ( new std::vector<int> );
  std::auto_ptr<std::vector<float> > genqPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqLxy ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genqCtau ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPt1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEta1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPhi1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetLxy1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCtau1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPt2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEta2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPhi2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetLxy2 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCtau2 ( new std::vector<float> );
  std::auto_ptr<float> genHT ( new float() );
  std::auto_ptr<float> HPt ( new float() );

  try {

    edm::Handle<reco::GenParticleCollection> genParticles;
    iEvent.getByLabel("genParticles",genParticles);

    std::vector<const reco::Candidate*> exo;

    for (unsigned int i = 0; i < genParticles->size(); i++) {
      reco::GenParticleRef p(genParticles,i);
      if (p->status()!=3) continue; //not decaying particles

      int pdgId=abs(p->pdgId());
      if (pdgId==35) *HPt.get()=p->pt();
      if (pdgId!=6001114 && pdgId!=6002114 && pdgId!=6003114) continue;
      exo.push_back(p.get());
      XpdgId->push_back(pdgId);
      //std::cout << "gen quarks" << std::endl;

      unsigned int nDau = p->numberOfDaughters();
      for (unsigned int i = 0; i < nDau; i++) {
        reco::GenParticleRef dau = p->daughterRef(i);
        if (abs(dau->pdgId()>5)) continue;
        float lxy = (dau->daughterRef(0)->vertex()-dau->vertex()).Rho();
        float lxyz = (dau->daughterRef(0)->vertex()-dau->vertex()).R();
        genqFlavor->push_back(abs(dau->pdgId()));
        genqPt->push_back(dau->pt());
        genqPhi->push_back(dau->phi());
        genqEta->push_back(dau->eta());
        genqLxy->push_back(lxy);
        genqCtau->push_back(lxyz*p->mass()/p->p());

        //std::cout << dau->pt() << " " << dau->eta() << " " << dau->phi() << std::endl;

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

        reco::GenJetRef j(genJets, i);
        if (fabs(j->eta())<3 && j->pt()>40) *genHT.get()+=j->pt();

        if (j->pt()<20) continue;
        if (fabs(j->eta())>2) continue;

        //std::cout << "===============================" << std::endl;
        //std::cout << j->pt() <<  " " << j->eta() << " " << j->phi() << std::endl; 

        float exo1Frac=0;
        float exo2Frac=0;
        float pFrac=0;

        std::vector<const reco::GenParticle*> constituents = j->getGenConstituents();
        for (unsigned j = 0; j<constituents.size(); j++){
          const reco::GenParticle* p=constituents.at(j);
          const reco::Candidate* mom=deepMother(p);
          if (mom==exo1) exo1Frac+=p->pt();
          else if (mom==exo2) exo2Frac+=p->pt();
          else pFrac+=p->pt();
        }
        exo1Frac/=j->pt();
        exo2Frac/=j->pt();
        pFrac/=j->pt();
        //std::cout << exo1Frac << " " << exo2Frac << " " << pFrac << std::endl;
      
        if (exo1Frac>0.5){
          genjetPt1->push_back(j->pt());
          genjetEta1->push_back(j->eta());
          genjetPhi1->push_back(j->phi());
          genjetLxy1->push_back(exo1lxy);
          genjetCtau1->push_back(exo1ctau);
        } else if (exo2Frac>0.5){
          genjetPt2->push_back(j->pt());
          genjetEta2->push_back(j->eta());
          genjetPhi2->push_back(j->phi());
          genjetLxy2->push_back(exo2lxy);
          genjetCtau2->push_back(exo2ctau);
        }
      
      }
    }
  } catch (cms::Exception &e) {
    edm::LogError("DJ_GenEvent") << e.what();
  }

  iEvent.put( XpdgId,   "XpdgId"   );
  iEvent.put( genqFlavor,   "genqFlavor"   );
  iEvent.put( genqPt,   "genqPt"   );
  iEvent.put( genqEta,   "genqEta"   );
  iEvent.put( genqPhi,   "genqPhi"   );
  iEvent.put( genqLxy,   "genqLxy"   );
  iEvent.put( genqCtau,   "genqCtau"   );
  iEvent.put( genjetPt1,   "genjetPt1"   );
  iEvent.put( genjetEta1,   "genjetEta1"   );
  iEvent.put( genjetPhi1,   "genjetPhi1"   );
  iEvent.put( genjetLxy1,   "genjetLxy1"   );
  iEvent.put( genjetCtau1,   "genjetCtau1"   );
  iEvent.put( genjetPt2,   "genjetPt2"   );
  iEvent.put( genjetEta2,   "genjetEta2"   );
  iEvent.put( genjetPhi2,   "genjetPhi2"   );
  iEvent.put( genjetLxy2,   "genjetLxy2"   );
  iEvent.put( genjetCtau2,   "genjetCtau2"   );
  iEvent.put( genHT,   "genHT"   );
  iEvent.put( HPt,   "HPt"   );

}

const reco::Candidate* DJ_GenEvent::deepMother(const reco::Candidate* p){

  if (p->pdgId() == 0 or p->mother()==NULL) return p;
  if (p->mother()->pdgId() > 6000000)
    return p->mother();
  else 
    return deepMother(p->mother());

}
