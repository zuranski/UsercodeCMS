// -*- C++ -*-
//
// Package:    MyPythiaFilter
// Class:      MyPythiaFilter
// 
/**\class MyPythiaFilter MyPythiaFilter.cc Analysis/MyPythiaFilter/src/MyPythiaFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andrzej Zuranski,Address unknown,NONE,
//         Created:  Tue May 25 16:46:17 EDT 2010
// $Id$
//
//


// system include files
#include <memory>
#include <iostream>
#include <vector>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

//
// class declaration
//

class MyPythiaFilter : public edm::EDFilter {
   public:
      explicit MyPythiaFilter(const edm::ParameterSet&);
      ~MyPythiaFilter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      void assignStableDaughters(HepMC::GenParticle* p, std::vector<HepMC::GenParticle*> & daughters);
       
      bool Kpi,K3pi;
      // ----------member data ---------------------------
};

//
// constructors and destructor
//
MyPythiaFilter::MyPythiaFilter(const edm::ParameterSet& iConfig):
  K3pi(iConfig.getParameter<bool>("K3pi")),
  Kpi(iConfig.getParameter<bool>("Kpi"))

{

   //now do what ever initialization is needed
}


MyPythiaFilter::~MyPythiaFilter()
{
 
}


//
// member functions
//

void MyPythiaFilter::assignStableDaughters(HepMC::GenParticle* p, std::vector<HepMC::GenParticle*> & daughters){


  for(HepMC::GenVertex::particles_out_const_iterator pout = p->end_vertex()->particles_out_const_begin(); pout != p->end_vertex()->particles_out_const_end(); pout++){
    if((*pout)->status() == 1){
      daughters.push_back(*pout);
    }
    else{
      assignStableDaughters((*pout),daughters);
    }
  }

  return;
}

// ------------ method called on each new Event  ------------
bool
MyPythiaFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
 
  if(Kpi && K3pi) return false;

  Handle<HepMCProduct> EvtHandle;
  iEvent.getByLabel("generator",EvtHandle);

  //get HepMC event
  const HepMC::GenEvent* Evt = EvtHandle->GetEvent();


  for(HepMC::GenEvent::particle_const_iterator p = Evt->particles_begin(); p != Evt->particles_end(); ++p){
    if(abs((*p)->pdg_id()) == 413){ // Dstar found
      HepMC::GenVertex *DSVtx = (*p)->end_vertex();
      HepMC::GenParticle *D0=0,*Spi=0;
      HepMC::GenVertex *D0Vtx=0;
      for(HepMC::GenVertex::particles_out_const_iterator dsout = DSVtx->particles_out_const_begin(); dsout != DSVtx->particles_out_const_end(); dsout++){
      	if(abs((*dsout)->pdg_id()) == 421){//D0 found
           D0 = *dsout;
           D0Vtx = (*dsout)->end_vertex();
         }
         if(abs((*dsout)->pdg_id()) == 211)//slow pi found
           Spi = *dsout;
      }

      if(D0!=0 && D0Vtx!=0 && Spi!=0){

        vector<HepMC::GenParticle*> D0daus;
        vector<int> D0dauspids;

        //find stable daughters of D0, requires recurrenctial loop
        assignStableDaughters(D0,D0daus);

        for(unsigned int i=0;i<D0daus.size();i++){
          HepMC::GenParticle* part = D0daus[i];
          D0dauspids.push_back(abs(part->pdg_id()));
        }


        // find Kpi and K3pi channels only
        int K_num=0;
        int pi_num=0;
        while (!D0dauspids.empty()){
          int pid = D0dauspids.back();
          if(pid==321)
            K_num++;
          if(pid==211)
            pi_num++;
          D0dauspids.pop_back();
        }

        if(D0daus.size()==2 && K_num==1 && pi_num==1 && Kpi) return true;
        if(D0daus.size()==4 && K_num==1 && pi_num==3 && K3pi) return true;

      }
    }
  }  


  return false;
}

// ------------ method called once each job just before starting event loop  ------------
void 
MyPythiaFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MyPythiaFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(MyPythiaFilter);
