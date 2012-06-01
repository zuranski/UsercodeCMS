#ifndef MyAnalysis_DisplacedJetAnlzr_pfjetpair_h
#define MyAnalysis_DisplacedJetAnlzr_pfjetpair_h

#include <vector>
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"

struct pfjetpair {

   double energy,pt,eta,phi,mass;
   double phFrac,neuHadFrac,chgHadFrac,eleFrac,muFrac,PromptEnergyFrac;
   int phN,neuHadN,chgHadN,eleN,muN,nPrompt;
   double lxy,lxysig,vtxmass,vtxpt,vtxchi2;
   int nDispTracks;
   int idx1,idx2;
   std::vector<track> disptracks;

};

#endif
