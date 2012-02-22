#ifndef MyAnalysis_DisplacedJetAnlzr_pfjet_h
#define MyAnalysis_DisplacedJetAnlzr_pfjet_h

#include <vector>
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"

struct pfjet {

   double energy,pt,eta,phi;
   double phFrac,neuHadFrac,chgHadFrac,eleFrac,muFrac,PromptEnergyFrac;
   int phN,neuHadN,chgHadN,eleN,muN,nPrompt;
   double lxy,lxysig,vtxmass,vtxpt,vtxchi2;
   int nDispTracks;
   std::vector<track> disptracks;

};

#endif
