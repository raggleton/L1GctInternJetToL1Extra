# L1GctInternJetToL1Extra

This EDProducer module converts the L1 GCT internal jets collection (in format L1GctInternJetDataCollection) into a collection of L1 Jet Particles. (L1JetParticleCollection). This means you can then pass the collection to the L1ExtraTreeProducer, like any other jet collection, to be kept in a NTuple.

Basically, combining this module with L1ExtraTreeProducer you can do:

L1GctInternJetDataCollection --[via this module]-> L1JetParticleCollection --[L1ExtraTreeProducer]-> L1Ntuple (in l1Extra format).

This should really be integrated into the l1Extra Particle Producer, but kept separate atm for backup purposes. 

##Producing GCT internal jets collection

Not seen documented elsewhere, so here it is. You will need to add the following snippet to your config file:
```
# To remake GCT digis
process.load("Configuration.StandardSequences.RawToDigi_cff")

# GCT emulator (to make simGctDigis)
process.load('Configuration/StandardSequences/SimL1Emulator_cff')

# change GCT emulator to take inputs from GCT unpacker (the 'gctdigis')
process.simGctDigis.inputLabel = cms.InputTag('gctDigis')
process.simGctDigis.writeInternalData = cms.bool(True)

# add to process path:
process.p = cms.Path(
    ...
    + process.gctDigis
    + process.simGctDigis
    ...
    )
``` 
