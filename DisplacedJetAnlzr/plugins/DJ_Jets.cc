#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_Jets.h"

DJ_Jets::DJ_Jets(const edm::ParameterSet& iConfig) :
patJetCollectionTag_(iConfig.getParameter<edm::InputTag>("patJetCollectionTag")){

  // single jet
  produces <std::vector<float> > ("jetEnergy");
  produces <std::vector<float> > ("jetPt");
  produces <std::vector<float> > ("jetPtUp");
  produces <std::vector<float> > ("jetPtDown");
  produces <std::vector<float> > ("jetEta");
  produces <std::vector<float> > ("jetPhi");
  produces <std::vector<float> > ("jetMass");
  produces <std::vector<float> > ("jetChgHadFrac");
  produces <std::vector<float> > ("jetNeuHadFrac");
  produces <std::vector<float> > ("jetMuFrac");
  produces <std::vector<float> > ("jetEleFrac");
  produces <std::vector<float> > ("jetPhFrac");
  produces <std::vector<int> > ("jetChgHadN");
  produces <std::vector<int> > ("jetNeuHadN");
  produces <std::vector<int> > ("jetMuN");
  produces <std::vector<int> > ("jetEleN");
  produces <std::vector<int> > ("jetPhN");
  produces <std::vector<int> > ("jetNConstituents");
  produces <std::vector<float> > ("jetPtFracTh1");
  produces <std::vector<float> > ("jetPtReduced");

}

void DJ_Jets::produce(edm::Event& iEvent, const edm::EventSetup& iSetup){

  std::auto_ptr<std::vector<float> > jetEnergy ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetPt ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetPtUp ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetPtDown ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetEta ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetPhi ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetMass ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetChgHadFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetNeuHadFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetMuFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetEleFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetPhFrac ( new std::vector<float> );
  std::auto_ptr<std::vector<int> > jetChgHadN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > jetNeuHadN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > jetMuN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > jetEleN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > jetPhN ( new std::vector<int> );
  std::auto_ptr<std::vector<int> > jetNConstituents ( new std::vector<int> );
  std::auto_ptr<std::vector<float> > jetPtFracTh1 ( new std::vector<float> );
  std::auto_ptr<std::vector<float> > jetPtReduced ( new std::vector<float> );

  edm::Handle<std::vector<pat::Jet> > patJetsHandle;
  iEvent.getByLabel(patJetCollectionTag_,patJetsHandle);

  iSetup.get<JetCorrectionsRecord>().get("AK5PF",JetCorParColl);
  JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
  JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(JetCorPar);

  for (size_t i=0;i<patJetsHandle->size();i++){
    pat::Jet j = patJetsHandle->at(i);
    
    jecUnc->setJetEta(j.eta());
    jecUnc->setJetPt(j.pt()); // here you must use the CORRECTED jet pt
    double unc = jecUnc->getUncertainty(true);

   
    // jet fractions for tracks with energy < 1 GeV
    const std::vector< reco::PFCandidatePtr > constituents=j.getPFConstituents();
    reco::Candidate::LorentzVector myP4Tot,myP4Reduced,myP4Th1;
    for( size_t k=0;k<constituents.size();k++){
      reco::PFCandidatePtr part = constituents.at(k);
      myP4Tot+=part->p4();
      if (part->energy() < 0.8 && part->particleId()<=3 && rand()/float(RAND_MAX) > 0.95) continue;
      myP4Reduced+=part->p4();
      if (part->energy() < 0.8 && part->particleId()<=3) continue;
      myP4Th1+=part->p4();
    }
    std::cout << "fraction %: " << (1.-myP4Th1.pt()/myP4Tot.pt())*100 << std::endl;
    std::cout << "reduction %: " << (1.-myP4Reduced.pt()/myP4Tot.pt())*100 << std::endl;
    jetPtFracTh1->push_back(100*(1-myP4Th1.pt()/myP4Tot.pt())); 
    jetPtReduced->push_back(j.pt()*myP4Th1.pt()/myP4Tot.pt()); 


    jetEnergy->push_back(j.energy());
    jetPt->push_back(j.pt());
    jetPtUp->push_back(j.pt()*(1+unc));
    jetPtDown->push_back(j.pt()*(1-unc));
    jetEta->push_back(j.eta());
    jetPhi->push_back(j.phi());
    jetMass->push_back(j.mass());
    jetNConstituents->push_back(j.nConstituents());

    jetChgHadFrac->push_back(j.chargedHadronEnergyFraction());
    jetChgHadN->push_back(j.chargedHadronMultiplicity());
    jetNeuHadFrac->push_back(j.neutralHadronEnergyFraction());
    jetNeuHadN->push_back(j.neutralHadronMultiplicity());
    jetPhFrac->push_back(j.photonEnergyFraction());
    jetPhN->push_back(j.photonMultiplicity());
    jetEleFrac->push_back(j.electronEnergyFraction());
    jetEleN->push_back(j.electronMultiplicity());
    jetMuFrac->push_back(j.muonEnergyFraction());
    jetMuN->push_back(j.muonMultiplicity());

  }

  iEvent.put(jetPt, "jetPt" );
  iEvent.put(jetPtUp, "jetPtUp" );
  iEvent.put(jetPtDown, "jetPtDown" );
  iEvent.put(jetEta,"jetEta");
  iEvent.put(jetPhi,"jetPhi");
  iEvent.put(jetMass,"jetMass");
  iEvent.put(jetEnergy,"jetEnergy");
  iEvent.put(jetNConstituents,"jetNConstituents");
  iEvent.put(jetChgHadFrac,"jetChgHadFrac");
  iEvent.put(jetNeuHadFrac,"jetNeuHadFrac");
  iEvent.put(jetPhFrac,"jetPhFrac");
  iEvent.put(jetEleFrac,"jetEleFrac");
  iEvent.put(jetMuFrac,"jetMuFrac");
  iEvent.put(jetChgHadN,"jetChgHadN");
  iEvent.put(jetNeuHadN,"jetNeuHadN");
  iEvent.put(jetPhN,"jetPhN");
  iEvent.put(jetEleN,"jetEleN");
  iEvent.put(jetMuN,"jetMuN");
  iEvent.put(jetPtFracTh1,"jetPtFracTh1");
  iEvent.put(jetPtReduced,"jetPtReduced");

}
