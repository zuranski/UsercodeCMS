import FWCore.ParameterSet.Config as cms
# Select exotics decaying to qq (b).
import GeneratorInterface.GenFilters.XtoFFbarFilter_cfi
djsignalfilterb = GeneratorInterface.GenFilters.XtoFFbarFilter_cfi.XtoFFbarFilter.clone(
   # exotic -> b
   idMotherX = cms.vint32(6000112),
   idMotherY = cms.vint32(6000112),
   idDaugtherX = cms.vint32(),
   idDaugtherY = cms.vint32()
)
