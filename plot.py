import ROOT

f=ROOT.TFile("resolutionHistos.root")


h_cellN=f.Get("h_cellneutrals")
h_cellN.SetFillColor(2)
h_cellN.SetFillStyle(3004)
h_trueN=f.Get("h_trueneutrals")
h_trueN.SetFillColor(9)
h_trueN.SetFillStyle(3005)

h_cellP=f.Get("h_cellprong")
h_cellP.SetFillColor(2)
h_cellP.SetFillStyle(3004)
h_trueP=f.Get("h_trueprong")
h_trueP.SetFillColor(9)
h_trueP.SetFillStyle(3005)

h_1p=f.Get("h_1p")
h_1p.SetFillColor(2)
h_1p.SetFillStyle(3004)
h_1p1p=f.Get("h_1p1p")
h_1p1p.SetFillColor(9)
h_1p1p.SetFillStyle(3005)

h_3p=f.Get("h_3p")
h_3p.SetFillColor(2)
h_3p.SetFillStyle(3004)
h_3p3p=f.Get("h_3p3p")
h_3p3p.SetFillColor(9)
h_3p3p.SetFillStyle(3005)


c1=ROOT.TCanvas("neutrals")
h_cellN.Draw()
h_trueN.Draw("same")

c2=ROOT.TCanvas("prong")
h_trueP.Draw()
h_cellP.Draw("same")

c3=ROOT.TCanvas("1 prong")
h_1p.Draw()
h_1p1p.Draw("same")

c4=ROOT.TCanvas("3 prong")
h_3p.Draw()
h_3p3p.Draw("same")
