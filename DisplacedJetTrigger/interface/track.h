#ifndef MyAnalysis_DisplacedJetTrigger_track_h
#define MyAnalysis_DisplacedJetTrigger_track_h

struct track {

   double pt,eta,phi,chi2,dxy,dz,ip3d,dxysig,ip3dsig;
   int nHits,nPixHits,algo;

};

#endif
