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
# Open files

#files=sys.argv[-1].split(',')
#for filename in files:
files='../../pier/ntuples/user.*.root'
ch = TChain('tau')
ch.Add(files)
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
cuts=[a,b,c]

output = TFile('resolutionHistos.root','RECREATE')

for cut in cuts:
   cut["name"]=ListoHistos(cut["name"])

"""
h_reco1P1N=TH1F('h_reco1P1N','Correctly identified 1p1n taus',40,-2.,2.)
h_reco1P1N_true1P0N=TH1F('h_reco1P1N_true1P0N','Reco 1P1N true 1P0N',40,-2.,2.)
h_reco1P1N_true1PXN=TH1F('h_reco1P1N_true1PXN','Reco 1P1N true 1PXN',40,-2.,2.)
h_reco1P1N_true3P=TH1F('h_reco1P1N_true3P','Reco 1P1N true 3P',40,-2.,2.)
h_3p=TH1F('h_3p','Reco 3 prong taus',40,-2.,2.)
h_3p3p=TH1F('h_3p3p','Correct reco 3 prong taus',40,-2.,2.)

h_trueprong=TH1F('h_trueprong','number of prongs',5,0.,5.)
h_trueneutrals=TH1F('h_trueneutrals','number of neutrals',5,0.,5.)
h_cellprong=TH1F('h_cellprong','number of prongs',5,0.,5.)
h_cellneutrals=TH1F('h_cellneutrals','number of neutrals',5,0.,5.)
"""


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
            dEta=tau.eta-trueTau.eta
            dPhi=tau.phi-trueTau.phi
            dR=(dEta*dEta+dPhi*dPhi)**0.5

            if dR<0.4:
   
               res=(tau.pt-trueTau.pt)/trueTau.pt
               cut["name"].h_trueneutrals.Fill(trueTau.trueN)
               cut["name"].h_cellneutrals.Fill(tau.cellN)
               cut["name"].h_trueprong.Fill(trueTau.trueP)
               cut["name"].h_cellprong.Fill(tau.cellP)

               if tau.cellP==1 and tau.cellN==1:
                  if trueTau.trueP==1:
                     if trueTau.trueN==1:
                        cut["name"].h_reco1P1N.Fill(res)
                     elif trueTau.trueN==0:
                        cut["name"].h_reco1P1N_true1P0N.Fill(res)
                     else:
                        cut["name"].h_reco1P1N_true1PXN.Fill(res)
                  else:
                     cut["name"].h_reco1P1N_true3P.Fill(res)
                     
               elif tau.cellP==3:
                  cut["name"].h_3p.Fill(res)
                  if trueTau.trueP==3:
                     cut["name"].h_3p3p.Fill(res)
   

   if jentry%100==0: print "event number",jentry

output.Write()
output.Close()
