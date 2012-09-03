#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_DiJets.h"

DJ_DiJets::DJ_DiJets(const edm::ParameterSet& iConfig) :
patJetCollectionTag_(iConfig.getParameter<edm::InputTag>("patJetCollectionTag")){

  produces <std::vector<float> > ("dijetEnergy");
  produces <std::vector<float> > ("dijetPt");
  produces <std::vector<float> > ("dijetEta");
  produces <std::vector<float> > ("dijetPhi");
  produces <std::vector<float> > ("dijetMass");
  produces <std::vector<float> > ("dijetChgHadFrac");
  produces <std::vector<float> > ("dijetNeuHadFrac");
  produces <std::vector<float> > ("dijetMuFrac");
  produces <std::vector<float> > ("dijetEleFrac");
  produces <std::vector<float> > ("dijetPhFrac");
  produces <std::vector<int> > ("dijetChgHadN");
  produces <std::vector<int> > ("dijetNeuHadN");
  produces <std::vector<int> > ("dijetMuN");
  produces <std::vector<int> > ("dijetEleN");
  produces <std::vector<int> > ("dijetPhN");
  produces <std::vector<int> > ("dijetNConstituents");
  produces <std::vector<int> > ("dijetIdx1");
  produces <std::vector<int> > ("dijetIdx2");

}

void DJ_DiJets::produce(edm::Event& iEvent, const edm::EventSetup& iSetup){

  std::auto_ptr<std::vector<float> > dijetEnergy ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetMass ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetChgHadFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetNeuHadFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetMuFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetEleFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > dijetPhFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<int> > dijetChgHadN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > dijetNeuHadN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > dijetMuN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > dijetEleN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > dijetPhN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > dijetNConstituents ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > dijetIdx1 ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > dijetIdx2 ( new std::vector<int> );

  edm::Handle<std::vector<pat::Jet> > patJetsHandle;
  iEvent.getByLabel(patJetCollectionTag_,patJetsHandle);

  for (int i=0;i<int(patJetsHandle->size()-1);i++){
    for (size_t j=i+1;j<patJetsHandle->size();j++){


      pat::Jet j1 = patJetsHandle->at(i);
      pat::Jet j2 = patJetsHandle->at(j);

      dijetIdx1->push_back(i);
      dijetIdx2->push_back(j);

      reco::Candidate::LorentzVector p4 = j1.p4() + j2.p4();

      dijetEnergy->push_back(j1.energy()+j2.energy());
      dijetPt->push_back(p4.pt());
      dijetEta->push_back(p4.eta());
      dijetPhi->push_back(p4.phi());
      dijetMass->push_back(p4.mass());
      dijetNConstituents->push_back(j1.nConstituents() + j2.nConstituents());

      dijetChgHadFrac->push_back((j1.chargedHadronEnergyFraction()*j1.energy() + 
				 j2.chargedHadronEnergyFraction()*j2.energy())/
                                 (j1.energy()+j2.energy())) ;
      dijetChgHadN->push_back(j1.chargedHadronMultiplicity()+j2.chargedHadronMultiplicity());
      dijetNeuHadFrac->push_back((j1.neutralHadronEnergyFraction()*j1.energy() + 
				 j2.neutralHadronEnergyFraction()*j2.energy())/
                                 (j1.energy()+j2.energy())) ;
      dijetNeuHadN->push_back(j1.neutralHadronMultiplicity()+j2.neutralHadronMultiplicity());
      dijetPhFrac->push_back((j1.photonEnergyFraction()*j1.energy() + 
				 j2.photonEnergyFraction()*j2.energy())/
                                 (j1.energy()+j2.energy())) ;
      dijetPhN->push_back(j1.photonMultiplicity()+j2.photonMultiplicity());
      dijetEleFrac->push_back((j1.electronEnergyFraction()*j1.energy() + 
				 j2.electronEnergyFraction()*j2.energy())/
                                 (j1.energy()+j2.energy())) ;
      dijetEleN->push_back(j1.electronMultiplicity()+j2.electronMultiplicity());
      dijetMuFrac->push_back((j1.muonEnergyFraction()*j1.energy() + 
				 j2.muonEnergyFraction()*j2.energy())/
                                 (j1.energy()+j2.energy())) ;
      dijetMuN->push_back(j1.muonMultiplicity()+j2.muonMultiplicity());

    }   
  }

  iEvent.put(dijetPt,"dijetPt");
  iEvent.put(dijetEta,"dijetEta");
  iEvent.put(dijetPhi,"dijetPhi");
  iEvent.put(dijetMass,"dijetMass");
  iEvent.put(dijetEnergy,"dijetEnergy");
  iEvent.put(dijetNConstituents,"dijetNConstituents");
  iEvent.put(dijetChgHadFrac,"dijetChgHadFrac");
  iEvent.put(dijetNeuHadFrac,"dijetNeuHadFrac");
  iEvent.put(dijetPhFrac,"dijetPhFrac");
  iEvent.put(dijetEleFrac,"dijetEleFrac");
  iEvent.put(dijetMuFrac,"dijetMuFrac");
  iEvent.put(dijetChgHadN,"dijetChgHadN");
  iEvent.put(dijetNeuHadN,"dijetNeuHadN");
  iEvent.put(dijetPhN,"dijetPhN");
  iEvent.put(dijetEleN,"dijetEleN");
  iEvent.put(dijetMuN,"dijetMuN");
  iEvent.put(dijetIdx1,"dijetIdx1");
  iEvent.put(dijetIdx2,"dijetIdx2");

}
