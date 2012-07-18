# Select exotics decaying to qq or bb.
import GeneratorInterface.GenFilters.XtoFFbarFilter_cfi
process.filterSignalMC = GeneratorInterface.GenFilters.XtoFFbarFilter_cfi.XtoFFbarFilter.clone(
   # exotic -> b
   idMotherX = cms.vint32(6000112),
   idMotherY = cms.vint32(6000112),
   idDaugtherX = cms.vint32(),
   idDaugtherY = cms.vint32()
)

if dataType=='u':
   # exotic -> uds
   process.filterSignalMC.idMotherX = cms.vint32(6000111)
   process.filterSignalMC.idMotherY = cms.vint32(6000111)

process.filterSignalMCSeq = cms.Sequence(process.filterSignalMC)
