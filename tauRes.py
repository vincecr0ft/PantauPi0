from ROOT import TFile,TChain
from ROOT import gDirectory
from ROOT import TLorentzVector
from ROOT import TH1F,TCanvas
from ROOT import gROOT


from calcTauVisibleSum import TauDecayMC
from calcTauSubstructure import TauSubstruct
from TauClass import Tau
from HistoClass import ListoHistos

import sys

gROOT.ProcessLine(".L loader.C+")


# Open files
files=sys.argv[-1].split(',')
for filename in files:
#files='../../pier/ntuples/user.*.root'
   ch = TChain('tau')
   ch.Add(filename)
   print "adding %s to inputs" % files
# retrieve the ntuple of interest
#ch = gDirectory.Get( 'tau' )

ch.SetBranchStatus("*",0)
ch.SetBranchStatus("mc_*",1)
ch.SetBranchStatus("tau_*",1)
ch.SetBranchStatus("tau_*",1)
ch.SetBranchStatus("trueTau_*",1)
ch.SetBranchStatus("EventNumber",1)

entries = ch.GetEntriesFast()

a={"name":"normal","value":0.0} 
b={"name":"tightened","value":0.25} 
c={"name":"loosened","value":-0.25}
d={"name":"loose","value":0.5} 
e={"name":"tight","value":-0.5}
f={"name":"public","value":-2.0}
g={"name":"cons","value":2.0}
cuts=[a,b,c,d,e,f,g]

output = TFile('resolutionHistos.root','RECREATE')

for cut in cuts:
   cut["name"]=ListoHistos(cut["name"])

for jentry in xrange( entries ):
 # get the next tree in the ch and verify
   ientry = ch.LoadTree( jentry )
   if ientry < 0:
      break

 # copy next entry into memory and verify
   nb = ch.GetEntry( jentry )
   if nb <= 0:
      continue

 # use the values directly from the tree
   EventNumber = int(ch.EventNumber)
   if EventNumber < 0:
     continue
   

   visTaus=TauDecayMC(ch)

   for cut in cuts:
      
      cellTaus=TauSubstruct(ch,cut["value"])
      for tau in cellTaus:

         for trueTau in visTaus:
            Pi=3.14159265359
            dEta=tau.eta-trueTau.eta
            dPhi=Pi-abs(abs(tau.phi-trueTau.phi)-Pi)
            dR=(dEta*dEta+dPhi*dPhi)**0.5

            if dR<0.4:
   
               res=(tau.pt-trueTau.pt)/trueTau.pt
               cut["name"].h_trueneutrals.Fill(trueTau.trueN)
               cut["name"].h_cellneutrals.Fill(tau.cellN)
               cut["name"].h_trueprong.Fill(trueTau.trueP)
               cut["name"].h_cellprong.Fill(tau.cellP)
               cut["name"].h_dR.Fill(dR)

               if tau.pt>15000:
                  if tau.cellP==1 and tau.cellN==0:
                     if trueTau.trueP==1:
                        if trueTau.trueN==0:
                           cut["name"].h_reco1P0N_true1P0N.Fill(res)
                        elif trueTau.trueN==1:
                           cut["name"].h_reco1P0N_true1P1N.Fill(res)
                        else:
                           cut["name"].h_reco1P0N_true1PXN.Fill(res)
                     else:
                        cut["name"].h_reco1P0N_true3P.Fill(res)
                  elif tau.cellP==1 and tau.cellN==1:
                     if trueTau.trueP==1:
                        if trueTau.trueN==0:
                           cut["name"].h_reco1P1N_true1P0N.Fill(res)
                        elif trueTau.trueN==1:
                           cut["name"].h_reco1P1N_true1P1N.Fill(res)
                        else:
                           cut["name"].h_reco1P1N_true1PXN.Fill(res)
                     else:
                        cut["name"].h_reco1P1N_true3P.Fill(res)
                  elif tau.cellP==1 and tau.cellN>1:
                     if trueTau.trueP==1:
                        if trueTau.trueN==0:
                           cut["name"].h_reco1PXN_true1P0N.Fill(res)
                        elif trueTau.trueN==1:
                           cut["name"].h_reco1PXN_true1P1N.Fill(res)
                        else:
                           cut["name"].h_reco1PXN_true1PXN.Fill(res)
                     else:
                        cut["name"].h_reco1PXN_true3P.Fill(res)
   if jentry%100==0: print "event number",jentry

output.Write()
output.Close()
