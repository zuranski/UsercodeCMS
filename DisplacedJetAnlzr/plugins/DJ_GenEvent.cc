#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_GenEvent.h"

DJ_GenEvent::DJ_GenEvent(const edm::ParameterSet& iConfig) {
  produces <std::vector<float> >         ( "genjetPt"  );
  produces <std::vector<float> >         ( "genjetEta"  );
  produces <std::vector<float> >         ( "genjetPhi"  );
  produces <std::vector<float> >         ( "genjetLxy"  );
  produces <std::vector<float> >         ( "genjetCtau"  );
}

void DJ_GenEvent::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<std::vector<float> > genjetPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetLxy ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > genjetCtau ( new std::vector<float> );

  try {

    edm::Handle<edm::HepMCProduct> EvtHandle;
    iEvent.getByLabel("generator",EvtHandle);

    //get HepMC event
    const HepMC::GenEvent* Evt = EvtHandle->GetEvent();

    for(HepMC::GenEvent::particle_const_iterator p = Evt->particles_begin(); p != Evt->particles_end(); ++p){
      if((abs((*p)->pdg_id()) == 6000111 || abs((*p)->pdg_id()) == 6000112 ) && (*p)->status()==3){ // Exotics found

        HepMC::GenParticle *exo = *p;
        HepMC::GenVertex *Xvtx = exo->end_vertex();
        reco::Candidate::LorentzVector exop4( exo->momentum() );

        for(HepMC::GenVertex::particles_out_const_iterator pout = Xvtx->particles_out_const_begin(); pout != Xvtx->particles_out_const_end(); pout++){
          if ((*pout)->pdg_id()>6) continue;
 
          HepMC::GenParticle *q = *pout;
          reco::Candidate::LorentzVector qp4(q->momentum());
          reco::Candidate::LorentzVector qx4(q->end_vertex()->position());

          genjetPt->push_back(qp4.pt());
          genjetPhi->push_back(qp4.phi());
          genjetEta->push_back(qp4.eta());
          genjetLxy->push_back(qx4.Pt());
          genjetCtau->push_back(qx4.P()*exop4.mass()/exop4.P());
        
        }
      }
    }

  } catch (cms::Exception &e) {
    edm::LogError("DJ_GenEvent") << e.what();
  }

  iEvent.put( genjetPt,   "genjetPt"   );
  iEvent.put( genjetEta,   "genjetEta"   );
  iEvent.put( genjetPhi,   "genjetPhi"   );
  iEvent.put( genjetLxy,   "genjetLxy"   );
  iEvent.put( genjetCtau,   "genjetCtau"   );

}
