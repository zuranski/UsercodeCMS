#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_PileupSummary.h"

DJ_PileupSummary::DJ_PileupSummary(const edm::ParameterSet& iConfig) :
  inputTag(iConfig.getParameter<edm::InputTag>("InputTag")),
  Prefix(iConfig.getParameter<std::string>("Prefix")),
  Suffix(iConfig.getParameter<std::string>("Suffix"))
{
  
  produces <bool>  ( Prefix + "HandleValid" + Suffix);
  produces <float>(Prefix + "TrueNumInteractionsBX0" + Suffix);
  produces <unsigned>(Prefix + "PUInteractionsBX0" + Suffix);
  produces <std::vector<float> >(Prefix + "TrueNumInteractions" + Suffix);
  produces <std::vector<unsigned> >(Prefix + "PUInteractions" + Suffix);
  produces <std::vector<int> >(Prefix + "BX" + Suffix);
}

void DJ_PileupSummary::
produce(edm::Event& event, const edm::EventSetup& ) {
  std::auto_ptr<float> nTrueBX0  (new float());
  std::auto_ptr<unsigned> interactionsBX0  (new unsigned());
  std::auto_ptr<std::vector<float> > nTrue ( new std::vector<float>() );
  std::auto_ptr<std::vector<unsigned> > interactions ( new std::vector<unsigned>() );
  std::auto_ptr<std::vector<int> >      bx           ( new std::vector<int>() );

  typedef std::vector<PileupSummaryInfo> PIV;
  edm::Handle<PIV> pileup;
  event.getByLabel(inputTag,pileup);

  if (pileup.isValid()) {
    for(PIV::const_iterator pu = pileup->begin(); pu != pileup->end(); ++pu) {
      nTrue->push_back(pu->getTrueNumInteractions());
      interactions->push_back(pu->getPU_NumInteractions());
      bx->push_back(pu->getBunchCrossing());
      if (!pu->getBunchCrossing()) {
	*interactionsBX0.get() = pu->getPU_NumInteractions();
	*nTrueBX0.get() = pu->getTrueNumInteractions();
      }
    }
  }

  event.put( std::auto_ptr<bool>( new bool(pileup.isValid())), Prefix + "HandleValid" + Suffix );
  event.put( nTrueBX0, Prefix + "TrueNumInteractionsBX0" + Suffix );
  event.put( nTrue,    Prefix + "TrueNumInteractions"    + Suffix );
  event.put( interactionsBX0, Prefix + "PUInteractionsBX0" + Suffix );
  event.put( interactions,    Prefix + "PUInteractions"    + Suffix );
  event.put( bx,              Prefix + "BX"              + Suffix );
  
}
