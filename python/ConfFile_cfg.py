import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/work/r/raggleto/L1JEC/CMSSW_7_2_0_pre7/src/L1Trigger/L1TCalorimeter/test/SimGCTEmulator.root'
    )
)

process.gctInternJetToL1Extra = cms.EDProducer('L1GctInternJetToL1Extra',
    gctInternJetSource = cms.InputTag("simGctDigis")
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.gctInternJetToL1Extra)

process.e = cms.EndPath(process.out)
