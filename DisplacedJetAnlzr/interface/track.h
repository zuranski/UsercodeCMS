#ifndef MyAnalysis_DisplacedJetAnlzr_track_h
#define MyAnalysis_DisplacedJetAnlzr_track_h

struct track {

   double pt,eta,phi,vtxpt,vtxeta,vtxphi,chi2,ip2d,ip3d,ip2dsig,ip3dsig,lxy,vlxy,vtxweight,guesslxy;
   int nHits,nPixHits,algo,exo,pdgid,momid,charge;
   int nHitsInFrontOfVert,nMissHitsAfterVert;

};

#endif
