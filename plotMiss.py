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

BDTs=['BDTnone']
plots={}
for cut in cuts:
   cut[cut['name']]=TH1F(cut['name'],cut['name'],101,-1.01,1.01)
   for bdt in BDTs:
      plots['1P0N']=infile.Get('Miss1P0N'+cut['name']+'_'+bdt)
      plots['1P1N']=infile.Get('Miss1P1N'+cut['name']+'_'+bdt)
      plots['1PXN']=infile.Get('Miss1PXN'+cut['name']+'_'+bdt)
      plots['3P0N']=infile.Get('Miss3P0N'+cut['name']+'_'+bdt)
      plots['3PXN']=infile.Get('Miss3PXN'+cut['name']+'_'+bdt)
      plots['1P0N'].SetStats(0)
      plots['1P1N'].SetStats(0)
      plots['1PXN'].SetStats(0)
      plots['3P0N'].SetStats(0)
      plots['3PXN'].SetStats(0)

      cut[cut['name']].Add(plots['1P0N'])
      cut[cut['name']].Add(plots['1P1N'])
      cut[cut['name']].Add(plots['1PXN'])
      cut[cut['name']].Add(plots['3P0N'])
      cut[cut['name']].Add(plots['3PXN'])


   c1=TCanvas(cut['name']+' inclusive plots')
   c1.cd()
   plots['1P0N'].SetLineColor(2)
   plots['1P1N'].SetLineColor(4)
   plots['1PXN'].SetLineColor(6)
   plots['3P0N'].SetLineColor(8)
   plots['3PXN'].SetLineColor(12)
   
   stack=THStack('stack','True Events Classified differently in CellBased and PanTau')
   stack.Add(plots['1P0N'])
   stack.Add(plots['1P1N'])
   stack.Add(plots['1PXN'])
   stack.Add(plots['3P0N'])
   stack.Add(plots['3PXN'])
   stack.Draw()

   RMSt=get3Sig(cuts[0]['Normal-Normal'])

   leg=TLegend(0.58,0.42,0.86,0.88)
   leg.SetBorderSize(0)
   leg.SetFillColor(0)
   leg.SetTextFont(62)
   leg.SetTextSize(0.03)
   RMS= RMSt-RMSt%0.001   

   leg.AddEntry(plots['1P0N'],'true1P0N:',"lpf")
   leg.AddEntry(plots['1P1N'],'true1P1N:',"lpf")
   leg.AddEntry(plots['1PXN'],'true1PXN:',"lpf")
   leg.AddEntry(plots['3P0N'],'true3P0N:',"lpf")
   leg.AddEntry(plots['3PXN'],'true3PXN:',"lpf")
   leg.AddEntry(cuts[0]['Normal-Normal'],'RMS of total:'+str(RMS),"lpf")
   leg.Draw()
