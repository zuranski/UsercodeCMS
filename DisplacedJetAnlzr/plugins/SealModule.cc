#include "FWCore/Framework/interface/MakerMacros.h"

#include "MyAnalysis/DisplacedJetAnlzr/interface/DJTree.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_Triggers.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_TriggerObjects.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_PileupSummary.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_Event.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_GenEvent.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_EventFilters.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_HcalNoiseSummaryExists.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/DJ_DisplacedJets.h"

DEFINE_FWK_MODULE(DJTree);
DEFINE_FWK_MODULE(DJ_Triggers);
DEFINE_FWK_MODULE(DJ_TriggerObjects);
DEFINE_FWK_MODULE(DJ_PileupSummary);
DEFINE_FWK_MODULE(DJ_Event);
DEFINE_FWK_MODULE(DJ_GenEvent);
DEFINE_FWK_MODULE(DJ_EventFilters);
DEFINE_FWK_MODULE(DJ_HcalNoiseSummaryExists);
DEFINE_FWK_MODULE(DJ_DisplacedJets);
