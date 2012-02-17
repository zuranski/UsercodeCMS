#ifndef MyAnalysis_DisplacedJetAnlzr_pfjet_h
#define MyAnalysis_DisplacedJetAnlzr_pfjet_h

#include <vector>
#include "FWCore/Utilities/interface/typedefs.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"

struct pfjet {

   double energy,pt,eta,phi;
   double phFrac,neuHadFrac,chgHadFrac,eleFrac,muFrac;
   int phN,neuHadN,chgHadN,eleN,muN;
   std::vector<track> tracks;

};

#endif
