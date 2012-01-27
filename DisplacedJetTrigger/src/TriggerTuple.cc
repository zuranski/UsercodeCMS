// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Data formats
#include "HLTrigger/HLTanalyzers/interface/HLTJets.h"
#include "HLTrigger/HLTanalyzers/interface/HLTTrack.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

#include "SimDataFormats/Track/interface/SimTrack.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertex.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"

//L1Trigger
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"

//File Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

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
      int nVtxs,nTracks;
      std::vector<double> jetPt,jetEta,jetPhi;
      std::vector<double> l1jetPt,l1jetEta,l1jetPhi;
      std::vector<double> trkPt,trkEta,trkPhi,trkHits,trkPixHits,trkChi2,trkDxy,trkDz;
      std::vector<double> pfjet4Pt,pfjet4Eta,pfjet4Phi,chgHadFrac4,chgHadN4,neuHadFrac4,neuHadN4;
      std::vector<double> eleFrac4,eleN4,muFrac4,muN4,phFrac4,phN4;
      std::vector<double> pfjet1Pt,pfjet1Eta,pfjet1Phi,chgHadFrac1,chgHadN1,neuHadFrac1,neuHadN1;
      std::vector<double> eleFrac1,eleN1,muFrac1,muN1,phFrac1,phN1;
      std::vector<double> genJetPt,genJetEta,genJetPhi,XPt,XEta,XPhi;
      std::vector<std::string> triggers; 
      edm::InputTag jets_,l1jets_,vertices_,tracks_,pfjets1_,pfjets4_;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

typedef std::pair<const char *, const edm::InputTag *> MissingCollectionInfo;

template <class T>
static inline
bool getCollection(const edm::Event & event, std::vector<MissingCollectionInfo> & missing, edm::Handle<T> & handle, const edm::InputTag & name, const char * description)
{
    event.getByLabel(name, handle);
    bool valid = handle.isValid();
    if (not valid) {
        missing.push_back( std::make_pair(description, & name) );
        handle.clear();
    }
    return valid;
}



//
// constructors and destructor
//
TriggerTuple::TriggerTuple(const edm::ParameterSet& iConfig)

