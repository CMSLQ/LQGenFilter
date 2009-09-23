import FWCore.ParameterSet.Config as cms

from Configuration.GenProduction.PythiaUESettings_cfi import *
source = cms.Source("PythiaSource",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.untracked.double(10000.0),
    crossSection = cms.untracked.double(0.1121),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('PMAS(42,1)=500.0        ! LQ mass', 
            'IMSS(21)=33             ! LUN number for SLHA File (must be 33)', 
            'IMSS(22)=33             ! Read-in SLHA decay table', 
            'MDCY(C111,1)=0          ! ', 
            'MSEL=0                  ! (D=1) to select between full user control (0, then use MSUB) and some preprogrammed alternative', 
            'MSUB(163)=1             ! g+g->LQ+LQbar', 
            'MSUB(164)=1             ! q+qbar->LQ+LQbar'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters',
            'SLHAParameters'),
        SLHAParameters = cms.vstring('SLHAFILE = Leptoquarks/LQGenFilter/data/LQ_cmu_beta1.0.out')
    )
)

configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.2 $'),
        name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/UserCode/Leptoquarks/LQGenFilter/python/PYTHIA6_Exotica_LQ_cmu_500_10TeV_mumujj_cff.py,v $'),
        annotation = cms.untracked.string('default documentation string for PYTHIA6_Exotica_LQ_cmu_500_10TeV_mumujj_cff.py')
)
