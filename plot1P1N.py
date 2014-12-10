from ROOT import TFile,TCanvas,TH1F,TH2F,THStack,TLegend,TF1
from HistoClass import ListoHistos


def get3Sig(hist):
   sig0=hist.GetRMS()
   temp=hist.Clone()
   lower=temp.GetMean()-3*sig0
   upper=temp.GetMean()+3*sig0
   for bin in range(1,temp.GetNbinsX()+1):
      thisbin=temp.GetBinCenter(bin)
      if thisbin<lower or thisbin>upper:
         temp.SetBinContent(bin,0)
   return temp.GetRMS()
   


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


cuts=[a]
#cuts=[a,b,c,d,e,f,g,h,i,j,k,l]
modes={'1P0N-1P0N':2,'1P0N-1P1N':4,'1P0N-1PXN':6,'1P0N-3P':8,
       '1P1N-1P0N':2,'1P1N-1P1N':4,'1P1N-1PXN':6,'1P1N-3P':8,
       '1PXN-1P0N':2,'1PXN-1P1N':4,'1PXN-1PXN':6,'1PXN-3P':8,
       '3P0N-1P':2,'3P0N-3P0N':6,'3P0N-3PXN':8,
       '3PXN-1P':2,'3PXN-3P0N':6,'3PXN-3PXN':8}

BDTs=['BDTnone']
#BDTs=['BDTnone','BDTloose','BDTmedium','BDTtight','ExoticVeto']
plots={}
inclusive={}
for cut in cuts:
   cut[cut['name']]=TH1F(cut['name'],cut['name'],101,-1.01,1.01)
   for bdt in BDTs:
      cut[bdt]=TH1F(cut['name']+'_'+bdt,cut['name']+'_'+bdt,101,-1.01,1.01)
      for mode in modes:
         plots[mode]=infile.Get(mode+'_'+cut['name']+'_'+bdt)
         plots[mode].SetStats(0)
         cut[bdt].Add(plots[mode])
      inclusive['inc_1P1N '+cut['name']+'_'+bdt]=TH1F('inc_1P1N_'+cut['name']+'_'+bdt,'1P1N_'+cut['name']+'_'+bdt,101,-1.01,1.01)
      inclusive['inc_1P1N '+cut['name']+'_'+bdt].Add(plots['1P1N-1P1N'])
      inclusive['stack_1P1N '+cut['name']+'_'+bdt]=THStack('stack','1P1N '+cut['name']+'_'+bdt)
      inclusive['stack_1P1N '+cut['name']+'_'+bdt].Add(plots['1P1N-1P1N'])

plots['1P1N BDTnone']=TCanvas('1P1N_BDTnone')
plots['1P1N BDTnone'].cd()

inclusive['inc_1P1N Normal-Normal_BDTnone'].SetStats(0)
inclusive['inc_1P1N Normal-Normal_BDTnone'].SetLineColor(4)
inclusive['inc_1P1N Normal-Normal_BDTnone'].Draw()

fit_x = TF1("fit_x", "gaus", -2.0, 2.0)
fit_x.SetLineColor(8)
fit_x.SetLineWidth(3)
inclusive['inc_1P1N Normal-Normal_BDTnone'].Fit("fit_x")

normalRMS=get3Sig(inclusive['inc_1P1N Normal-Normal_BDTnone'])
#publicRMS=get3Sig(inclusive['inc_1P1N Public-Normal_BDTnone'])
fitChi=fit_x.GetChisquare()

leg1P1N=TLegend(0.58,0.42,0.86,0.88)
leg1P1N.SetBorderSize(0)
leg1P1N.SetFillColor(0)
leg1P1N.SetTextFont(62)
leg1P1N.SetTextSize(0.03)
RMSnormal=normalRMS-normalRMS%0.001
Chi=fitChi-fitChi%0.001

leg1P1N.AddEntry(inclusive['inc_1P1N Normal-Normal_BDTnone'],'1P1N-1P1N with RMS: '+str(RMSnormal),"lpf")
leg1P1N.AddEntry(fit_x,'Chi Squared of Fit '+str(Chi),"lpf")

leg1P1N.Draw()
