// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Data formats
#include "HLTrigger/HLTanalyzers/interface/HLTJets.h"
#include "HLTrigger/HLTanalyzers/interface/HLTTrack.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

#include "SimDataFormats/Track/interface/SimTrack.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertex.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"


#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

//L1Trigger
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"

//File Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

#include "MyAnalysis/DisplacedJetTrigger/interface/jet.h"
#include "MyAnalysis/DisplacedJetTrigger/interface/pfjet.h"

//
// class declaration
//


class TriggerTuple : public edm::EDAnalyzer {
   public:
      explicit TriggerTuple(const edm::ParameterSet&);
      ~TriggerTuple();

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

      TTree* tree;
      bool l1HTT50,l1HTT75,l1HTT100,l1HTT150;
      double ht,l1ht;
      int nPixVtx;
      std::vector<jet> jets;
      std::vector<jet> l1jets;
      std::vector<pfjet> pfjets;
      std::vector<double> genJetPt,genJetEta,genJetPhi,XPt,XEta,XPhi,XLifeTime,Xlxy;
      std::vector<std::string> triggers; 
      edm::InputTag jets_,l1jets_,vertices_,tracks_,l1tracks_,pfjets_,pftracks_;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//
// constructors and destructor
//
TriggerTuple::TriggerTuple(const edm::ParameterSet& iConfig)

{
   jets_ = iConfig.getParameter<edm::InputTag>("jets");
   l1jets_ = iConfig.getParameter<edm::InputTag>("l1jets");
   vertices_ = iConfig.getParameter<edm::InputTag>("vertices");
   tracks_ = iConfig.getParameter<edm::InputTag>("tracks");
   l1tracks_ = iConfig.getParameter<edm::InputTag>("l1tracks");
   pftracks_ = iConfig.getParameter<edm::InputTag>("pftracks");
   pfjets_ = iConfig.getParameter<edm::InputTag>("pfjets");

   edm::Service<TFileService> fs;
   tree = fs->make<TTree>("tree","tree");
}


TriggerTuple::~TriggerTuple()
{
}

// ------------ method called for each event  ------------
void
TriggerTuple::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

// clear variables
   l1HTT50=0;l1HTT75=0;l1HTT100=0;l1HTT150=0;
   ht = 0; l1ht = 0; nPixVtx=0;
   jets.clear(); pfjets.clear(); l1jets.clear();
   genJetPt.clear(); genJetEta.clear();genJetPhi.clear();
   XPt.clear();XEta.clear();XPhi.clear();XLifeTime.clear();Xlxy.clear();
   triggers.clear();

// generator information

  if (!iEvent.isRealData()){

  Handle<HepMCProduct> EvtHandle;
  iEvent.getByLabel("generator",EvtHandle);

  //get HepMC event
  const HepMC::GenEvent* Evt = EvtHandle->GetEvent();


    for(HepMC::GenEvent::particle_const_iterator p = Evt->particles_begin(); p != Evt->particles_end(); ++p){
      if((abs((*p)->pdg_id()) == 6000111 || abs((*p)->pdg_id()) == 6000112 ) && (*p)->status()==3){ // Dstar found
        HepMC::GenVertex *Xvtx = (*p)->end_vertex();

        reco::Candidate::LorentzVector p4( (*p)->momentum() );
        XPt.push_back(p4.pt());
        XPhi.push_back(p4.phi());
        XEta.push_back(p4.eta());

        bool flag = false;

        for(HepMC::GenVertex::particles_out_const_iterator pout = Xvtx->particles_out_const_begin(); pout != Xvtx->particles_out_const_end(); pout++){
	  if ((*pout)->pdg_id()>6) continue;
          reco::Candidate::LorentzVector pout4((*pout)->momentum());
          genJetPt.push_back(pout4.pt());
	  genJetPhi.push_back(pout4.phi());
	  genJetEta.push_back(pout4.eta());
	  if (!flag){
	    reco::Candidate::LorentzVector x4((*pout)->end_vertex()->position());
	    XLifeTime.push_back(x4.P()*p4.mass()/p4.P());
	    Xlxy.push_back(x4.Pt());
	    flag = true;
          }
        }
      }

    }
  }

// L1 HT bits

   edm::Handle<L1GlobalTriggerObjectMapRecord> l1trig_handle;
   iEvent.getByLabel("hltL1GtObjectMap",l1trig_handle);
   const L1GlobalTriggerObjectMapRecord* l1trig = l1trig_handle.product(); 

