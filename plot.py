
import ROOT

f=ROOT.TFile("resolutionHistos.root")


h_cellN_a=f.Get("h_cellneutrals_normal")
h_cellN_a.SetFillColor(2)
h_cellN_a.SetFillStyle(3005)
h_cellN_b=f.Get("h_cellneutrals_loosened")
h_cellN_b.SetFillColor(7)
#h_cellN_b.SetFillStyle(3005)
h_cellN_c=f.Get("h_cellneutrals_tightened")
h_cellN_c.SetStats(0)
h_cellN_c.SetFillColor(28)
h_cellN_c.SetFillStyle(3017)
h_trueN=f.Get("h_trueneutrals_normal")
h_trueN.SetFillColor(9)
#h_trueN.SetFillStyle(3005)

h_cellP=f.Get("h_cellprong_normal")
h_cellP.SetFillColor(2)
h_cellP.SetFillStyle(3004)
h_trueP=f.Get("h_trueprong_normal")
h_trueP.SetStats(0)
h_trueP.SetFillColor(9)
h_trueP.SetFillStyle(3005)


#normal
h_reco1P1N_normal=f.Get("h_reco1P1N_normal")
h_reco1P1N_normal.SetFillColor(9)
h_reco1P1N_normal.SetFillStyle(3004)
h_reco1P1N_true1P0N_normal=f.Get("h_reco1P1N_true1P0N_normal")
h_reco1P1N_true1P0N_normal.SetFillColor(2)
h_reco1P1N_true1P0N_normal.SetFillStyle(3005)
h_reco1P1N_true1PXN_normal=f.Get("h_reco1P1N_true1PXN_normal")
h_reco1P1N_true1PXN_normal.SetFillColor(8)
h_reco1P1N_true1PXN_normal.SetFillStyle(3005)
h_reco1P1N_true3P_normal=f.Get("h_reco1P1N_true3P_normal")
h_reco1P1N_true3P_normal.SetFillColor(28)
h_reco1P1N_true3P_normal.SetFillStyle(3005)


h_3p_normal=f.Get("h_3p_normal")
h_3p_normal.SetFillColor(2)
h_3p_normal.SetFillStyle(3004)
h_3p3p_normal=f.Get("h_3p3p_normal")
h_3p3p_normal.SetFillColor(9)
h_3p3p_normal.SetFillStyle(3005)

#loose
h_reco1P1N_loosened=f.Get("h_reco1P1N_loosened")
h_reco1P1N_loosened.SetFillColor(9)
h_reco1P1N_loosened.SetFillStyle(3004)
h_reco1P1N_true1P0N_loosened=f.Get("h_reco1P1N_true1P0N_loosened")
h_reco1P1N_true1P0N_loosened.SetFillColor(2)
h_reco1P1N_true1P0N_loosened.SetFillStyle(3005)
h_reco1P1N_true1PXN_loosened=f.Get("h_reco1P1N_true1PXN_loosened")
h_reco1P1N_true1PXN_loosened.SetFillColor(8)
h_reco1P1N_true1PXN_loosened.SetFillStyle(3005)
h_reco1P1N_true3P_loosened=f.Get("h_reco1P1N_true3P_loosened")
h_reco1P1N_true3P_loosened.SetFillColor(28)
h_reco1P1N_true3P_loosened.SetFillStyle(3005)


h_3p_loosened=f.Get("h_3p_loosened")
h_3p_loosened.SetFillColor(2)
h_3p_loosened.SetFillStyle(3004)
h_3p3p_loosened=f.Get("h_3p3p_loosened")
h_3p3p_loosened.SetFillColor(9)
h_3p3p_loosened.SetFillStyle(3005)


#tight
h_reco1P1N_tightened=f.Get("h_reco1P1N_tightened")
h_reco1P1N_tightened.SetFillColor(9)
h_reco1P1N_tightened.SetFillStyle(3004)
h_reco1P1N_true1P0N_tightened=f.Get("h_reco1P1N_true1P0N_tightened")
h_reco1P1N_true1P0N_tightened.SetFillColor(2)
h_reco1P1N_true1P0N_tightened.SetFillStyle(3005)
h_reco1P1N_true1PXN_tightened=f.Get("h_reco1P1N_true1PXN_tightened")
h_reco1P1N_true1PXN_tightened.SetFillColor(8)
h_reco1P1N_true1PXN_tightened.SetFillStyle(3005)
h_reco1P1N_true3P_tightened=f.Get("h_reco1P1N_true3P_tightened")
h_reco1P1N_true3P_tightened.SetFillColor(28)
h_reco1P1N_true3P_tightened.SetFillStyle(3005)


h_3p_tightened=f.Get("h_3p_tightened")
h_3p_tightened.SetFillColor(2)
h_3p_tightened.SetFillStyle(3004)
h_3p3p_tightened=f.Get("h_3p3p_tightened")
h_3p3p_tightened.SetFillColor(9)
h_3p3p_tightened.SetFillStyle(3005)

#plot

c1=ROOT.TCanvas("neutrals")
h_cellN_c.Draw()
h_trueN.Draw("same")
h_cellN_b.Draw("same")
h_cellN_a.Draw("same")
h_cellN_c.Draw("same")



