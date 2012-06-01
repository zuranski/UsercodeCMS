#include "MyAnalysis/DisplacedJetAnlzr/interface/genjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/pfjetpair.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/exotic.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/trgObj.h"
#include "DataFormats/Common/interface/Wrapper.h"

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
    edm::Wrapper<trgObj> t0;
    edm::Wrapper<std::vector<trgObj> > t0s;
  };

}
