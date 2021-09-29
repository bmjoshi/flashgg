import ROOT
from DataFormats.FWLite import Events, Handle
#import numpy as np


events = Events('/tmp/bjoshi/964F3DD8-C77E-9346-8C6A-A95AC4EDF2C7.root')
handle = Handle('std::vector<pat::PackedGenParticle>')
label = ("packedGenParticles","","PAT") 

'''
for count, e in enumerate(events,1):
   e.getByLabel(label,handle)
   genParticles = handle.product()
   nMu = 0
   print("Analyzing event: {:d}".format(count))
   for p in genParticles:
      if not(abs(p.pdgId())==13): continue;
      nMu += 1
      print("Muon Pt: {:2f}, Eta: {:2f}, Phi: {:2f}".format(p.pt(),p.eta(),p.phi()))
   print("Total number of muons: {:d}".format(nMu))
'''

handle_lheevent = Handle('LHEEventProduct')
label_lheevent = ("externalLHEProducer","","SIM")

for count, e in enumerate(events, 1):
    if count>2: continue
    e.getByLabel(label_lheevent, handle_lheevent)
    lhe = handle_lheevent.product()
    print("npLO: {}".format(lhe.npLO()))
    print("npNLO: {}".format(lhe.npNLO()))
    pdf = lhe.pdf()
    #print("pdf")
    #print("ID:{}, x: {}, xpdf: {}, scalepdf: {}".format(pdf.id, pdf.x, pdf.xPDF, pdf.scalePDF))
    for scale_ in lhe.scales(): print(scale_)
    for weight_ in lhe.weights(): print("Id:{}, weight:{}".format(weight_.id(), weight_.wgt()))