c2=ROOT.TCanvas("prong")
h_trueP.Draw()
h_cellP.Draw("same")

c3=ROOT.TCanvas("1 prong")
normal=ROOT.THStack("normal","normal cell based")
normal.Add(h_reco1P1N_true1P0N_normal)
normal.Add(h_reco1P1N_true1PXN_normal)
normal.Add(h_reco1P1N_true3P_normal)
normal.Add(h_reco1P1N_normal)
normal.Draw()
c3leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c3leg.SetBorderSize(0)
c3leg.SetFillColor(0)
c3leg.SetTextFont(62)
c3leg.SetTextSize(0.050)
RMS1P1N=h_reco1P1N_normal.GetRMS()-h_reco1P1N_normal.GetRMS()%0.001
RMS1P0N=h_reco1P1N_true1P0N_normal.GetRMS()-h_reco1P1N_true1P0N_normal.GetRMS()%0.001
RMS1PXN=h_reco1P1N_true1PXN_normal.GetRMS()-h_reco1P1N_true1PXN_normal.GetRMS()%0.001
RMS3P=h_reco1P1N_true3P_normal.GetRMS()-h_reco1P1N_true3P_normal.GetRMS()%0.001
c3leg.AddEntry("h_reco1P1N_normal","1P1N "+str(RMS1P1N),"lpf")
c3leg.AddEntry("h_reco1P1N_true1P0N_normal","1PON "+str(RMS1P0N),"lpf")
c3leg.AddEntry("h_reco1P1N_true1PXN_normal","1PXN "+str(RMS1PXN),"lpf")
c3leg.AddEntry("h_reco1P1N_true3P_normal","3prong "+str(RMS3P),"lpf")
c3leg.Draw()

c4=ROOT.TCanvas("1 prong b")
loosened=ROOT.THStack("loosened","loosened cell based")

loosened.Add(h_reco1P1N_true1P0N_loosened)
loosened.Add(h_reco1P1N_true1PXN_loosened)
loosened.Add(h_reco1P1N_true3P_loosened)
loosened.Add(h_reco1P1N_loosened)
loosened.Draw()
c4leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c4leg.SetBorderSize(0)
c4leg.SetFillColor(0)
c4leg.SetTextFont(62)
c4leg.SetTextSize(0.050)
RMS1P1N=h_reco1P1N_loosened.GetRMS()-h_reco1P1N_loosened.GetRMS()%0.001
RMS1P0N=h_reco1P1N_true1P0N_loosened.GetRMS()-h_reco1P1N_true1P0N_loosened.GetRMS()%0.001
RMS1PXN=h_reco1P1N_true1PXN_loosened.GetRMS()-h_reco1P1N_true1PXN_loosened.GetRMS()%0.001
RMS3P=h_reco1P1N_true3P_loosened.GetRMS()-h_reco1P1N_true3P_loosened.GetRMS()%0.001
c4leg.AddEntry("h_reco1P1N_loosened","1P1N "+str(RMS1P1N),"lpf")
c4leg.AddEntry("h_reco1P1N_true1P0N_loosened","1PON "+str(RMS1P0N),"lpf")
c4leg.AddEntry("h_reco1P1N_true1PXN_loosened","1PXN "+str(RMS1PXN),"lpf")
c4leg.AddEntry("h_reco1P1N_true3P_loosened","3prong "+str(RMS3P),"lpf")
c4leg.Draw()


c5=ROOT.TCanvas("1 prong c")
tightened=ROOT.THStack("tightened","tightened cell based")

tightened.Add(h_reco1P1N_true1P0N_tightened)
tightened.Add(h_reco1P1N_true1PXN_tightened)
tightened.Add(h_reco1P1N_true3P_tightened)
tightened.Add(h_reco1P1N_tightened)
tightened.Draw()

c5leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c5leg.SetBorderSize(0)
c5leg.SetFillColor(0)
c5leg.SetTextFont(62)
c5leg.SetTextSize(0.050)
RMS1P1N=h_reco1P1N_tightened.GetRMS()-h_reco1P1N_tightened.GetRMS()%0.001
RMS1P0N=h_reco1P1N_true1P0N_tightened.GetRMS()-h_reco1P1N_true1P0N_tightened.GetRMS()%0.001
RMS1PXN=h_reco1P1N_true1PXN_tightened.GetRMS()-h_reco1P1N_true1PXN_tightened.GetRMS()%0.001
RMS3P=h_reco1P1N_true3P_tightened.GetRMS()-h_reco1P1N_true3P_tightened.GetRMS()%0.001
c5leg.AddEntry("h_reco1P1N_tightened","1P1N "+str(RMS1P1N),"lpf")
c5leg.AddEntry("h_reco1P1N_true1P0N_tightened","1PON "+str(RMS1P0N),"lpf")
c5leg.AddEntry("h_reco1P1N_true1PXN_tightened","1PXN "+str(RMS1PXN),"lpf")
c5leg.AddEntry("h_reco1P1N_true3P_tightened","3prong "+str(RMS3P),"lpf")
c5leg.Draw()

