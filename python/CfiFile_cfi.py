import FWCore.ParameterSet.Config as cms

L1GctInternJetToL1Extra = cms.EDProducer('L1GctInternJetToL1Extra',
    gctInternJetSource = cms.InputTag("simGctDigis")
)
