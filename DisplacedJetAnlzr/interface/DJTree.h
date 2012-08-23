#ifndef DJ_Tree_h
#define DJ_Tree_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include <string>
#include <vector>
#include <TTree.h>

class DJTree : public edm::EDAnalyzer {
private:    
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob(){}

  class BranchConnector {
  public:
    virtual ~BranchConnector() {};
    virtual void connect(const edm::Event&) = 0;
  };
  
  template <class T>
  class TypedBranchConnector : public BranchConnector {
  private:
    std::string ml;   //module label
    std::string pin;  //product instance name
    T object_;
    T* object_ptr_;
  public:
    TypedBranchConnector(edm::BranchDescription const*, std::string, TTree*);
    void connect(const edm::Event&);
  };

  edm::Service<TFileService> fs;
  TTree * tree;
  std::vector<BranchConnector*> connectors;
  edm::ParameterSet pset;

public:
  explicit DJTree(const edm::ParameterSet& iConfig) : pset(iConfig) {}
};

#endif
