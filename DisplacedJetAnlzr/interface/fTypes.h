#ifndef DJ_FTYPES
#define DJ_FTYPES

#include <map>
#include <string>
#include "Math/LorentzVector.h"
#include "Math/PtEtaPhiE4D.h"
#include "Math/PtEtaPhiM4D.h"
#include "Math/Vector3D.h"
#include "Math/Point3D.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/genjet.h"
#include "MyAnalysis/DisplacedJetAnlzr/interface/djcandidate.h"

struct fTypes {

  typedef ROOT::Math::PositionVector3D<ROOT::Math::Cartesian3D<float> >       fPoint;
  typedef ROOT::Math::PositionVector3D<ROOT::Math::Cartesian3D<double> >      dPoint;
  typedef ROOT::Math::DisplacementVector3D<ROOT::Math::Cartesian3D<float> >  fVector;
  typedef ROOT::Math::DisplacementVector3D<ROOT::Math::Cartesian3D<double> > dVector;
  typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float> >  fPolarLorentzV;
  typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiE4D<double> > dPolarLorentzV;
  typedef ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> >     dXYZLorentzV;

  typedef std::map<std::string,       bool> mapStringBool;
  typedef std::map<std::string,        int> mapStringInt;
  typedef std::map<std::string,std::string> mapStringString;

  enum LEAFTYPE {BOOL=1,  BOOL_V,          
		 SHORT,   SHORT_V,           
		 U_SHORT, U_SHORT_V,       
		 INT,     INT_V,             
		 U_INT,   U_INT_V,
		 FLOAT,   FLOAT_V,           
		 DOUBLE,  DOUBLE_V,
		 LONG,    LONG_V,	     
		 U_LONG,  U_LONG_V,
		 LORENTZVD,   LORENTZVP,   
		 LORENTZVD_V, LORENTZVP_V, 
		 LORENTZVF, LORENTZVF_V,
		 POINTD,   VECTORD,
		 POINTD_V, VECTORD_V,
		 POINTF, POINTF_V, VECTORF, VECTORF_V,
		 STRING,     STRING_BOOL_M, STRING_INT_M, STRING_STRING_M, 
		 GENJET_V, DJCANDIDATE_V};

  static std::map<std::string,LEAFTYPE> dict();
};

#endif
