// Package:    DisplacedJetAnlzr
// Class:      DisplacedJetAnlzr
// 

//
// Original Author:  Andrzej Zuranski
//         Created:  Thu Feb 16 09:43:08 CST 2012


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Trigger
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

//File Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

//My Data Formats
#include "MyAnalysis/DisplacedJetAnlzr/interface/exotic.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/genjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjet.h"

//EDM Data Formats
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/ParticleFlowReco/interface/PFDisplacedVertex.h"

//Transient Tracks
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"


class DisplacedJetAnlzr : public edm::EDAnalyzer {
   public:
      explicit DisplacedJetAnlzr(const edm::ParameterSet&);
      ~DisplacedJetAnlzr();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------
      TTree *tree;
      std::vector<std::string> triggers;
      std::vector<exotic> Xs;
      std::vector<genjet> gjets;
      std::vector<pfjet> pfjets;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DisplacedJetAnlzr::DisplacedJetAnlzr(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   tree = fs->make<TTree>("tree","tree");

}


DisplacedJetAnlzr::~DisplacedJetAnlzr()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DisplacedJetAnlzr::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

// Clear variables
   triggers.clear();Xs.clear();gjets.clear();pfjets.clear();

// Triggers

   HLTConfigProvider hltConfig;
   bool changed;
   hltConfig.init(iEvent.getRun(),iSetup,"hltreco",changed);

   edm::Handle<edm::TriggerResults> hltResults;
   iEvent.getByLabel(edm::InputTag("TriggerResults","","hltreco"),hltResults);
   const std::vector< std::string > &trgNames = hltConfig.triggerNames();

   for (size_t i=0;i<hltResults->size();i++)
	if (hltResults->accept(i) && trgNames.at(i).find("DisplacedPFJet") != std::string::npos)
	 triggers.push_back(trgNames.at(i));

   // no DisplacedPFJet trigger fired.. so sad
   if (triggers.size() == 0 ) return;

// generator information

  if (!iEvent.isRealData()){

  Handle<HepMCProduct> EvtHandle;
  iEvent.getByLabel("generator",EvtHandle);

  //get HepMC event
  const HepMC::GenEvent* Evt = EvtHandle->GetEvent();

    for(HepMC::GenEvent::particle_const_iterator p = Evt->particles_begin(); p != Evt->particles_end(); ++p){
      if((abs((*p)->pdg_id()) == 6000111 || abs((*p)->pdg_id()) == 6000112 ) && (*p)->status()==3){ // Exotics found

        exotic X;
	HepMC::GenParticle *exo = *p;
        HepMC::GenVertex *Xvtx = exo->end_vertex();

        reco::Candidate::LorentzVector exop4( exo->momentum() );
        X.pt = exop4.pt();
        X.phi = exop4.phi();
        X.eta = exop4.eta();
	X.mass = exop4.mass();

        for(HepMC::GenVertex::particles_out_const_iterator pout = Xvtx->particles_out_const_begin(); pout != Xvtx->particles_out_const_end(); pout++){
	  if ((*pout)->pdg_id()>6) continue;
	 
	  genjet gj;
	  HepMC::GenParticle *q = *pout;

          reco::Candidate::LorentzVector qp4(q->momentum());
          gj.pt = qp4.pt();
	  gj.phi = qp4.phi();
	  gj.eta = qp4.eta();
	  reco::Candidate::LorentzVector qx4(q->end_vertex()->position());
	  double lxy = qx4.Pt();
	  gj.lxy = lxy;
	  X.lxy = lxy;
	  X.ctau = qx4.P()*exop4.mass()/exop4.P();

          gjets.push_back(gj);
        }

        Xs.push_back(X);
      }

    }
  }

// Trigger objects ... for later



// PFJets

   edm::Handle<reco::PFJetCollection> pfjetsh;
   iEvent.getByLabel("ak5PFJets",pfjetsh);

   edm::ESHandle<TransientTrackBuilder> theB;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);

   for (reco::PFJetCollection::const_iterator j = pfjetsh->begin(); j != pfjetsh->end();++j){

     if (j->pt()<40 || fabs(j->eta())>2) continue;

     pfjet pfj;

     pfj.energy = j->energy();
     pfj.pt = j->pt();
     pfj.eta = j->eta();
     pfj.phi = j->phi();

     pfj.chgHadFrac = j->chargedHadronEnergyFraction();
     pfj.chgHadN = j->chargedHadronMultiplicity();
     pfj.neuHadFrac = j->neutralHadronEnergyFraction();
     pfj.neuHadN = j->neutralMultiplicity();
     pfj.phFrac = j->photonEnergyFraction();
     pfj.phN = j->photonMultiplicity();
     pfj.eleFrac = j->electronEnergyFraction();
     pfj.eleN = j->electronMultiplicity();
     pfj.muFrac = j->muonEnergyFraction();
     pfj.muN = j->muonMultiplicity();

     pfjets.push_back(pfj);

     reco::TrackRefVector jtrks = j->getTrackRefs();
     std::vector<reco::TransientTrack> goodtrks;
     for (size_t i=0;i<jtrks.size();i++){
	if (jtrks[i]->pt() < 1.) continue;
	reco::Track trk = *jtrks[i].get();
        goodtrks.push_back(theB->build(trk));
     }

     std::cout << goodtrks.size() << std::endl;

   }


// play with PF secondary vertices 
   edm::Handle<std::vector<reco::PFDisplacedVertex> > pfvtxsh;
   iEvent.getByLabel("particleFlowDisplacedVertex",pfvtxsh);


   for (size_t i=0; i<pfvtxsh->size(); i++){
     reco::PFDisplacedVertex v = pfvtxsh->at(i);
     v.Dump();
   }


   tree->Fill();
   return;
}


// ------------ method called once each job just before starting event loop  ------------
void 
DisplacedJetAnlzr::beginJob()
{
tree->Branch("triggers",&triggers);
tree->Branch("Xs",&Xs);
tree->Branch("gjets",&gjets);
tree->Branch("pfjets",&pfjets);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DisplacedJetAnlzr::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
DisplacedJetAnlzr::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DisplacedJetAnlzr::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
DisplacedJetAnlzr::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
DisplacedJetAnlzr::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DisplacedJetAnlzr::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedJetAnlzr);
