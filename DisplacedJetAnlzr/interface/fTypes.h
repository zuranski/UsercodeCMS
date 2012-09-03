#ifndef DJ_FTYPES
#define DJ_FTYPES

#include <map>
#include <string>

struct fTypes {

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
		 STRING,     STRING_BOOL_M, STRING_INT_M, STRING_STRING_M, 
		 STRING_V};

  static std::map<std::string,LEAFTYPE> dict();
};

#endif
