#ifndef DJ_KSHORTS
#define DJ_KSHORTS

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

//Data Formats and Tools 
#include "DataFormats/Candidate/interface/VertexCompositeCandidate.h"
#include "DataFormats/Candidate/interface/VertexCompositeCandidateFwd.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/V0Candidate/interface/V0Candidate.h"


#include "RecoVertex/KinematicFit/interface/KinematicParticleVertexFitter.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleFitter.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticle.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"

// copied stuff
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "RecoVertex/ConfigurableVertexReco/interface/ConfigurableVertexFitter.h"
#include "PhysicsTools/RecoUtils/interface/CheckHitPattern.h"
#include "SimTracker/TrackAssociation/interface/TrackAssociatorBase.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

#include "UsercodeCMS/DisplacedJetAnlzr/interface/helpers.h"

class DJ_KShorts : public edm::EDProducer {
   public:
      explicit DJ_KShorts(const edm::ParameterSet&);

   private:
      virtual void produce(edm::Event&, const edm::EventSetup&);


      // configurables
      const edm::InputTag patJetCollectionTag_;
      double PromptTrackDxyCut_,TrackPtCut_;

      // global edm objects
      reco::Vertex pv;
      edm::ESHandle<TransientTrackBuilder> theB;

};

#endif
