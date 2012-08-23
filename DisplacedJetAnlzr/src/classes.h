#ifndef DJ_CLASSES_H
#define DJ_CLASSES_H

#include "MyAnalysis/DisplacedJetAnlzr/interface/genjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjetpair.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/exotic.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/djcandidate.h"
#include "DataFormats/Common/interface/Wrapper.h"
#include <string>
#include <map>
#include "Math/LorentzVector.h"
#include "Math/PtEtaPhiE4D.h"
#include "Math/PtEtaPhiM4D.h"

namespace {

  struct dictionary {
    edm::Wrapper<exotic> exo;
    edm::Wrapper<std::vector<exotic> > exos;
    edm::Wrapper<genjet> genj;
    edm::Wrapper<std::vector<genjet> > genjs;
    edm::Wrapper<track> trk;
    edm::Wrapper<std::vector<track> > trks;
    edm::Wrapper<pfjet> pfj;
    edm::Wrapper<std::vector<pfjet> > pfjets;
    edm::Wrapper<pfjetpair> pfjpair;
    edm::Wrapper<std::vector<pfjetpair> > pfjetpairs;
    edm::Wrapper<djcandidate> djc;
    edm::Wrapper<std::vector<djcandidate> > djcs;

    std::map<std::string,bool> dummy0;
    edm::Wrapper<std::map<std::string,bool> > dummy1;

    std::map<std::string,int> dummi0;
    edm::Wrapper<std::map<std::string,int> > dummi1;

    std::map<std::string,std::string> dummee0;
    edm::Wrapper<std::map<std::string,std::string> > dummee1;

    ROOT::Math::PtEtaPhiM4D<float> dumdum;
  };

}

#endif
