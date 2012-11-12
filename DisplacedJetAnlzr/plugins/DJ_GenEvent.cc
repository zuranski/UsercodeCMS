#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_GenEvent.h"

DJ_GenEvent::DJ_GenEvent(const edm::ParameterSet& iConfig) {
  produces <std::vector<int> >         ( "XpdgId"  );
  produces <std::vector<int> >         ( "genjetFlavor" );
  produces <std::vector<float> >         ( "genjetPt"  );
  produces <std::vector<float> >         ( "genjetEta"  );
  produces <std::vector<float> >         ( "genjetPhi"  );
  produces <std::vector<float> >         ( "genjetLxy"  );
  produces <std::vector<float> >         ( "genjetCtau"  );
}

void DJ_GenEvent::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<std::vector<int> > XpdgId ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > genjetFlavor ( new std::vector<int> );
  std::auto_ptr<std::vector<float> > genjetPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetLxy ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCtau ( new std::vector<float> );

  try {

    edm::Handle<reco::GenParticleCollection> genParticles;
    iEvent.getByLabel("genParticles",genParticles);

    for (unsigned int i = 0; i < genParticles->size(); i++) {

      reco::GenParticleRef p(genParticles, i);
      if (p->status()!=3) continue; //not decaying particles

      int pdgId=abs(p->pdgId());
      if (pdgId!=6001114 && pdgId!=6002114 && pdgId!=6003114) continue;
      XpdgId->push_back(pdgId);

      unsigned int nDau = p->numberOfDaughters();
      for (unsigned int i = 0; i < nDau; i++) {
        reco::GenParticleRef dau = p->daughterRef(i);
        if (abs(dau->pdgId()>5)) continue;
        float lxy = (dau->daughterRef(0)->vertex()-dau->vertex()).Rho();
        float lxyz = (dau->daughterRef(0)->vertex()-dau->vertex()).R();
        genjetFlavor->push_back(abs(dau->pdgId()));
        genjetPt->push_back(dau->pt());
        genjetPhi->push_back(dau->phi());
        genjetEta->push_back(dau->eta());
        genjetLxy->push_back(lxy);
        genjetCtau->push_back(lxyz*p->mass()/p->p());
      }
    }
  } catch (cms::Exception &e) {
    edm::LogError("DJ_GenEvent") << e.what();
  }

  iEvent.put( XpdgId,   "XpdgId"   );
  iEvent.put( genjetFlavor,   "genjetFlavor"   );
  iEvent.put( genjetPt,   "genjetPt"   );
  iEvent.put( genjetEta,   "genjetEta"   );
  iEvent.put( genjetPhi,   "genjetPhi"   );
  iEvent.put( genjetLxy,   "genjetLxy"   );
  iEvent.put( genjetCtau,   "genjetCtau"   );

}
