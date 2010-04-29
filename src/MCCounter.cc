// system include files
#include <memory>
                                                                                                                                                             
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
                                                                                                                                                             
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
                                                                                                                                                             
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "TTree.h"

class MCCounter : public edm::EDAnalyzer {
   public:
      explicit MCCounter(const edm::ParameterSet&);
      ~MCCounter();
                                                                                                                                                             
   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      void assignStableDaughters(const reco::Candidate* p, std::vector<int> & pids);

      TTree *tree;
      int NKpiMC,NK3piMC;

};

MCCounter::MCCounter(const edm::ParameterSet& iConfig){

  edm::Service<TFileService> fs;
  tree = fs->make<TTree>("tree","tree");

}

MCCounter::~MCCounter(){}

void MCCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace reco;

  Handle<GenParticleCollection> genParticles;
  iEvent.getByLabel("genParticles",genParticles);
                             
  NKpiMC=0;
  NK3piMC=0;
                                                                                                                                
  for(size_t i=0;i<genParticles->size();i++){
                                                                                                                                                             
    const GenParticle & p = (*genParticles)[i];
                                                                                                                                                             
    if(fabs(p.pdgId())==413){ //D*
                                                                                                                                                             
      for(size_t j=0;j<p.numberOfDaughters();j++){
                                                                                                                                                             
        const Candidate* dau = p.daughter(j);
                                                                                                                                                             
        if(fabs(dau->pdgId())==421){
                                                                                                                                                             
          std::vector<int> d0dauspids;
          assignStableDaughters(dau,d0dauspids);
          int K_num=0,pi_num=0,ndau=d0dauspids.size();
                                                                                                                                                             
          while (!d0dauspids.empty()){
            int pid = d0dauspids.back();
            if(pid==321)
              K_num++;
            if(pid==211)
              pi_num++;
            d0dauspids.pop_back();
          }
                                                                                                                                                             
          if(K_num==1 && pi_num==1 && ndau==2){
            NKpiMC++;
          }
          if(K_num==1 && pi_num==3 && ndau==4){
            NK3piMC++;
          }
        }
      }
    }
  }

  tree->Fill();

}

void MCCounter::assignStableDaughters(const reco::Candidate* p, std::vector<int> & pids){
                                                                                                                                                             
  for(size_t i=0;i<p->numberOfDaughters();i++){
    if(p->daughter(i)->status()==1)
      pids.push_back(abs(p->daughter(i)->pdgId()));
    else
     assignStableDaughters(p->daughter(i),pids);
  }
  return;
}

void MCCounter::beginJob(){

tree->Branch("NKpiMC",&NKpiMC,"NKpiMC/I");
tree->Branch("NK3piMC",&NK3piMC,"NK3piMC/I");

}

void MCCounter::endJob(){

}


DEFINE_FWK_MODULE(MCCounter);
