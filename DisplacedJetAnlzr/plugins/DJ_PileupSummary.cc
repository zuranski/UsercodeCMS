#include "UsercodeCMS/DisplacedJetAnlzr/interface/DJ_PileupSummary.h"

DJ_PileupSummary::DJ_PileupSummary(const edm::ParameterSet& iConfig) :
  inputTag(iConfig.getParameter<edm::InputTag>("InputTag")),
  pdfCTEQWeightsInputTag(iConfig.getParameter<edm::InputTag>("PDFCTEQWeightsInputTag")),
  pdfMSTWWeightsInputTag(iConfig.getParameter<edm::InputTag>("PDFMSTWWeightsInputTag")),
  pdfNNPDFWeightsInputTag(iConfig.getParameter<edm::InputTag>("PDFNNPDFWeightsInputTag")),
  Prefix(iConfig.getParameter<std::string>("Prefix")),
  Suffix(iConfig.getParameter<std::string>("Suffix"))
{
  
  produces <bool>  ( Prefix + "HandleValid" + Suffix);
  produces <std::vector<double> > ( "PDFCTEQWeights" );
  produces <std::vector<double> > ( "PDFMSTWWeights" );
  produces <std::vector<double> > ( "PDFNNPDFWeights" );
  produces <double> ("pdfCTEQw");
  produces <double> ("pdfMSTWw");
  produces <double> ("pdfNNPDFw");
  produces <float>(Prefix + "TrueNumInteractionsBX0" + Suffix);
  produces <unsigned>(Prefix + "PUInteractionsBX0" + Suffix);
  produces <std::vector<float> >(Prefix + "TrueNumInteractions" + Suffix);
  produces <std::vector<unsigned> >(Prefix + "PUInteractions" + Suffix);
  produces <std::vector<int> >(Prefix + "BX" + Suffix);
}

void DJ_PileupSummary::
produce(edm::Event& event, const edm::EventSetup& ) {
  std::auto_ptr<std::vector<double> >  pdfCTEQWeights  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pdfMSTWWeights  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pdfNNPDFWeights  ( new std::vector<double>()  );
  std::auto_ptr<double> pdfCTEQw (new double());
  std::auto_ptr<double> pdfMSTWw (new double()); 
  std::auto_ptr<double> pdfNNPDFw (new double());
  std::auto_ptr<float> nTrueBX0  (new float());
  std::auto_ptr<unsigned> interactionsBX0  (new unsigned());
  std::auto_ptr<std::vector<float> > nTrue ( new std::vector<float>() );
  std::auto_ptr<std::vector<unsigned> > interactions ( new std::vector<unsigned>() );
  std::auto_ptr<std::vector<int> >      bx           ( new std::vector<int>() );

  edm::Handle<std::vector<double> > pdfCTEQWeightsHandle;
  edm::Handle<std::vector<double> > pdfMSTWWeightsHandle;
  edm::Handle<std::vector<double> > pdfNNPDFWeightsHandle;

  event.getByLabel(pdfCTEQWeightsInputTag, pdfCTEQWeightsHandle);
  event.getByLabel(pdfMSTWWeightsInputTag, pdfMSTWWeightsHandle);
  event.getByLabel(pdfNNPDFWeightsInputTag, pdfNNPDFWeightsHandle);

  if( pdfCTEQWeightsHandle.isValid() ) {
    *pdfCTEQWeights.get() = *pdfCTEQWeightsHandle;
    *pdfCTEQw.get() = pdfCTEQWeights->at(0);
  }

  if( pdfMSTWWeightsHandle.isValid() ) {
    *pdfMSTWWeights.get() = *pdfMSTWWeightsHandle;
    *pdfMSTWw.get() = pdfMSTWWeights->at(0);
  }

  if( pdfNNPDFWeightsHandle.isValid() ) {
    *pdfNNPDFWeights.get() = *pdfNNPDFWeightsHandle;
    *pdfNNPDFw.get() = pdfNNPDFWeights->at(0);
  }

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
  event.put( pdfCTEQWeights, "PDFCTEQWeights" );
  event.put( pdfMSTWWeights, "PDFMSTWWeights" );
  event.put( pdfNNPDFWeights, "PDFNNPDFWeights" ); 
  event.put( pdfCTEQw, "pdfCTEQw" );
  event.put( pdfMSTWw, "pdfMSTWw" );
  event.put( pdfNNPDFw, "pdfNNPDFw" ); 

}