   l1HTT50 = l1trig->getObjectMap(69)->algoGtlResult();
   l1HTT100 = l1trig->getObjectMap(70)->algoGtlResult();
   l1HTT150 = l1trig->getObjectMap(71)->algoGtlResult();
   l1HTT75 = l1trig->getObjectMap(72)->algoGtlResult();


// HLT trigger table - in open mode all triggers pass

   HLTConfigProvider hltConfig;
   bool changed;
   hltConfig.init(iEvent.getRun(),iSetup,"myHLT",changed);

   edm::Handle<edm::TriggerResults> hltResults;
   iEvent.getByLabel(edm::InputTag("TriggerResults","","myHLT"),hltResults);
   const std::vector< std::string > &trgNames = hltConfig.triggerNames();

   for (size_t i=0;i<hltResults->size();i++)
	if (hltResults->accept(i))
	 triggers.push_back(trgNames.at(i));

// Vertices

   edm::Handle<reco::VertexCollection> vertices;
   iEvent.getByLabel(vertices_,vertices);


   nPixVtx=vertices->size();
   reco::Vertex dummy;
   const reco::Vertex *pv = &dummy;
   int ndof = 0;
   for (reco::VertexCollection::const_iterator vtx = vertices->begin(); vtx != vertices->end(); vtx++){
     if (vtx->ndof() > ndof){
       pv = &*vtx;
       ndof = vtx->ndof();
     }
   }

// jets and their tracks

   edm::ESHandle<TransientTrackBuilder> builder;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", builder);

   edm::Handle<reco::TrackCollection> tracksh;
   iEvent.getByLabel(tracks_,tracksh);

   edm::Handle<reco::CaloJetCollection> jetsh;
   iEvent.getByLabel(jets_,jetsh);

   for (reco::CaloJetCollection::const_iterator j = jetsh->begin(); j != jetsh->end(); j++) {

     if (j->pt() > 40 and fabs(j->eta())<3) ht+=j->et();

     if (j->pt() < 40 or fabs(j->eta()) > 2.) continue;
     jet jet_;
     jet_.energy = j->energy();
     jet_.pt = j->pt();
     jet_.eta = j->eta();
     jet_.phi = j->phi();
     std::vector<track> tracks_;
     GlobalVector direction(j->px(), j->py(), j->pz());
     
     for (reco::TrackCollection::const_iterator trk = tracksh->begin(); trk != tracksh->end(); trk++) {
	
       if (deltaR(j->eta(),j->phi(),trk->eta(),trk->phi())>0.5) continue;
         track track_;

         reco::TransientTrack transientTrack = builder->build(*trk);
         double ip3d = IPTools::signedImpactParameter3D(transientTrack, direction, *pv).second.value(); 
	   
         track_.pt = trk->pt();
         track_.eta = trk->eta();
         track_.phi = trk->phi();
         track_.chi2 = trk->normalizedChi2();
         track_.nHits = trk->numberOfValidHits();
         track_.nPixHits = trk->hitPattern().numberOfValidPixelHits();
         track_.dxy = trk->dxy(pv->position());
         track_.dz = trk->dz(pv->position());
	 track_.ip3d = ip3d;
	 track_.algo = trk->algo();

	 tracks_.push_back(track_);
     }
     jet_.tracks = tracks_;
     jets.push_back(jet_);
   }


// l1jets and their tracks

   edm::Handle<reco::TrackCollection> l1tracksh;
   iEvent.getByLabel(l1tracks_,l1tracksh);

   edm::Handle<reco::CaloJetCollection> l1jetsh;
   iEvent.getByLabel(l1jets_,l1jetsh);

   for (reco::CaloJetCollection::const_iterator j = l1jetsh->begin(); j != l1jetsh->end(); j++) {

     if (j->pt() > 40 and fabs(j->eta())<3) l1ht+=j->et();

     if (j->pt() < 40 or fabs(j->eta()) > 2.) continue;
     jet jet_;
     jet_.energy = j->energy();
     jet_.pt = j->pt();
     jet_.eta = j->eta();
     jet_.phi = j->phi();
     std::vector<track> tracks_;
     GlobalVector direction(j->px(), j->py(), j->pz());
     
     for (reco::TrackCollection::const_iterator trk = l1tracksh->begin(); trk != l1tracksh->end(); trk++) {
	
       if (deltaR(j->eta(),j->phi(),trk->eta(),trk->phi())>0.5) continue;
         track track_;

         reco::TransientTrack transientTrack = builder->build(*trk);
         double ip3d = IPTools::signedImpactParameter3D(transientTrack, direction, *pv).second.value(); 
	   
         track_.pt = trk->pt();
         track_.eta = trk->eta();
         track_.phi = trk->phi();
         track_.chi2 = trk->normalizedChi2();
         track_.nHits = trk->numberOfValidHits();
         track_.nPixHits = trk->hitPattern().numberOfValidPixelHits();
         track_.dxy = trk->dxy(pv->position());
         track_.dz = trk->dz(pv->position());
	 track_.ip3d = ip3d;
	 track_.algo = trk->algo();

	 tracks_.push_back(track_);
     }
     jet_.tracks = tracks_;
     l1jets.push_back(jet_);
   }

// PF jets 4 Trk iteration

