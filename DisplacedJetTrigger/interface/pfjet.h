#ifndef MyAnalysis_DisplacedJetTrigger_pfjet_h
#define MyAnalysis_DisplacedJetTrigger_pfjet_h

#include <vector>
#include "FWCore/Utilities/interface/typedefs.h"
#include "MyAnalysis/DisplacedJetTrigger/interface/track.h"

struct pfjet {

   double energy,pt,eta,phi;
   double phFrac,neuHadFrac,chgHadFrac,eleFrac,muFrac;
   int phN,neuHadN,chgHadN,eleN,muN;
   std::vector<track> tracks;

};

#endif
