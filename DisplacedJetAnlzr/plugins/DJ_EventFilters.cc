#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_EventFilters.h"

DJ_EventFilters::DJ_EventFilters(const edm::ParameterSet& iConfig) :
    l1InputTag(iConfig.getParameter<edm::InputTag>("L1InputTag")),
    vtxInputTag(iConfig.getParameter<edm::InputTag>("VertexInputTag")),
    vtxMinNDOF(iConfig.getParameter<unsigned int>("VertexMinimumNDOF")),
    vtxMaxAbsZ(iConfig.getParameter<double>("VertexMaxAbsZ")),
    vtxMaxd0(iConfig.getParameter<double>("VertexMaxd0")),
    trkInputTag(iConfig.getParameter<edm::InputTag>("TracksInputTag")),
    numTracks(iConfig.getParameter<unsigned int>("NumTracks")),
    hpTrackThreshold(iConfig.getParameter<double>("HPTrackThreshold")),
    hcalNoiseInputTag(iConfig.getParameter<edm::InputTag>("HcalNoiseInputTag")),
    beamHaloInputTag(iConfig.getParameter<edm::InputTag>("BeamHaloInputTag"))
{
  produces <bool> ("physicsDeclaredFilterFlag");
  produces <bool> ("bptx0FilterFlag");
  produces <bool> ("bscMinBiasFilterFlag");
  produces <bool> ("primaryVertexFilterFlag");
  produces <bool> ("beamScrapingFilterFlag");
  produces <bool> ("hbheNoiseFilterFlag");
  produces <bool> ("beamHaloLooseFilterFlag");
  produces <bool> ("beamHaloTightFilterFlag");
  //
}

void DJ_EventFilters::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::auto_ptr<bool> physicsdeclared( new bool() );
  std::auto_ptr<bool> bptx0( new bool() );
  std::auto_ptr<bool> bscminbias( new bool() );
  std::auto_ptr<bool> primaryvertex( new bool() );
  std::auto_ptr<bool> beamscraping( new bool() );
  std::auto_ptr<bool> hbhenoise( new bool() );
  std::auto_ptr<bool> beamhaloloose( new bool() );
  std::auto_ptr<bool> beamhalotight( new bool() );

  *physicsdeclared.get() = false;
  *bptx0.get() = false;
  *bscminbias.get() = false;
  *primaryvertex.get() = false;
  *beamscraping.get() = false;
  *hbhenoise.get() = false;
  *beamhaloloose.get() = false;
  *beamhalotight.get() = false;

  //-----------------------------------------------------------------
  edm::Handle<L1GlobalTriggerReadoutRecord> l1GtReadoutRecord;
  iEvent.getByLabel(l1InputTag, l1GtReadoutRecord);

  // Technical Trigger Part
  if(l1GtReadoutRecord.isValid()) {
    edm::LogInfo("DJ_EventFilters") << "Successfully obtained " << l1InputTag;

    L1GtFdlWord fdlWord = l1GtReadoutRecord->gtFdlWord();
    if (fdlWord.physicsDeclared() == 1)
      *physicsdeclared.get() = true;

    // BPTX0
    if ( l1GtReadoutRecord->technicalTriggerWord()[0] )
      *bptx0.get() = true;

    // MinBias
    if ( l1GtReadoutRecord->technicalTriggerWord()[40] || l1GtReadoutRecord->technicalTriggerWord()[41] )
      *bscminbias.get() = true;

  } else {
    edm::LogError("DJ_EventFilters") << "Error! Can't get the product " << l1InputTag;
  }

  // Good Primary Vertex Part
  edm::Handle<reco::VertexCollection> primaryVertices;
  iEvent.getByLabel(vtxInputTag,primaryVertices);

  if(primaryVertices.isValid()) {
    edm::LogInfo("DJ_EventFilters") << "Total # Primary Vertices: " << primaryVertices->size();

    for( reco::VertexCollection::const_iterator it=primaryVertices->begin() ; it!=primaryVertices->end() ; ++it ) {
      if( !(it->isFake()) && it->ndof() > vtxMinNDOF &&
          fabs(it->z()) <= vtxMaxAbsZ && fabs(it->position().rho()) <= vtxMaxd0
        ) *primaryvertex.get() = true;
    }
  } else {
    edm::LogError("DJ_EventFilters") << "Error! Can't get the product " << vtxInputTag;
  }

  // Scraping Events Part
  edm::Handle<reco::TrackCollection> tracks;
  iEvent.getByLabel(trkInputTag,tracks);

  if(tracks.isValid()) {
    edm::LogInfo("DJ_EventFilters") << "Total # Tracks: " << tracks->size();

    int numhighpurity = 0;
    double fraction = 0.;
    reco::TrackBase::TrackQuality trackQuality = reco::TrackBase::qualityByName("highPurity");

    if( tracks->size() > numTracks ){
      for( reco::TrackCollection::const_iterator it=tracks->begin(); it!=tracks->end(); ++it ) {
        if( it->quality(trackQuality) ) numhighpurity++;
      }
      fraction = (double)numhighpurity/(double)tracks->size();
      if( fraction > hpTrackThreshold ) *beamscraping.get() = true;
    }
  } else {
    edm::LogError("DJ_EventFilters") << "Error! Can't get the product " << trkInputTag;
  }

  // Hcal Noise Part
  edm::Handle<bool> hbheFilterResult;
  iEvent.getByLabel(hcalNoiseInputTag, hbheFilterResult);

  if(hbheFilterResult.isValid()) {
    edm::LogInfo("DJ_EventFilters") << "Successfully obtained " << hcalNoiseInputTag;

      *hbhenoise.get()=*hbheFilterResult;
  } else {
    edm::LogError("DJ_EventFilters") << "Error! Can't get the product " << hcalNoiseInputTag;
  }

  // Beam Halo part
  edm::Handle<reco::BeamHaloSummary> TheBeamHaloSummary;
  iEvent.getByLabel(beamHaloInputTag,TheBeamHaloSummary); 

  if(TheBeamHaloSummary.isValid()) {
    edm::LogInfo("DJ_EventFilters") << "Successfully obtained " << beamHaloInputTag;
    const reco::BeamHaloSummary TheSummary = (*TheBeamHaloSummary.product() );
    *beamhaloloose.get() = !TheSummary.CSCLooseHaloId();
    *beamhalotight.get() = !TheSummary.CSCTightHaloId();    
  } else {
    edm::LogError("DJ_EventFilters") << "Error! Can't get the product " << beamHaloInputTag;
  }

  //-----------------------------------------------------------------
  iEvent.put(physicsdeclared,"physicsDeclaredFilterFlag");
  iEvent.put(bptx0,"bptx0FilterFlag");
  iEvent.put(bscminbias,"bscMinBiasFilterFlag");
  iEvent.put(primaryvertex,"primaryVertexFilterFlag");
  iEvent.put(beamscraping,"beamScrapingFilterFlag");
  iEvent.put(hbhenoise,"hbheNoiseFilterFlag");
  iEvent.put(beamhaloloose,"beamHaloLooseFilterFlag");
  iEvent.put(beamhalotight,"beamHaloTightFilterFlag");
}



