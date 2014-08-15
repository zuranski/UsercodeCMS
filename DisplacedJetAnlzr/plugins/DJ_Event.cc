#include "UsercodeCMS/DisplacedJetAnlzr/interface/DJ_Event.h"

DJ_Event::DJ_Event(const edm::ParameterSet& iConfig):
patJetCollectionTag_(iConfig.getParameter<edm::InputTag>("patJetCollectionTag")) {
  produces <bool>         ( "realData"  );
  produces <unsigned int> ( "run"   );
  produces <unsigned int> ( "event" );
  produces <unsigned int> ( "lumiSection" );
  produces <unsigned int> ( "bunch" );
  produces <unsigned int> ( "orbit" );
  produces <double>       ( "time" );
  produces <unsigned int> ( "nPV" );
  produces <unsigned int> ( "nTrks" );
  produces <float> ( "pfHT" );
  produces <float> ( "caloHT" );
  produces <float> ( "caloHTup" );
  produces <float> ( "caloHTdown" );
}

void DJ_Event::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<bool >     realData ( new bool(        iEvent.isRealData()      ) );
  std::auto_ptr<unsigned int >  run   ( new unsigned int(iEvent.id().run()        ) );
  std::auto_ptr<unsigned int >  event ( new unsigned int(iEvent.id().event()      ) );
  std::auto_ptr<unsigned int >  ls    ( new unsigned int(iEvent.luminosityBlock() ) );
  std::auto_ptr<unsigned int >  bunch ( new unsigned int(iEvent.bunchCrossing()   ) );
  std::auto_ptr<unsigned int >  orbit ( new unsigned int(iEvent.orbitNumber()     ) );
  
  double sec  = iEvent.time().value() >> 32 ;
  double usec = 0xFFFFFFFF & iEvent.time().value();
  double conv = 1e6;

  std::auto_ptr<double >        time  	      ( new double(sec+usec/conv));

  edm::Handle<reco::VertexCollection> PrimaryVertices;
  iEvent.getByLabel("goodVertices", PrimaryVertices );
  std::auto_ptr<unsigned int> nPV ( new unsigned int(PrimaryVertices->size() ) );

  edm::Handle<reco::TrackCollection> generalTracks;
  iEvent.getByLabel("generalTracks",generalTracks);
  std::auto_ptr<unsigned int> nTrks ( new unsigned int(generalTracks->size() ) );

  edm::Handle<std::vector<pat::Jet> > patJetsHandle;
  iEvent.getByLabel(patJetCollectionTag_,patJetsHandle);

  float ht=0;
  for (size_t i=0;i<patJetsHandle->size();i++){
    pat::Jet j = patJetsHandle->at(i);
    ht+=j.et();
  }
  std::auto_ptr<float> pfHT ( new float(ht) );
  
  edm::Handle<std::vector<pat::Jet> > caloJetsHandle;
  iEvent.getByLabel("patJetsAK5Calo",caloJetsHandle);

  iSetup.get<JetCorrectionsRecord>().get("AK5Calo",JetCorParColl); 
  JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
  JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(JetCorPar);

  //JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty("UsercodeCMS/DisplacedJetAnlzr/data/Fall12_V7_MC_Uncertainty_AK5Calo.txt");

  float cht=0;
  float cht_up=0;
  float cht_down=0;
  for (size_t i=0;i<caloJetsHandle->size();i++){
    pat::Jet j = caloJetsHandle->at(i);
    jecUnc->setJetEta(j.eta());
    jecUnc->setJetPt(j.pt()); // here you must use the CORRECTED jet pt
    double unc = jecUnc->getUncertainty(true);
    if (fabs(j.eta())<3 && j.pt()>40) {
      cht+=j.et();
      cht_up+=j.et()*(1+unc);
      cht_down+=j.et()*(1-unc);
    }
  }
  std::auto_ptr<float> caloHT ( new float(cht) );
  std::auto_ptr<float> caloHTup ( new float(cht_up) );
  std::auto_ptr<float> caloHTdown ( new float(cht_down) );

  iEvent.put( realData, "realData" );
  iEvent.put( run,   "run"   );
  iEvent.put( event, "event" );
  iEvent.put( ls   , "lumiSection" );
  iEvent.put( bunch, "bunch" );
  iEvent.put( orbit, "orbit" );
  iEvent.put( time,  "time"  );
  iEvent.put( nPV,   "nPV"   );
  iEvent.put( nTrks, "nTrks" );
  iEvent.put( pfHT, "pfHT"   );
  iEvent.put( caloHT, "caloHT"   );
  iEvent.put( caloHTup, "caloHTup"   );
  iEvent.put( caloHTdown, "caloHTdown"   );
}
