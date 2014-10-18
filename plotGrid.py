from ROOT import TFile,TCanvas,TH1F,TH2F,THStack
from testClass import ListoHistos

infile=TFile('resolutionHistos.root')

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

#arranged in tight->loose blocks of ptthreshold
cuts=[y,u,v,w,x,e,a,b,c,d,j,f,g,h,i,o,k,l,m,n,t,p,q,r,s]



modes={'1P0N-1P0N':2,'1P0N-1P1N':4,'1P0N-1PXN':6,'1P0N-3P':8,
       '1P1N-1P0N':2,'1P1N-1P1N':4,'1P1N-1PXN':6,'1P1N-3P':8,
       '1PXN-1P0N':2,'1PXN-1P1N':4,'1PXN-1PXN':6,'1PXN-3P':8,
       '3P0N-1P':2,'3P0N-3P0N':6,'3P0N-3PXN':8,
       '3PXN-1P':2,'3PXN-3P0N':6,'3PXN-3PXN':8}
BDTs=['BDTnone','BDTloose','BDTmedium','BDTtight']
plots={}
Grid=TH2F('grid','grid',5,0,5,5,0,5)
for cut in cuts:
   cut[cut['name']]=TH1F(cut['name'],cut['name'],40,-1.,1.)
   for bdt in BDTs:
      cut[bdt]=TH1F(cut['name']+'_'+bdt,cut['name']+'_'+bdt,40,-1.,1.)
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

Grid.GetXaxis().SetBinLabel(1,'BDT '+str(cuts[0]['BDTvalue']))
Grid.GetXaxis().SetBinLabel(2,'Normal')
Grid.GetXaxis().SetBinLabel(3,'BDT '+str(cuts[2]['BDTvalue']))
Grid.GetXaxis().SetBinLabel(4,'BDT '+str(cuts[3]['BDTvalue']))
Grid.GetXaxis().SetBinLabel(5,'No BDT requirement')

Grid.GetYaxis().SetBinLabel(1,'Pt -'+str(cuts[0]['Cutvalue'])+'MeV')
Grid.GetYaxis().SetBinLabel(2,'Normal')
Grid.GetYaxis().SetBinLabel(3,'Pt -'+str(cuts[10]['Cutvalue'])+'MeV')
Grid.GetYaxis().SetBinLabel(4,'Pt -'+str(cuts[15]['Cutvalue'])+'MeV')
Grid.GetYaxis().SetBinLabel(5,'Pt -'+str(cuts[20]['Cutvalue'])+'MeV')


Grid.SetBinContent(1,1,cuts[0]['3SigRMS'])#tight-tight
Grid.SetBinContent(2,1,cuts[1]['3SigRMS'])
Grid.SetBinContent(3,1,cuts[2]['3SigRMS'])
Grid.SetBinContent(4,1,cuts[3]['3SigRMS'])
Grid.SetBinContent(5,1,cuts[4]['3SigRMS'])#Public-tight-

Grid.SetBinContent(1,2,cuts[5]['3SigRMS'])#tight-Normal
Grid.SetBinContent(2,2,cuts[6]['3SigRMS'])
Grid.SetBinContent(3,2,cuts[7]['3SigRMS'])
Grid.SetBinContent(4,2,cuts[8]['3SigRMS'])
Grid.SetBinContent(5,2,cuts[9]['3SigRMS'])#public-normal

Grid.SetBinContent(1,3,cuts[10]['3SigRMS'])#tight-loose
Grid.SetBinContent(2,3,cuts[11]['3SigRMS'])
Grid.SetBinContent(3,3,cuts[12]['3SigRMS'])
Grid.SetBinContent(4,3,cuts[13]['3SigRMS'])
Grid.SetBinContent(5,3,cuts[14]['3SigRMS'])

Grid.SetBinContent(1,4,cuts[15]['3SigRMS'])#tight-looser
Grid.SetBinContent(2,4,cuts[16]['3SigRMS'])
Grid.SetBinContent(3,4,cuts[17]['3SigRMS'])
Grid.SetBinContent(4,4,cuts[18]['3SigRMS'])
Grid.SetBinContent(5,4,cuts[19]['3SigRMS'])

Grid.SetBinContent(1,5,cuts[20]['3SigRMS'])#tight-ExtraLoose
Grid.SetBinContent(2,5,cuts[21]['3SigRMS'])
Grid.SetBinContent(3,5,cuts[22]['3SigRMS'])
Grid.SetBinContent(4,5,cuts[23]['3SigRMS'])
Grid.SetBinContent(5,5,cuts[24]['3SigRMS'])



Grid.SetStats(0)
Grid.Draw('text,box,colz')



