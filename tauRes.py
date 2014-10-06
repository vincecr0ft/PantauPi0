from ROOT import TFile,TChain
from ROOT import gDirectory
from ROOT import TLorentzVector
from ROOT import TH1F,TCanvas
from ROOT import gROOT


from calcTauVisibleSum import TauDecayMC
from calcTauSubstructure import TauSubstruct
from TauClass import Tau
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

a={"name":"Normal-Normal","BDTvalue":0.0,"Cutvalue":0.0} 
b={"name":"Loose-Normal","BDTvalue":-0.25,"Cutvalue":0.0} 
c={"name":"ExtraLoose-Normal","BDTvalue":-0.5,"Cutvalue":0.0} 
d={"name":"Public-Normal","BDTvalue":-2.0,"Cutvalue":0.0} 
e={"name":"Tight-Normal","BDTvalue":0.25,"Cutvalue":0.0} 

f={"name":"Normal-Loose","BDTvalue":0.0,"Cutvalue":250} 
g={"name":"Loose-Loose","BDTvalue":-0.25,"Cutvalue":250} 
h={"name":"ExtraLoose-Loose","BDTvalue":-0.5,"Cutvalue":250} 
i={"name":"Public-Loose","BDTvalue":-2,"Cutvalue":250} 
j={"name":"Tight-Loose","BDTvalue":0.25,"Cutvalue":250} 

k={"name":"Normal-Looser","BDTvalue":0.0,"Cutvalue":500} 
l={"name":"Loose-Looser","BDTvalue":-0.25,"Cutvalue":500} 
m={"name":"ExtraLoose-Looser","BDTvalue":-0.5,"Cutvalue":500} 
n={"name":"Public-Looser","BDTvalue":-2,"Cutvalue":500} 
o={"name":"Tight-Looser","BDTvalue":0.25,"Cutvalue":500} 

p={"name":"Normal-ExtraLoose","BDTvalue":0.0,"Cutvalue":1000} 
q={"name":"Loose-ExtraLoose","BDTvalue":-0.25,"Cutvalue":1000} 
r={"name":"ExtraLoose-ExtraLoose","BDTvalue":-0.5,"Cutvalue":1000} 
s={"name":"Public-ExtraLoose","BDTvalue":-2,"Cutvalue":1000} 
t={"name":"Tight-ExtraLoose","BDTvalue":0.25,"Cutvalue":1000} 

u={"name":"Normal-Tight","BDTvalue":0.0,"Cutvalue":-250} 
v={"name":"Loose-Tight","BDTvalue":-0.25,"Cutvalue":-250} 
w={"name":"ExtraLoose-Tight","BDTvalue":-0.5,"Cutvalue":-250} 
x={"name":"Public-Tight","BDTvalue":-2,"Cutvalue":-250} 
y={"name":"Tight-Tight","BDTvalue":0.25,"Cutvalue":-250} 


cuts=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y]
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
   

   visTaus=TauDecayMC(ch)
   first=True
   for cut in cuts:
      
      cellTaus=TauSubstruct(ch,cut["BDTvalue"],cut["Cutvalue"])
      for tau in cellTaus:

         for trueTau in visTaus:
            Pi=3.14159265359
            dEta=tau.eta-trueTau.eta
            dPhi=Pi-abs(abs(tau.phi-trueTau.phi)-Pi)
            dR=(dEta*dEta+dPhi*dPhi)**0.5

            if dR<0.2:
   
               res=(tau.pt-trueTau.pt)/trueTau.pt
               if tau.pt>15000 and abs(tau.eta)<2.5:

                  for bdt in bdtcuts:
                     ok =False
                     if bdt=="BDTnone":ok=True
                     if bdt=="BDTloose":ok=tau.BDTloose
                     if bdt=="BDTmedium":ok=tau.BDTmedium
                     if bdt=="BDTtight":ok=tau.BDTtight

                     if ok==True:
                        
                        if trueTau.trueN>0 and tau.cellN>0:
                           neutralRes=(tau.cellSum-trueTau.trueSum)/trueTau.trueSum
                           leadPi0Res=(tau.cellLead-trueTau.trueLead)/trueTau.trueLead

                           cut[bdt].histos['sumRes'].Fill(neutralRes)
                           cut[bdt].histos['leadRes'].Fill(leadPi0Res)
                        
                        if first:
                           cellRes=(tau.cellPt-trueTau.pt)/trueTau.pt                     
                           cut[bdt].histos['cellres'].Fill(res-cellRes)

                        if trueTau.trueP==1:
                           if trueTau.trueN==0:
                              if tau.cellP==1:
                                 if tau.cellN==0: cut[bdt].histos['1P0N-1P0N'].Fill(res)
                                 elif tau.cellN==1:cut[bdt].histos['1P0N-1P1N'].Fill(res)
                                 else:  cut[bdt].histos['1P0N-1PXN'].Fill(res)
                              else:  cut[bdt].histos['1P0N-3P'].Fill(res)
                           elif trueTau.trueN==1:
                              if tau.cellP==1:
                                 if tau.cellN==0:  cut[bdt].histos['1P1N-1P0N'].Fill(res)
                                 elif tau.cellN==1: cut[bdt].histos['1P1N-1P1N'].Fill(res)
                                 else:  cut[bdt].histos['1P1N-1PXN'].Fill(res)
                              else:  cut[bdt].histos['1P1N-3P'].Fill(res)
                           else:
                              if tau.cellP==1:
                                 if tau.cellN==0:  cut[bdt].histos['1PXN-1P0N'].Fill(res)
                                 elif tau.cellN==1: cut[bdt].histos['1PXN-1P1N'].Fill(res)
                                 else:  cut[bdt].histos['1PXN-1PXN'].Fill(res)
                              else:  cut[bdt].histos['1PXN-3P'].Fill(res)
                        else:
                           if trueTau.trueN==0:
                              if tau.cellP==3:
                                 if tau.cellN==0:  cut[bdt].histos['3P0N-3P0N'].Fill(res)
                                 else:  cut[bdt].histos['3P0N-3PXN'].Fill(res)
                              else:  cut[bdt].histos['3P0N-1P'].Fill(res)
                           else:
                              if tau.PanTauFlag==True and (tau.cellP!=3 or tau.cellN==0):
                                 cut[bdt].histos['Pantau'].Fill(res)
                              if tau.cellP==3:
                                 if tau.cellN==0:  cut[bdt].histos['3PXN-3P0N'].Fill(res)
                                 else:  cut[bdt].histos['3PXN-3PXN'].Fill(res)
                              else:  cut[bdt].histos['3PXN-1P'].Fill(res)
      first=False


   if jentry%100==0: print "event number",jentry

output.Write()
output.Close()
