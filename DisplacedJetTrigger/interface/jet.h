#ifndef UsercodeCMS_DisplacedJetTrigger_jet_h
#define UsercodeCMS_DisplacedJetTrigger_jet_h

#include <vector>
#include "FWCore/Utilities/interface/typedefs.h"
#include "UsercodeCMS/DisplacedJetTrigger/interface/track.h"

struct jet {

   double energy,pt,eta,phi;
   std::vector<track> tracks;

};

#endif
