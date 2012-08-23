#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_Event.h"

DJ_Event::DJ_Event(const edm::ParameterSet& iConfig) {
  produces <bool>         ( "isRealData"  );
  produces <unsigned int> ( "run"   );
  produces <unsigned int> ( "event" );
  produces <unsigned int> ( "lumiSection" );
  produces <unsigned int> ( "bunch" );
  produces <unsigned int> ( "orbit" );
  produces <double>       ( "time" );
  produces <unsigned int> ( "nPV" );
  produces <unsigned int> ( "nTrks" );
}

void DJ_Event::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<bool >     isRealData ( new bool(        iEvent.isRealData()      ) );
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
  iEvent.getByLabel("offlinePrimaryVertices", PrimaryVertices );
  std::auto_ptr<unsigned int> nPV ( new unsigned int(PrimaryVertices->size() ) );

  edm::Handle<reco::TrackCollection> generalTracks;
  iEvent.getByLabel("generalTracks",generalTracks);
  std::auto_ptr<unsigned int> nTrks ( new unsigned int(generalTracks->size() ) );

  iEvent.put( isRealData, "isRealData" );
  iEvent.put( run,   "run"   );
  iEvent.put( event, "event" );
  iEvent.put( ls   , "lumiSection" );
  iEvent.put( bunch, "bunch" );
  iEvent.put( orbit, "orbit" );
  iEvent.put( time,  "time"  );
  iEvent.put( nPV,   "nPV"   );
  iEvent.put( nTrks, "nTrks" );
}
