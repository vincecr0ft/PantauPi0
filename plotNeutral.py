from ROOT import TFile,TCanvas,TH1F,TH2F,THStack,TLegend
from HistoClass import ListoHistos

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


cuts=[a,d]
#cuts=[a,b,c,d,e,f,g,h,i,j,k,l]
modes={'1P0N-1P0N':2,'1P0N-1P1N':4,'1P0N-1PXN':6,'1P0N-3P':8,
       '1P1N-1P0N':2,'1P1N-1P1N':4,'1P1N-1PXN':6,'1P1N-3P':8,
       '1PXN-1P0N':2,'1PXN-1P1N':4,'1PXN-1PXN':6,'1PXN-3P':8,
       '3P0N-1P':2,'3P0N-3P0N':6,'3P0N-3PXN':8,
       '3PXN-1P':2,'3PXN-3P0N':6,'3PXN-3PXN':8}

BDTs=['BDTnone']
#BDTs=['BDTnone','BDTloose','BDTmedium','BDTtight','ExoticVeto']
plots={}
for cut in cuts:
   for bdt in BDTs:
      cut['neutralSum '+bdt]=infile.Get('sumRes'+cut['name']+'_'+bdt)
      cut['neutralLead '+bdt]=infile.Get('leadRes'+cut['name']+'_'+bdt)
      cut['1Prong neutrals '+bdt]=infile.Get("1prong Neutral "+cut['name']+"_BDTnone")
      cut['3Prong neutrals '+bdt]=infile.Get("3prong Neutral "+cut['name']+"_BDTnone")

plots['NeutralSum']=TCanvas('Neutral Sum')
plots['NeutralSum'].cd()
cuts[0]['neutralSum BDTnone'].SetFillColor(2)
cuts[0]['neutralSum BDTnone'].SetFillStyle(3017)
cuts[0]['neutralSum BDTnone'].SetStats(0)
cuts[0]['neutralSum BDTnone'].Draw()
cuts[1]['neutralSum BDTnone'].SetFillColor(4)
cuts[1]['neutralSum BDTnone'].SetFillStyle(3017)
cuts[1]['neutralSum BDTnone'].SetStats(0)
cuts[1]['neutralSum BDTnone'].Draw("same")


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
cuts[0]['neutralLead BDTnone'].Draw()
cuts[1]['neutralLead BDTnone'].SetFillColor(4)
cuts[1]['neutralLead BDTnone'].SetFillStyle(3017)
cuts[1]['neutralLead BDTnone'].SetStats(0)
cuts[1]['neutralLead BDTnone'].Draw("same")

leg2=TLegend(0.58,0.42,0.86,0.88)
leg2.SetBorderSize(0)
leg2.SetFillColor(0)
leg2.SetTextFont(62)
leg2.SetTextSize(0.03)
leg2.AddEntry(cuts[0]['neutralLead BDTnone'],"Leading Accepted Neutral","lpf")
leg2.AddEntry(cuts[1]['neutralLead BDTnone'],"Lead of All possible neutrals","lpf")
leg2.Draw()

plots['1Prong neutrals']=TCanvas('1P1N Neutral resolution')
plots['1Prong neutrals'].cd()
cuts[0]['1Prong neutrals BDTnone'].SetFillColor(2)
cuts[0]['1Prong neutrals BDTnone'].SetFillStyle(3017)
cuts[0]['1Prong neutrals BDTnone'].SetStats(0)
cuts[0]['1Prong neutrals BDTnone'].Draw()
cuts[1]['1Prong neutrals BDTnone'].SetFillColor(4)
cuts[1]['1Prong neutrals BDTnone'].SetFillStyle(3017)
cuts[1]['1Prong neutrals BDTnone'].SetStats(0)
cuts[1]['1Prong neutrals BDTnone'].Draw("same")

leg3=TLegend(0.58,0.42,0.86,0.88)
leg3.SetBorderSize(0)
leg3.SetFillColor(0)
leg3.SetTextFont(62)
leg3.SetTextSize(0.03)
leg3.AddEntry(cuts[0]['1Prong neutrals BDTnone'],"1P1N Neutral resolution","lpf")
leg3.AddEntry(cuts[1]['1Prong neutrals BDTnone'],"without pi0 seleciton","lpf")
leg3.Draw()

plots['3Prong neutrals']=TCanvas('3PXN Neutral resolution')
plots['3Prong neutrals'].cd()
cuts[0]['3Prong neutrals BDTnone'].SetFillColor(2)
cuts[0]['3Prong neutrals BDTnone'].SetFillStyle(3017)
cuts[0]['3Prong neutrals BDTnone'].SetStats(0)
cuts[0]['3Prong neutrals BDTnone'].Draw()
cuts[1]['3Prong neutrals BDTnone'].SetFillColor(4)
cuts[1]['3Prong neutrals BDTnone'].SetFillStyle(3017)
cuts[1]['3Prong neutrals BDTnone'].SetStats(0)
cuts[1]['3Prong neutrals BDTnone'].Draw("same")

leg4=TLegend(0.58,0.42,0.86,0.88)
leg4.SetBorderSize(0)
leg4.SetFillColor(0)
leg4.SetTextFont(62)
leg4.SetTextSize(0.03)
leg4.AddEntry(cuts[0]['3Prong neutrals BDTnone'],"3PXN Neutral resolution","lpf")
leg4.AddEntry(cuts[1]['3Prong neutrals BDTnone'],"without pi0 seleciton","lpf")
leg4.Draw()


#  LocalWords:  neutralLead BDTnone