   edm::Handle<reco::TrackCollection> pftracksh;
   iEvent.getByLabel(pftracks_,pftracksh);

   edm::Handle<reco::PFJetCollection> pfjetsh;
   iEvent.getByLabel(pfjets_,pfjetsh);

   for (reco::PFJetCollection::const_iterator j = pfjetsh->begin(); j != pfjetsh->end();++j){

     if (j->pt()<40 || fabs(j->eta())>2) continue;

     pfjet pfjet_;

     pfjet_.energy = j->energy();
     pfjet_.pt = j->pt();
     pfjet_.eta = j->eta();
     pfjet_.phi = j->phi();

     pfjet_.chgHadFrac = j->chargedHadronEnergyFraction();
     pfjet_.chgHadN = j->chargedHadronMultiplicity();
     pfjet_.neuHadFrac = j->neutralHadronEnergyFraction();
     pfjet_.neuHadN = j->neutralMultiplicity();
     pfjet_.phFrac = j->photonEnergyFraction();
     pfjet_.phN = j->photonMultiplicity();
     pfjet_.eleFrac = j->electronEnergyFraction();
     pfjet_.eleN = j->electronMultiplicity();
     pfjet_.muFrac = j->muonEnergyFraction();
     pfjet_.muN = j->muonMultiplicity();	

     std::vector<track> tracks_;
     GlobalVector direction(j->px(), j->py(), j->pz());
     
     for (reco::TrackCollection::const_iterator trk = pftracksh->begin(); trk != pftracksh->end(); trk++) {
	
       if (deltaR(j->eta(),j->phi(),trk->eta(),trk->phi())>0.5) continue;
         track track_;

         reco::TransientTrack transientTrack = builder->build(*trk);
         double ip3d = IPTools::signedImpactParameter3D(transientTrack, direction, *pv).second.value(); 
	   
         track_.pt = trk->pt();
         track_.eta = trk->eta();
         track_.phi = trk->phi();
         track_.chi2 = trk->normalizedChi2();
         track_.nHits = trk->numberOfValidHits();
         track_.nPixHits = trk->hitPattern().numberOfValidPixelHits();
         track_.dxy = trk->dxy(pv->position());
         track_.dz = trk->dz(pv->position());
	 track_.ip3d = ip3d;
	 track_.algo = trk->algo();

	 tracks_.push_back(track_);
     }
     pfjet_.tracks = tracks_;
     pfjets.push_back(pfjet_);
   }


   tree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerTuple::beginJob()
{
tree->Branch("jets",&jets);
tree->Branch("l1jets",&l1jets);
tree->Branch("pfjet",&pfjets);

tree->Branch("l1HTT50",&l1HTT50,"l1HTT50/O");
tree->Branch("l1HTT75",&l1HTT75,"l1HTT75/O");
tree->Branch("l1HTT100",&l1HTT100,"l1HTT100/O");
tree->Branch("l1HTT150",&l1HTT150,"l1HTT150/O");

tree->Branch("nPixVtx",&nPixVtx,"nPixVtx/I");

tree->Branch("ht",&ht,"ht/D");
tree->Branch("l1ht",&l1ht,"l1ht/D");

tree->Branch("genJetPt",&genJetPt);
tree->Branch("genJetPhi",&genJetPhi);
tree->Branch("genJetEta",&genJetEta);
tree->Branch("XPt",&XPt);
tree->Branch("XEta",&XEta);
tree->Branch("XPhi",&XPhi);
tree->Branch("XLifeTime",&XLifeTime);
tree->Branch("Xlxy",&Xlxy);

tree->Branch("triggers",&triggers);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerTuple::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
TriggerTuple::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
TriggerTuple::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
TriggerTuple::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
TriggerTuple::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerTuple::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerTuple);
