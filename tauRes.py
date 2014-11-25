from ROOT import TFile,TChain
from ROOT import gDirectory
from ROOT import TLorentzVector
from ROOT import TH1F,TCanvas
from ROOT import gROOT


from calcTauVisibleSum import TauDecayMC
from calcTauSubstructure import TauSubstruct
from TauClass import Tau
from HistoClass import ListoHistos
from CutGrid import CutList

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
bdtcuts=['BDTnone','BDTloose','BDTmedium','BDTtight','ExoticVeto']

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
   

   visTaus=TauDecayMC(ch)
   first=True
   for cut in cuts:
      
      cellTaus=TauSubstruct(ch,cut["BDTvalue"],cut["Cutvalue"])
      for tau in cellTaus:

         for trueTau in visTaus:
#            Pi=3.14159265359
#            dEta=tau.eta-trueTau.eta
#            dPhi=Pi-abs(abs(tau.phi-trueTau.phi)-Pi)
#            dR=(dEta*dEta+dPhi*dPhi)**0.5

            dR=tau.cellTau.DeltaR(trueTau.trueTau)

            if dR<0.2 and tau.pt>15000 and abs(tau.eta)<2.5:
   
               res=(tau.pt-trueTau.pt)/trueTau.pt
               if tau.pt>15000 and abs(tau.eta)<2.5:
#                  print 'matching %f with %f and eta at %f -%f'%(tau.pt,trueTau.pt,tau.eta,trueTau.eta)
                  for bdt in bdtcuts:
                     ok =False
                     if bdt=="BDTnone":ok=True
                     if bdt=="BDTloose":ok=tau.BDTloose
                     if bdt=="BDTmedium":ok=tau.BDTmedium
                     if bdt=="BDTtight":ok=tau.BDTtight
                     if bdt=="ExoticVeto":ok=not trueTau.ExoticVeto
                     if ok==True:
                        
                        #make standard values
                        if trueTau.trueN>0 and tau.cellN>0 and trueTau.trueLead>10:
                           neutralRes=(tau.cellSum-trueTau.trueSum)/trueTau.trueSum
                           leadPi0Res=(tau.cellLead-trueTau.trueLead)/trueTau.trueLead
                           cut[bdt].histos['sumRes'].Fill(neutralRes)
                           cut[bdt].histos['leadRes'].Fill(leadPi0Res)
                        #formerly used for checks, after bug fix currently not used.
                        elif trueTau.trueLead<10. and trueTau.trueN>0:
                           trueTau.trueN=0

                        #check nominal values
                        if first:
                           cellRes=(tau.cellPt-trueTau.pt)/trueTau.pt                     
                           cut[bdt].histos['cellres'].Fill(res-cellRes)
                           cut[bdt].histos['cellbased'].Fill((tau.cellTau.Pt()-trueTau.pt)/trueTau.pt)
                           cut[bdt].histos['PanTau'].Fill((tau.panTauPt-trueTau.pt)/trueTau.pt)

                        #set Cell ID
                        if tau.cellP==1:
                           if tau.cellN==0:tau.CellID=0
                           elif tau.cellN==1:tau.CellID=1
                           else: tau.CellID=2
                        elif tau.cellP==3:
                           if tau.cellN==0:tau.CellID=3
                           else: tau.CellID=4
                        else: tau.CellID=5

                        if trueTau.trueP==1:
                           if trueTau.trueN==0:
                              if tau.PanTauID!=tau.CellID: cut[bdt].histos['Miss1P0N'].Fill(res)
                              if tau.cellP==1:
                                 if tau.cellN==0: cut[bdt].histos['1P0N-1P0N'].Fill(res)
                                 elif tau.cellN==1:cut[bdt].histos['1P0N-1P1N'].Fill(res)
                                 else:  cut[bdt].histos['1P0N-1PXN'].Fill(res)
                              else:  cut[bdt].histos['1P0N-3P'].Fill(res)
                           elif trueTau.trueN==1:
                              if tau.PanTauID!=tau.CellID: cut[bdt].histos['Miss1P1N'].Fill(res)
                              if tau.cellP==1:
                                 if tau.cellN==0:  cut[bdt].histos['1P1N-1P0N'].Fill(res)
                                 elif tau.cellN==1: 
                                    cut[bdt].histos['1P1N-1P1N'].Fill(res)
                                    cut[bdt].histos['1Pneutral'].Fill(neutralRes)
                                 else:  cut[bdt].histos['1P1N-1PXN'].Fill(res)
                              else:  cut[bdt].histos['1P1N-3P'].Fill(res)
                           else:
                              if tau.PanTauID!=tau.CellID: cut[bdt].histos['Miss1PXN'].Fill(res)
                              if tau.cellP==1:
                                 if tau.cellN==0:  cut[bdt].histos['1PXN-1P0N'].Fill(res)
                                 elif tau.cellN==1: cut[bdt].histos['1PXN-1P1N'].Fill(res)
                                 else:  cut[bdt].histos['1PXN-1PXN'].Fill(res)
                              else:  cut[bdt].histos['1PXN-3P'].Fill(res)
                        else:
                           if trueTau.trueN==0:
                              if tau.PanTauID!=tau.CellID: cut[bdt].histos['Miss3P0N'].Fill(res)
                              if tau.cellP==3:
                                 if tau.cellN==0:  cut[bdt].histos['3P0N-3P0N'].Fill(res)
                                 else:  cut[bdt].histos['3P0N-3PXN'].Fill(res)
                              else:  cut[bdt].histos['3P0N-1P'].Fill(res)
                           else:
                              if tau.PanTauID!=tau.CellID: cut[bdt].histos['Miss3PXN'].Fill(res)
                              if tau.cellP==3:
                                 if tau.cellN==0:  cut[bdt].histos['3PXN-3P0N'].Fill(res)
                                 else:  
                                    cut[bdt].histos['3PXN-3PXN'].Fill(res)
                                    cut[bdt].histos['2D_neutral'].Fill(neutralRes,tau.nClusters)
                                    cut[bdt].histos['3Pneutral'].Fill(neutralRes)
                              else:  cut[bdt].histos['3PXN-1P'].Fill(res)
      first=False


   if jentry%100==0: print "event number",jentry

output.Write()
output.Close()
