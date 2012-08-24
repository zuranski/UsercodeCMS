#ifndef DJ_DISPLACEDJETS
#define DJ_DISPLACEDJETS

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"

//My Data Formats
#include "MyAnalysis/DisplacedJetAnlzr/interface/djcandidate.h"

//Data Formats and Tools 
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "RecoVertex/ConfigurableVertexReco/interface/ConfigurableVertexFitter.h"
#include "PhysicsTools/RecoUtils/interface/CheckHitPattern.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorBase.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"


class DJ_DisplacedJets : public edm::EDProducer {
   public:
      explicit DJ_DisplacedJets(const edm::ParameterSet&);

   private:
      virtual void produce(edm::Event&, const edm::EventSetup&);

      void GetMothers(const HepMC::GenParticle *p, std::vector<std::pair<int,double> > &moms);
      void ClearEventData();
      void GetEventInfo(const edm::Event&, const edm::EventSetup&);
      void LoopPFJets(const edm::Event&, const edm::EventSetup&, std::vector<djcandidate> &, std::vector<djcandidate> &);
      void DoVertexing(const edm::EventSetup&, djcandidate &djc, std::vector<reco::TransientTrack> disptrks);


      // configurables
      const edm::InputTag patJetCollectionTag_;
      bool useTrackingParticles_;
      double PromptTrackDxyCut_,TrackPtCut_;
      const edm::ParameterSet vtxconfig_;
      ConfigurableVertexFitter vtxfitter_;

      // stuff to use over the different functions
      reco::RecoToSimCollection RecoToSimColl;

      // global edm objects
      reco::Vertex pv;
      edm::ESHandle<TransientTrackBuilder> theB;
      CheckHitPattern checkHitPattern_;

};

#endif
