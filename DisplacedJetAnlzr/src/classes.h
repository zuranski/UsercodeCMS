#ifndef DJ_CLASSES_H
#define DJ_CLASSES_H

#include "DataFormats/Common/interface/Wrapper.h"
#include <string>
#include <map>

namespace {

  struct dictionary {
    std::map<std::string,bool> dummy0;
    edm::Wrapper<std::map<std::string,bool> > dummy1;

    std::map<std::string,int> dummi0;
    edm::Wrapper<std::map<std::string,int> > dummi1;

    std::map<std::string,std::string> dummee0;
    edm::Wrapper<std::map<std::string,std::string> > dummee1;

  };

}

#endif
