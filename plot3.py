from ROOT import TFile,TCanvas,TH1F,TH2F,THStack,TLegend
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


cuts=[a,d,m]
#cuts=[a,b,c,d,e,f,g,h,i,j,k,l]
modes={'1P0N-1P0N':2,'1P0N-1P1N':4,'1P0N-1PXN':6,'1P0N-3P':8,
       '1P1N-1P0N':2,'1P1N-1P1N':4,'1P1N-1PXN':6,'1P1N-3P':8,
       '1PXN-1P0N':2,'1PXN-1P1N':4,'1PXN-1PXN':6,'1PXN-3P':8,
       '3P0N-1P':2,'3P0N-3P0N':6,'3P0N-3PXN':8,
       '3PXN-1P':2,'3PXN-3P0N':6,'3PXN-3PXN':8}

#BDTs=['BDTnone']
BDTs=['BDTnone','BDTloose','BDTmedium','BDTtight']
plots={}
inclusive={}
Pi0BDT=TH1F('Pi0BDT','Pi0BDT',4,0,4)
Pi0BDT=TH1F('Pi0Pt','Pi0Pt',4,0,4)
Grid=TH2F('grid','grid',4,0,4,4,0,4)
for cut in cuts:
   cut[cut['name']]=TH1F(cut['name'],cut['name'],40,-1.,1.)
   for bdt in BDTs:
      cut['neutralSum '+bdt]=infile.Get('sumRes'+cut['name']+'_'+bdt)
      cut['neutralLead '+bdt]=infile.Get('leadRes'+cut['name']+'_'+bdt)
#      cut['neutralSum '+bdt]=TH1F('neutralSum_'+bdt,'neutralSum_'+bdt,20,-1.,1.)
#      temp
#      cut['neutralSum '+bdt].Add(temp)
      cut[bdt]=TH1F(cut['name']+'_'+bdt,cut['name']+'_'+bdt,40,-1.,1.)

      for mode in modes:
         plots[mode]=infile.Get(mode+'_'+cut['name']+'_'+bdt)
         plots[mode].SetFillColor(modes[mode])
         plots[mode].SetFillStyle(3017)
         plots[mode].SetStats(0)
         cut[bdt].Add(plots[mode])
      inclusive['inc_3PXN '+cut['name']+'_'+bdt]=TH1F('inc_3PXN_'+cut['name']+'_'+bdt,'3PXN_'+cut['name']+'_'+bdt,40,-1.,1.)
      inclusive['inc_3PXN '+cut['name']+'_'+bdt].Add(plots['3PXN-3PXN'])
      inclusive['stack_3PXN '+cut['name']+'_'+bdt]=THStack('stack','3PXN '+cut['name']+'_'+bdt)
      inclusive['stack_3PXN '+cut['name']+'_'+bdt].Add(plots['3PXN-3PXN'])



   plots[bdt]=TCanvas(cut['name']+' inclusive plots')
   plots[bdt].cd()
   cut['BDTnone'].SetFillColor(2)
   cut['BDTnone'].SetFillStyle(3017)
   cut['BDTloose'].SetLineColor(4)
   cut['BDTmedium'].SetLineColor(6)
   cut['BDTtight'].SetLineColor(2)

   cut['BDTnone'].Draw()
   cut['BDTloose'].Draw('same')
   cut['BDTmedium'].Draw('same')
   cut['BDTtight'].Draw('same')



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


plots['3PXN BDTnone']=TCanvas('3PXN_BDTnone')
plots['3PXN BDTnone'].cd()

inclusive['inc_3PXN Normal-Normal_BDTnone'].SetStats(0)
inclusive['inc_3PXN Normal-Normal_BDTnone'].SetFillColor(4)
inclusive['inc_3PXN Normal-Normal_BDTnone'].SetFillStyle(3017)
inclusive['inc_3PXN Normal-Normal_BDTnone'].Draw()
#inclusive['stack_3PXN Normal-Normal_BDTnone'].Draw("same")
inclusive['inc_3PXN Public-Normal_BDTnone'].SetStats(0)
inclusive['inc_3PXN Public-Normal_BDTnone'].SetFillColor(2)
inclusive['inc_3PXN Public-Normal_BDTnone'].SetFillStyle(3017)
inclusive['inc_3PXN Public-Normal_BDTnone'].Draw("same")
#inclusive['stack_3PXN Public-Normal_BDTnone'].Draw("same")





