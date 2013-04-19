import FWCore.ParameterSet.Config as cms
# Select exotics decaying to qq (uds).
import GeneratorInterface.GenFilters.XtoFFbarFilter_cfi
djsignalfilter = GeneratorInterface.GenFilters.XtoFFbarFilter_cfi.XtoFFbarFilter.clone(
   # exotic -> uds
   idMotherX = cms.vint32(6001114,6002114,6003114),
#   idMotherY = cms.vint32(6001114,6002114,6003114),
   idMotherY = cms.vint32(),
   idDaugtherX = cms.vint32(1,2,3,4,5),
#   idDaugtherY = cms.vint32(1,2,3,4,5)
   idDaugtherY = cms.vint32()
)
