from ROOT import TFile,TChain
from ROOT import gDirectory
from ROOT import TLorentzVector as TLV
from ROOT import TH1F,TCanvas
from ROOT import gROOT


from calcTauVisibleSum import TauDecayMC
from calcTauSubstructure import TauSubstruct
from TauClass import Tau
from CutGrid import CutList
#from HistoClass import ListoHistos
from testClass import ListoHistos

import sys

gROOT.ProcessLine(".L loader.C+")


# Open files
files=sys.argv[-1].split(',')
ch = TChain('tau')
for filename in files:
   ch.Add(filename)
   print "adding %s to inputs" % filename

ch.SetBranchStatus("*",0)
ch.SetBranchStatus("mc_*",1)
ch.SetBranchStatus("tau_*",1)
ch.SetBranchStatus("tau_*",1)
ch.SetBranchStatus("trueTau_*",1)
ch.SetBranchStatus("EventNumber",1)

entries = ch.GetEntriesFast()
cuts=CutList()
bdtcuts=['BDTnone','BDTloose','BDTmedium','BDTtight']

selection={'name':bdtcuts}
plots=['1P0N-1P0N','1P0N-1P1N','1P0N-1PXN','1P0N-3P',
       '1P1N-1P0N','1P1N-1P1N','1P1N-1PXN','1P1N-3P',
       '1PXN-1P0N','1PXN-1P1N','1PXN-1PXN','1PXN-3P',
       '3P0N-1P','3P0N-3P0N','3P0N-3PXN',
       '3PXN-1P','3PXN-3P0N','3PXN-3PXN']



output = TFile('resolutionHistos.root','RECREATE')


for cut in cuts:
   for bdt in bdtcuts:
      hist=cut['name']+'_'+bdt
      cut[bdt]=ListoHistos(hist,plots)

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
   

#   visTaus=TauDecayMC(ch)
#   for cut in cuts:
      
   cellTaus=TauSubstruct(ch)
   trueTaus=TauDecayMC(ch)

   for tau in cellTaus:
      dR=10.
      dPt=10000
      tauTLV=TLV(0,0,0,0)
      tauTLV.SetPtEtaPhiM(tau.pt,tau.eta,tau.phi,tau.m)
      for trueTau in trueTaus:
         trueTLV=TLV(0,0,0,0)
         trueTLV.SetPtEtaPhiM(trueTau.pt,trueTau.eta,trueTau.phi,trueTau.m)
         if tauTLV.DeltaR(trueTLV)<dR and abs(tauTLV.Pt()-trueTLV.Pt())<dPt:
            dR=tauTLV.DeltaR(trueTLV)
            dPt=abs(tauTLV.Pt()-trueTLV.Pt())
            tau.trueSum=trueTau.trueSum
            tau.trueLead=trueTau.trueLead
            if tau.trueLead>tau.trueSum: print 'nononononono',tau.trueTau.Pt(),' ',trueTau.pt
            tau.ExoticFlag=trueTau.ExoticFlag
      for bdt in bdtcuts:
         ok =False
         if bdt=="BDTnone":ok=True
         if bdt=="BDTloose":ok=tau.BDTloose
         if bdt=="BDTmedium":ok=tau.BDTmedium
         if bdt=="BDTtight":ok=tau.BDTtight

         if ok==True and tau.matched==True and tau.pt>1500 and abs(tau.eta)<2.5 and tau.ExoticFlag==False:                        
            for cut in cuts: 
               name=cut["name"]

               if tau.trueN>0 and tau.cellN>0 and tau.trueLead>0:
                  neutralRes=(tau.cellSum-tau.trueSum)/tau.trueSum
                  leadPi0Res=(tau.cellLead-tau.trueLead)/tau.trueLead

                  cut[bdt].histos['sumRes'].Fill(neutralRes)
                  cut[bdt].histos['leadRes'].Fill(leadPi0Res)
               if tau.trueP==1:
                  if tau.trueN==0:
                     if tau.cellP==1:
                        if tau.cellN==0:cut[bdt].histos['1P0N-1P0N'].Fill(tau.cuts[name]['res'])
                        elif tau.cellN==1:cut[bdt].histos['1P0N-1P1N'].Fill(tau.cuts[name]['res'])
                        else:  cut[bdt].histos['1P0N-1PXN'].Fill(tau.cuts[name]['res'])
                     else:  cut[bdt].histos['1P0N-3P'].Fill(tau.cuts[name]['res'])
                  elif tau.trueN==1 and tau.trueLead>0:
                     if tau.cellP==1:
                        if tau.cellN==0:  cut[bdt].histos['1P1N-1P0N'].Fill(tau.cuts[name]['res'])
                        elif tau.cellN==1:  
                           cut[bdt].histos['1P1N-1P1N'].Fill(tau.cuts[name]['res'])
                           cut[bdt].histos['1P1N-1P1N'].Fill((tau.cuts[name]['neutralSum']-tau.trueSum)/tau.trueSum)
                        else:  cut[bdt].histos['1P1N-1PXN'].Fill(tau.cuts[name]['res'])
                     else:  cut[bdt].histos['1P1N-3P'].Fill(tau.cuts[name]['res'])
                  else:
                     if tau.cellP==1:
                        if tau.cellN==0:  cut[bdt].histos['1PXN-1P0N'].Fill(tau.cuts[name]['res'])
                        elif tau.cellN==1: cut[bdt].histos['1PXN-1P1N'].Fill(tau.cuts[name]['res'])
                        else:  cut[bdt].histos['1PXN-1PXN'].Fill(tau.cuts[name]['res'])
                     else:  cut[bdt].histos['1PXN-3P'].Fill(tau.cuts[name]['res'])
               else:
                  if tau.trueN==0:
                     if tau.cellP==3:
                        if tau.cellN==0:  cut[bdt].histos['3P0N-3P0N'].Fill(tau.cuts[name]['res'])
                        else:  cut[bdt].histos['3P0N-3PXN'].Fill(tau.cuts[name]['res'])
                     else:  cut[bdt].histos['3P0N-1P'].Fill(tau.cuts[name]['res'])
                  elif tau.trueLead>0:
                     if tau.cellP==3:
                        if tau.cellN==0:  cut[bdt].histos['3PXN-3P0N'].Fill(tau.cuts[name]['res'])
                        else:
                           cut[bdt].histos['3PXN-3PXN'].Fill(tau.cuts[name]['res'])
                           cut[bdt].histos['3PXN-3PXN'].Fill((tau.cuts[name]['neutralSum']-tau.trueSum)/tau.trueSum)
                     else:  cut[bdt].histos['3PXN-1P'].Fill(tau.cuts[name]['res'])
                     


   if jentry%100==0: print "event number",jentry

output.Write()
output.Close()
