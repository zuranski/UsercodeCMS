import FWCore.ParameterSet.Config as cms
# Select exotics decaying to qq (uds).
import GeneratorInterface.GenFilters.XtoFFbarFilter_cfi
djsignalfilteruds = GeneratorInterface.GenFilters.XtoFFbarFilter_cfi.XtoFFbarFilter.clone(
   # exotic -> uds
   idMotherX = cms.vint32(6000111),
   idMotherY = cms.vint32(6000111),
   idDaugtherX = cms.vint32(),
   idDaugtherY = cms.vint32()
)
