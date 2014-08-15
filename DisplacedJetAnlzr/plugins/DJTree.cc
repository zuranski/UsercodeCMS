#include "UsercodeCMS/DisplacedJetAnlzr/interface/DJTree.h"
#include "UsercodeCMS/DisplacedJetAnlzr/interface/fTypes.h"

#include "FWCore/Framework/interface/ConstProductRegistry.h" 
#include "FWCore/Framework/interface/GroupSelector.h"
#include "FWCore/Framework/interface/GroupSelectorRules.h"
#include "DataFormats/Provenance/interface/Selections.h"

#include "boost/foreach.hpp"

void DJTree::
analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  BOOST_FOREACH( BranchConnector* connector, connectors)
    connector->connect(iEvent);
  tree->Fill();
}

template <class T>
void DJTree::TypedBranchConnector<T>::
connect(const edm::Event& iEvent) {
  edm::Handle<T> handle_;
  iEvent.getByLabel(ml, pin, handle_);
  object_ = *handle_;
}

template <class T> 
DJTree::TypedBranchConnector<T>::
TypedBranchConnector(edm::BranchDescription const* desc, 
		     std::string t, 
		     TTree * tree)
  :  ml( desc->moduleLabel() ),  
     pin( desc->productInstanceName() )
{
  object_ptr_ = &object_;  
  std::string name = (pin=="") ? ml : pin;
  if(t!="")  { tree->Branch( name.c_str(),  object_ptr_, (name+t).c_str() );}  //raw type
  else       { tree->Branch( name.c_str(), &object_ptr_                   );}  //vector<type>
}

void DJTree::
beginJob() {
  tree = fs->make<TTree>("tree", ""); 

  edm::Service<edm::ConstProductRegistry> reg;
  edm::Selections allBranches = reg->allBranchDescriptions();
  edm::GroupSelectorRules groupSelectorRules_(pset, "outputCommands", "DJTree");
  edm::GroupSelector groupSelector_;
  groupSelector_.initialize(groupSelectorRules_, allBranches);

  std::map<std::string,fTypes::LEAFTYPE> dict = fTypes::dict();
  std::set<std::string> branchnames;
  BOOST_FOREACH( const edm::Selections::value_type& selection, allBranches) {
    if(groupSelector_.selected(*selection)) {

      //Check for duplicate branch names
      const std::string name = selection->productInstanceName()==""? selection->moduleLabel() : selection->productInstanceName();
      if (branchnames.find(name) != branchnames.end() )
	throw edm::Exception(edm::errors::Configuration)
	  << "More than one branch named: " << name << std::endl
	  << "Exception thrown from DJTree::beginJob" << std::endl;
      else 
	branchnames.insert( selection->productInstanceName() );
      
      //Create DJTree branch
      switch(dict.find( selection->friendlyClassName() )->second) {
#define EXPAND(enumT,typeT,charT) case fTypes::enumT : connectors.push_back( new TypedBranchConnector<typeT >(selection,charT,tree)); break
	EXPAND(   BOOL,           bool, "/O");
	EXPAND(    INT,            int, "/I");
	EXPAND(  U_INT,       unsigned, "/i");
	EXPAND(  SHORT,          short, "/S");
	EXPAND(U_SHORT, unsigned short, "/s");
	EXPAND(  FLOAT,          float, "/F");
	EXPAND( DOUBLE,         double, "/D");
	EXPAND(   LONG,           long, "/L");
	EXPAND( U_LONG,  unsigned long, "/l");
	EXPAND(   STRING,            std::string, "");

	EXPAND(   BOOL_V, std::vector<          bool>, "");
	EXPAND(    INT_V, std::vector<           int>, "");
	EXPAND(  U_INT_V, std::vector<      unsigned>, "");
	EXPAND(  SHORT_V, std::vector<         short>, "");
	EXPAND(U_SHORT_V, std::vector<unsigned short>, "");
	EXPAND(  FLOAT_V, std::vector<         float>, "");
	EXPAND( DOUBLE_V, std::vector<        double>, "");
	EXPAND(   LONG_V, std::vector<          long>, "");
	EXPAND( U_LONG_V, std::vector< unsigned long>, "");
	EXPAND( STRING_V, std::vector<   std::string>, "");

	EXPAND(  STRING_BOOL_M, fTypes::mapStringBool   , "");
	EXPAND(   STRING_INT_M, fTypes::mapStringInt    , "");
	EXPAND(STRING_STRING_M, fTypes::mapStringString , "");

#undef EXPAND
      default: 
	{
	  std::string leafstring = "";
	  typedef std::pair<std::string, fTypes::LEAFTYPE> pair_t;
	  BOOST_FOREACH( const pair_t& leaf, dict) 
	    leafstring+= "\t" + leaf.first + "\n";

	  throw edm::Exception(edm::errors::Configuration)
	    << "class DJTree does not handle leaves of type " << selection->className() << " like\n"
	    <<   selection->friendlyClassName()   << "_" 
	    <<   selection->moduleLabel()         << "_" 
	    <<   selection->productInstanceName() << "_"  
	    <<   selection->processName()         << std::endl
	    << "Valid leaf types are (friendlyClassName):\n"
	    <<   leafstring
	    << "Exception thrown from DJTree::beginJob\n";
	}
      }
    }
  }
}
