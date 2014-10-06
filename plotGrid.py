from ROOT import TFile,TCanvas,TH1F,TH2F,THStack
from testClass import ListoHistos

infile=TFile('resolutionHistos.root')

a={"name":"Normal-Normal","BDTvalue":0.0,"Cutvalue":0.0}
b={"name":"Loose-Normal","BDTvalue":-0.25,"Cutvalue":0.0}
c={"name":"ExtraLoose-Normal","BDTvalue":-0.5,"Cutvalue":0.0}
d={"name":"Public-Normal","BDTvalue":-2.0,"Cutvalue":0.0}

e={"name":"Normal-Loose","BDTvalue":0.0,"Cutvalue":250}
f={"name":"Loose-Loose","BDTvalue":-0.25,"Cutvalue":250}
g={"name":"ExtraLoose-Loose","BDTvalue":-0.5,"Cutvalue":250}
h={"name":"Public-Loose","BDTvalue":-2,"Cutvalue":250}

i={"name":"Normal-Looser","BDTvalue":0.0,"Cutvalue":500}
j={"name":"Loose-Looser","BDTvalue":-0.25,"Cutvalue":500}
k={"name":"ExtraLoose-Looser","BDTvalue":-0.5,"Cutvalue":500}
l={"name":"Public-Looser","BDTvalue":-2,"Cutvalue":500}

m={"name":"Normal-ExtraLoose","BDTvalue":0.0,"Cutvalue":1000}
n={"name":"Loose-ExtraLoose","BDTvalue":-0.25,"Cutvalue":1000}
o={"name":"ExtraLoose-ExtraLoose","BDTvalue":-0.5,"Cutvalue":1000}
p={"name":"Public-ExtraLoose","BDTvalue":-2,"Cutvalue":1000}
cuts=[a,b,c,d,e,f,g,h,i,j,k,l]
modes={'1P0N-1P0N':2,'1P0N-1P1N':4,'1P0N-1PXN':6,'1P0N-3P':8,
       '1P1N-1P0N':2,'1P1N-1P1N':4,'1P1N-1PXN':6,'1P1N-3P':8,
       '1PXN-1P0N':2,'1PXN-1P1N':4,'1PXN-1PXN':6,'1PXN-3P':8,
       '3P0N-1P':2,'3P0N-3P0N':6,'3P0N-3PXN':8,
       '3PXN-1P':2,'3PXN-3P0N':6,'3PXN-3PXN':8}
BDTs=['BDTnone','BDTloose','BDTmedium','BDTtight']
plots={}
Grid=TH2F('grid','grid',4,0,4,4,0,4)
for cut in cuts:
   cut[cut['name']]=TH1F(cut['name'],cut['name'],40,-2,2)
   for bdt in BDTs:
      cut[bdt]=TH1F(cut['name']+'_'+bdt,cut['name']+'_'+bdt,40,-2,2)
      for mode in modes:
         plots[mode]=infile.Get(mode+'_'+cut['name']+'_'+bdt)
         cut[bdt].Add(plots[mode])
   cut[cut['name']].Add(cut['BDTnone'])
   cut['sig0']=cut[cut['name']].GetRMS()
   temp=cut[cut['name']].Clone()
   lower=temp.GetMean()-3*cut['sig0']
   upper=temp.GetMean()+3*cut['sig0']
   for bin in range(1,temp.GetNbinsX()+1):
      thisbin=temp.GetBinCenter(bin)
      if thisbin<lower or thisbin>upper:
         temp.SetBinContent(bin,0)
   cut['3SigRMS']=temp.GetRMS()
   print 'cut %s has 3SigRMS of %f'%(cut['name'],cut['3SigRMS'])

Grid.GetXaxis().SetBinLabel(1,'Normal')
Grid.GetXaxis().SetBinLabel(2,'BDT '+str(cuts[1]['BDTvalue']))
Grid.GetXaxis().SetBinLabel(3,'BDT '+str(cuts[2]['BDTvalue']))
Grid.GetXaxis().SetBinLabel(4,'No BDT requirement')
Grid.GetYaxis().SetBinLabel(1,'Normal')
Grid.GetYaxis().SetBinLabel(2,'Pt '+str(cuts[4]['Cutvalue']))
Grid.GetYaxis().SetBinLabel(3,'Pt '+str(cuts[8]['Cutvalue']))
#Grid.GetYaxis().SetBinLabel(4,'Pt '+str(cuts[12]['Cutvalue']))

Grid.SetBinContent(1,1,cuts[0]['3SigRMS'])
Grid.SetBinContent(2,1,cuts[1]['3SigRMS'])
Grid.SetBinContent(3,1,cuts[2]['3SigRMS'])
Grid.SetBinContent(4,1,cuts[3]['3SigRMS'])
Grid.SetBinContent(1,2,cuts[4]['3SigRMS'])
Grid.SetBinContent(2,2,cuts[5]['3SigRMS'])
Grid.SetBinContent(3,2,cuts[6]['3SigRMS'])
Grid.SetBinContent(4,2,cuts[7]['3SigRMS'])
Grid.SetBinContent(1,3,cuts[8]['3SigRMS'])
Grid.SetBinContent(2,3,cuts[9]['3SigRMS'])
Grid.SetBinContent(3,3,cuts[10]['3SigRMS'])
Grid.SetBinContent(4,3,cuts[11]['3SigRMS'])
Grid.SetStats(0)
Grid.Draw('text')



