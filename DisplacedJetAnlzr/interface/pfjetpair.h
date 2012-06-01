#ifndef MyAnalysis_DisplacedJetAnlzr_pfjetpair_h
#define MyAnalysis_DisplacedJetAnlzr_pfjetpair_h

#include <vector>
#include "MyAnalysis/DisplacedJetAnlzr/interface/track.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjet.h"

struct pfjetpair : pfjet{

   int idx1,idx2;

};

#endif
