#ifndef MyAnalysis_DisplacedJetAnlzr_pfjet_h
#define MyAnalysis_DisplacedJetAnlzr_pfjet_h

#include <vector>
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"

struct pfjet {

   double energy,pt,eta,phi,mass;
   double truelxy;
   double phFrac,neuHadFrac,chgHadFrac,eleFrac,muFrac,PromptEnergyFrac;
   int phN,neuHadN,chgHadN,eleN,muN;
   int nDispTracks,nPrompt;
   double lxy,lxysig,vtxmass,vtxpt,vtxX,vtxY,vtxZ,vtxchi2,vtxCharge,vtxdR,vtxN;
   std::vector<track> disptracks;

};

#endif
