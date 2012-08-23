#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_GenEvent.h"

DJ_GenEvent::DJ_GenEvent(const edm::ParameterSet& iConfig) {
  produces <std::vector<genjet> >         ( "gjets"  );
}

void DJ_GenEvent::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<std::vector<genjet> > gjets ( new std::vector<genjet> );

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
 
          genjet gj;

          HepMC::GenParticle *q = *pout;
          reco::Candidate::LorentzVector qp4(q->momentum());
          reco::Candidate::LorentzVector qx4(q->end_vertex()->position());

          gj.pt = qp4.pt();
          gj.phi = qp4.phi();
          gj.eta = qp4.eta();
          gj.lxy = qx4.Pt();
          gj.ctau = qx4.P()*exop4.mass()/exop4.P();
        
          gjets->push_back(gj);

        }
      }
    }

  } catch (cms::Exception &e) {
    edm::LogError("DJ_GenEvent") << e.what();
  }

  iEvent.put( gjets,   "gjets"   );

}
