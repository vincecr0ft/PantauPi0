from ROOT import TFile,TCanvas,TH1F,TH2F,THStack,TLegend
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
c={"name":"ExtraLoose-Normal","BDTvalue":-1.0,"Cutvalue":0.0}

cuts=[a]

modes={'1P0N-1P0N':2,'1P0N-1P1N':4,'1P0N-1PXN':6,'1P0N-3P':8,
       '1P1N-1P0N':2,'1P1N-1P1N':4,'1P1N-1PXN':6,'1P1N-3P':8,
       '1PXN-1P0N':2,'1PXN-1P1N':4,'1PXN-1PXN':6,'1PXN-3P':8,
       '3P0N-1P':2,'3P0N-3P0N':6,'3P0N-3PXN':8,
       '3PXN-1P':2,'3PXN-3P0N':6,'3PXN-3PXN':8}

BDTs=['BDTnone','BDTloose','BDTmedium','BDTtight','ExoticVeto']
plots={}
for cut in cuts:
   cut[cut['name']]=TH1F(cut['name'],cut['name'],101,-1.01,1.01)
   for bdt in BDTs:
      cut[bdt]=TH1F(cut['name']+'_'+bdt,cut['name']+'_'+bdt,101,-1.01,1.01)
      for mode in modes:
         plots[mode]=infile.Get(mode+'_'+cut['name']+'_'+bdt)
 #        plots[mode].SetFillColor(modes[mode])
 #        plots[mode].SetFillStyle(3017)
         plots[mode].SetStats(0)
         cut[bdt].Add(plots[mode])

   c1=TCanvas(cut['name']+' inclusive plots')
   c1.cd()
#   c1.SetLogy()
#   cut['BDTnone'].SetFillColor(2)
#   cut['BDTnone'].SetFillStyle(3017)
   cut['BDTloose'].SetLineColor(4)
   cut['BDTmedium'].SetLineColor(6)
   cut['BDTtight'].SetLineColor(2)
   cut['ExoticVeto'].SetLineColor(8)

   cut['BDTnone'].SetStats(0)

   cut['BDTnone'].Draw()
   cut['BDTloose'].Draw('same')
   cut['BDTmedium'].Draw('same')
   cut['BDTtight'].Draw('same')
   cut['ExoticVeto'].Draw('same')

   noneRMS=get3Sig(cut['BDTnone'])
   looseRMS=get3Sig(cut['BDTloose'])
   mediumRMS=get3Sig(cut['BDTmedium'])
   tightRMS=get3Sig(cut['BDTtight'])
   exoticRMS=get3Sig(cut['ExoticVeto'])

   leg=TLegend(0.58,0.42,0.86,0.88)
   leg.SetBorderSize(0)
   leg.SetFillColor(0)
   leg.SetTextFont(62)
   leg.SetTextSize(0.03)
   RMSnone=noneRMS-noneRMS%0.001
   RMSloose=looseRMS-looseRMS%0.001
   RMSmedium=mediumRMS-mediumRMS%0.001
   RMStight=tightRMS-tightRMS%0.001
   RMSexotic=exoticRMS-exoticRMS%0.001
   

   leg.AddEntry(cut['BDTnone'],'no BDT RMS:'+str(RMSnone),"lpf")
   leg.AddEntry(cut['BDTloose'],'loose BDT RMS:'+str(RMSloose),"lpf")
   leg.AddEntry(cut['BDTmedium'],'medium BDT RMS:'+str(RMSmedium),"lpf")
   leg.AddEntry(cut['BDTtight'],'tight BDT RMS:'+str(RMStight),"lpf")
   leg.AddEntry(cut['ExoticVeto'],'Exotic Veto RMS:'+str(RMSexotic),"lpf")
   leg.Draw()