plots['inc']=TCanvas('inclusive plots')
plots['inc'].cd()
cuts[2]['BDTnone'].SetFillColor(2)
cuts[2]['BDTnone'].SetFillStyle(3017)
cuts[2]['BDTnone'].SetStats(0)
cuts[0]['BDTnone'].SetFillColor(4)
cuts[0]['BDTnone'].SetFillStyle(3017)
cuts[0]['BDTnone'].SetStats(0)
print cuts[0]['BDTnone'].GetRMS(),cuts[1]['BDTnone'].GetRMS()
cuts[0]['BDTnone'].Draw()
cuts[2]['BDTnone'].Draw('same')

leg=TLegend(0.58,0.42,0.86,0.88)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetTextFont(62)
leg.SetTextSize(0.03)
RMS0=cuts[0]['BDTnone'].GetRMS()-cuts[0]['BDTnone'].GetRMS()%0.001
RMS1=cuts[2]['BDTnone'].GetRMS()-cuts[2]['BDTnone'].GetRMS()%0.001
RMS30=cuts[0]['3SigRMS']-cuts[0]['3SigRMS']%0.001
RMS31=cuts[2]['3SigRMS']-cuts[2]['3SigRMS']%0.001

leg.AddEntry(cuts[0]['BDTnone'],cuts[0]['name']+' '+str(RMS0),"lpf")
leg.AddEntry(cuts[0]['BDTnone'],'with 3Sig RMS of '+str(RMS30),"lpf")
leg.AddEntry(cuts[2]['BDTnone'],cuts[2]['name']+' '+str(RMS1),"lpf")
leg.AddEntry(cuts[2]['BDTnone'],'with 3Sig RMS of '+str(RMS31),"lpf")
leg.Draw()


plots['NeutralSum']=TCanvas('Neutral Sum')
plots['NeutralSum'].cd()
cuts[0]['neutralSum BDTnone'].SetFillColor(2)
cuts[0]['neutralSum BDTnone'].SetFillStyle(3017)
cuts[0]['neutralSum BDTnone'].SetStats(0)
cuts[0]['neutralSum BDTnone'].DrawNormalized()
cuts[1]['neutralSum BDTnone'].SetFillColor(4)
cuts[1]['neutralSum BDTnone'].SetFillStyle(3017)
cuts[1]['neutralSum BDTnone'].SetStats(0)
cuts[1]['neutralSum BDTnone'].DrawNormalized("same")


leg1=TLegend(0.58,0.42,0.86,0.88)
leg1.SetBorderSize(0)
leg1.SetFillColor(0)
leg1.SetTextFont(62)
leg1.SetTextSize(0.03)
leg1.AddEntry(cuts[0]['neutralSum BDTnone'],"Sum of Accepted Neutrals","lpf")
leg1.AddEntry(cuts[1]['neutralSum BDTnone'],"Sum of All neutrals","lpf")
leg1.Draw()


plots['NeutralLead']=TCanvas('Neutral Lead')
plots['NeutralLead'].cd()
cuts[0]['neutralLead BDTnone'].SetFillColor(2)
cuts[0]['neutralLead BDTnone'].SetFillStyle(3017)
cuts[0]['neutralLead BDTnone'].SetStats(0)
cuts[0]['neutralLead BDTnone'].DrawNormalized()
cuts[1]['neutralLead BDTnone'].SetFillColor(4)
cuts[1]['neutralLead BDTnone'].SetFillStyle(3017)
cuts[1]['neutralLead BDTnone'].SetStats(0)
cuts[1]['neutralLead BDTnone'].DrawNormalized("same")

leg2=TLegend(0.58,0.42,0.86,0.88)
leg2.SetBorderSize(0)
leg2.SetFillColor(0)
leg2.SetTextFont(62)
leg2.SetTextSize(0.03)
leg2.AddEntry(cuts[0]['neutralLead BDTnone'],"Leading Accepted Neutral","lpf")
leg2.AddEntry(cuts[1]['neutralLead BDTnone'],"Lead of All possible neutrals","lpf")
leg2.Draw()