{
   jets_ = iConfig.getParameter<edm::InputTag>("jets");
   l1jets_ = iConfig.getParameter<edm::InputTag>("l1jets");
   vertices_ = iConfig.getParameter<edm::InputTag>("vertices");
   tracks_ = iConfig.getParameter<edm::InputTag>("tracks");
   pfjets1_ = iConfig.getParameter<edm::InputTag>("pfjets1");
   pfjets4_ = iConfig.getParameter<edm::InputTag>("pfjets4");

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

   std::vector<MissingCollectionInfo> missing;

// clear variables
   l1HTT50=0;l1HTT75=0;l1HTT100=0;l1HTT150=0;
   ht = 0; l1ht = 0;nVtxs = 0; nTracks = 0;
   jetPt.clear();jetEta.clear();jetPhi.clear();
   l1jetPt.clear();l1jetEta.clear();l1jetPhi.clear();
   trkPt.clear();trkEta.clear();trkPhi.clear();trkHits.clear();trkPixHits.clear();trkChi2.clear();trkDxy.clear();trkDz.clear();
   pfjet4Pt.clear();pfjet4Eta.clear();pfjet4Phi.clear();chgHadFrac4.clear();chgHadN4.clear();
   neuHadFrac4.clear();neuHadN4.clear();phFrac4.clear();phN4.clear();eleFrac4.clear();eleN4.clear();
   muFrac4.clear();muN4.clear();
   pfjet1Pt.clear();pfjet1Eta.clear();pfjet1Phi.clear();chgHadFrac1.clear();chgHadN1.clear();
   neuHadFrac1.clear();neuHadN1.clear();phFrac1.clear();phN1.clear();eleFrac1.clear();eleN1.clear();
   muFrac1.clear();muN1.clear();
   genJetPt.clear(); genJetEta.clear();genJetPhi.clear();XPt.clear();XEta.clear();XPhi.clear();
   triggers.clear();

// generator information

   if (!iEvent.isRealData()){

     edm::Handle<reco::GenParticleCollection> genParticles;
     iEvent.getByLabel("genParticles",genParticles);

     for(size_t i=0;i<genParticles->size();i++){

      const reco::GenParticle & p = (*genParticles)[i];

      if((fabs(p.pdgId())==6000111 || fabs(p.pdgId()) == 6000112) && p.status()==3){ // X exotics

        XPt.push_back(p.pt());
        XPhi.push_back(p.phi());
        XEta.push_back(p.eta());

        for(size_t j=0;j<p.numberOfDaughters();j++){

          const reco::Candidate* dau = p.daughter(j);
          if (fabs(dau->pdgId()) > 6) continue;
          genJetPt.push_back(dau->pt());
          genJetPhi.push_back(dau->phi());
          genJetEta.push_back(dau->eta());

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

// HT Cut from HT250 path

   try{ 
     edm::Handle<reco::CaloJetCollection> jets;
     iEvent.getByLabel(jets_,jets);

     for (reco::CaloJetCollection::const_iterator jet = jets->begin(); jet != jets->end(); jet++) {
       double mom = jet->et();
       if (mom > 40 and fabs(jet->eta()) < 3.) {
         jetPt.push_back(jet->pt());
         jetEta.push_back(jet->eta());
         jetPhi.push_back(jet->phi());
         ht += mom;
       }
     }
   } catch(...) {;}

// HT Cut from HT250L1FastJet path 
   try{

     edm::Handle<reco::CaloJetCollection> l1jets;
     iEvent.getByLabel(l1jets_,l1jets);
     for (reco::CaloJetCollection::const_iterator jet = l1jets->begin(); jet != l1jets->end(); jet++) {
        double mom = jet->et();
        if(mom > 40 and fabs(jet->eta()) < 3.) {
          l1jetPt.push_back(jet->pt());
          l1jetEta.push_back(jet->eta());
          l1jetPhi.push_back(jet->phi());
          l1ht += mom;
       }
     }
   } catch (...) {;}

// PF jets 1 Trk iteration

   try{
     edm::Handle<reco::PFJetCollection> pfjets1;
     iEvent.getByLabel(pfjets1_,pfjets1);

     for (reco::PFJetCollection::const_iterator pfjet = pfjets1->begin(); pfjet != pfjets1->end();++pfjet){

	if (pfjet->pt()<20 || fabs(pfjet->eta())>2) continue;

	pfjet1Pt.push_back(pfjet->pt());
	pfjet1Eta.push_back(pfjet->eta());
	pfjet1Phi.push_back(pfjet->phi());

	chgHadFrac1.push_back(pfjet->chargedHadronEnergyFraction());
	chgHadN1.push_back(pfjet->chargedHadronMultiplicity());

	neuHadFrac1.push_back(pfjet->neutralHadronEnergyFraction());
	neuHadN1.push_back(pfjet->neutralMultiplicity());
	
	phFrac1.push_back(pfjet->photonEnergyFraction());
	phN1.push_back(pfjet->photonMultiplicity());

	eleFrac1.push_back(pfjet->electronEnergyFraction());
	eleN1.push_back(pfjet->electronMultiplicity());
	
	muFrac1.push_back(pfjet->muonEnergyFraction());
	muN1.push_back(pfjet->muonMultiplicity());	

     }

   } catch (...) {;}

// PF jets 4 Trk iteration

   try{
     edm::Handle<reco::PFJetCollection> pfjets4;
     iEvent.getByLabel(pfjets4_,pfjets4);

     for (reco::PFJetCollection::const_iterator pfjet = pfjets4->begin(); pfjet != pfjets4->end();++pfjet){

	if (pfjet->pt()<20 || fabs(pfjet->eta())>2) continue;

	pfjet4Pt.push_back(pfjet->pt());
	pfjet4Eta.push_back(pfjet->eta());
	pfjet4Phi.push_back(pfjet->phi());

	chgHadFrac4.push_back(pfjet->chargedHadronEnergyFraction());
	chgHadN4.push_back(pfjet->chargedHadronMultiplicity());

	neuHadFrac4.push_back(pfjet->neutralHadronEnergyFraction());
	neuHadN4.push_back(pfjet->neutralMultiplicity());
	
	phFrac4.push_back(pfjet->photonEnergyFraction());
	phN4.push_back(pfjet->photonMultiplicity());

	eleFrac4.push_back(pfjet->electronEnergyFraction());
	eleN4.push_back(pfjet->electronMultiplicity());
	
	muFrac4.push_back(pfjet->muonEnergyFraction());
	muN4.push_back(pfjet->muonMultiplicity());	

     }

   } catch (...) {;}

// Vertices

   try{
     edm::Handle<reco::VertexCollection> vertices;
     iEvent.getByLabel(vertices_,vertices);

     reco::Vertex dummy;
     const reco::Vertex *pv = &dummy;
     int ndof = 0;
     for (reco::VertexCollection::const_iterator vtx = vertices->begin(); vtx != vertices->end(); vtx++){
       if (vtx->ndof() > ndof){
         pv = &*vtx;
         ndof = vtx->ndof();
       }
     }
// Tracks
 
     edm::Handle<reco::TrackCollection> hlttracks;
     iEvent.getByLabel(tracks_,hlttracks);

     for (reco::TrackCollection::const_iterator trk = hlttracks->begin(); trk != hlttracks->end(); trk++) {
       trkPt.push_back(trk->pt());
       trkEta.push_back(trk->eta());
       trkPhi.push_back(trk->phi());
       trkChi2.push_back(trk->normalizedChi2());
       trkHits.push_back(trk->numberOfValidHits());
       trkPixHits.push_back(trk->hitPattern().numberOfValidPixelHits());
       trkDxy.push_back(trk->dxy(pv->position()));
       trkDz.push_back(trk->dz(pv->position()));
     }
   } catch (...) {;}

   tree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerTuple::beginJob()
{

tree->Branch("l1HTT50",&l1HTT50,"l1HTT50/O");
tree->Branch("l1HTT75",&l1HTT75,"l1HTT75/O");
tree->Branch("l1HTT100",&l1HTT100,"l1HTT100/O");
tree->Branch("l1HTT150",&l1HTT150,"l1HTT150/O");

tree->Branch("ht",&ht,"ht/D");
tree->Branch("l1ht",&l1ht,"l1ht/D");

tree->Branch("jetPt",&jetPt);
tree->Branch("jetEta",&jetEta);
tree->Branch("jetPhi",&jetPhi);

tree->Branch("l1jetPt",&l1jetPt);
tree->Branch("l1jetEta",&l1jetEta);
tree->Branch("l1jetPhi",&l1jetPhi);

tree->Branch("trkPt",&trkPt);
tree->Branch("trkEta",&trkEta);
tree->Branch("trkPhi",&trkPhi);
tree->Branch("trkChi2",&trkChi2);
tree->Branch("trkHits",&trkHits);
tree->Branch("trkPixHits",&trkPixHits);
tree->Branch("trkDxy",&trkDxy);
tree->Branch("trkDz",&trkDz);

tree->Branch("pfjet1Pt",&pfjet1Pt);
tree->Branch("pfjet1Eta",&pfjet1Eta);
tree->Branch("pfjet1Phi",&pfjet1Phi);
tree->Branch("chgHadFrac1",&chgHadFrac1);
tree->Branch("neuHadFrac1",&neuHadFrac1);
tree->Branch("phFrac1",&phFrac1);
tree->Branch("eleFrac1",&eleFrac1);
tree->Branch("muFrac1",&muFrac1);
tree->Branch("chgHadN1",&chgHadN1);
tree->Branch("neuHadN1",&neuHadN1);
tree->Branch("phN1",&phN1);
tree->Branch("eleN1",&eleN1);
tree->Branch("muN1",&muN1);

tree->Branch("pfjet4Pt",&pfjet4Pt);
tree->Branch("pfjet4Eta",&pfjet4Eta);
tree->Branch("pfjet4Phi",&pfjet4Phi);
tree->Branch("chgHadFrac4",&chgHadFrac4);
tree->Branch("neuHadFrac4",&neuHadFrac4);
tree->Branch("phFrac4",&phFrac4);
tree->Branch("eleFrac4",&eleFrac4);
tree->Branch("muFrac4",&muFrac4);
tree->Branch("chgHadN4",&chgHadN4);
tree->Branch("neuHadN4",&neuHadN4);
tree->Branch("phN4",&phN4);
tree->Branch("eleN4",&eleN4);
tree->Branch("muN4",&muN4);

tree->Branch("genJetPt",&genJetPt);
tree->Branch("genJetPhi",&genJetPhi);
tree->Branch("genJetEta",&genJetEta);
tree->Branch("XPt",&XPt);
tree->Branch("XEta",&XEta);
tree->Branch("XPhi",&XPhi);

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
