import ROOT


f=ROOT.TFile("resolutionHistos.root")

h_dR_normal=f.Get("h_dR_normal")

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

###################   1P0N   ###################

#normal
h_reco1P0N_true1P0N_normal=f.Get("h_reco1P0N_true1P0N_normal")
h_reco1P0N_true1P0N_normal.SetFillColor(9)
h_reco1P0N_true1P0N_normal.SetFillStyle(3004)
h_reco1P0N_true1P1N_normal=f.Get("h_reco1P0N_true1P1N_normal")
h_reco1P0N_true1P1N_normal.SetFillColor(2)
h_reco1P0N_true1P1N_normal.SetFillStyle(3005)
h_reco1P0N_true1PXN_normal=f.Get("h_reco1P0N_true1PXN_normal")
h_reco1P0N_true1PXN_normal.SetFillColor(8)
h_reco1P0N_true1PXN_normal.SetFillStyle(3005)
h_reco1P0N_true3P_normal=f.Get("h_reco1P0N_true3P_normal")
h_reco1P0N_true3P_normal.SetFillColor(28)
h_reco1P0N_true3P_normal.SetFillStyle(3005)

#loose
h_reco1P0N_true1P0N_loosened=f.Get("h_reco1P0N_true1P0N_loosened")
h_reco1P0N_true1P0N_loosened.SetFillColor(9)
h_reco1P0N_true1P0N_loosened.SetFillStyle(3004)
h_reco1P0N_true1P1N_loosened=f.Get("h_reco1P0N_true1P1N_loosened")
h_reco1P0N_true1P1N_loosened.SetFillColor(2)
h_reco1P0N_true1P1N_loosened.SetFillStyle(3005)
h_reco1P0N_true1PXN_loosened=f.Get("h_reco1P0N_true1PXN_loosened")
h_reco1P0N_true1PXN_loosened.SetFillColor(8)
h_reco1P0N_true1PXN_loosened.SetFillStyle(3005)
h_reco1P0N_true3P_loosened=f.Get("h_reco1P0N_true3P_loosened")
h_reco1P0N_true3P_loosened.SetFillColor(28)
h_reco1P0N_true3P_loosened.SetFillStyle(3005)

#tight
h_reco1P0N_true1P0N_tightened=f.Get("h_reco1P0N_true1P0N_tightened")
h_reco1P0N_true1P0N_tightened.SetFillColor(9)
h_reco1P0N_true1P0N_tightened.SetFillStyle(3004)
h_reco1P0N_true1P1N_tightened=f.Get("h_reco1P0N_true1P1N_tightened")
h_reco1P0N_true1P1N_tightened.SetFillColor(2)
h_reco1P0N_true1P1N_tightened.SetFillStyle(3005)
h_reco1P0N_true1PXN_tightened=f.Get("h_reco1P0N_true1PXN_tightened")
h_reco1P0N_true1PXN_tightened.SetFillColor(8)
h_reco1P0N_true1PXN_tightened.SetFillStyle(3005)
h_reco1P0N_true3P_tightened=f.Get("h_reco1P0N_true3P_tightened")
h_reco1P0N_true3P_tightened.SetFillColor(28)
h_reco1P0N_true3P_tightened.SetFillStyle(3005)

#public
h_reco1P0N_true1P0N_public=f.Get("h_reco1P0N_true1P0N_public")
h_reco1P0N_true1P0N_public.SetFillColor(9)
h_reco1P0N_true1P0N_public.SetFillStyle(3004)
h_reco1P0N_true1P1N_public=f.Get("h_reco1P0N_true1P1N_public")
h_reco1P0N_true1P1N_public.SetFillColor(2)
h_reco1P0N_true1P1N_public.SetFillStyle(3005)
h_reco1P0N_true1PXN_public=f.Get("h_reco1P0N_true1PXN_public")
h_reco1P0N_true1PXN_public.SetFillColor(8)
h_reco1P0N_true1PXN_public.SetFillStyle(3005)
h_reco1P0N_true3P_public=f.Get("h_reco1P0N_true3P_public")
h_reco1P0N_true3P_public.SetFillColor(28)
h_reco1P0N_true3P_public.SetFillStyle(3005)
 
h_1P0N_tightened=ROOT.TH1F("h_1P0N_tightened","reco 1P0N taus - tightened",40,-2,2)
h_1P0N_tightened.SetStats(0)
h_1P0N_normal=ROOT.TH1F("h_1P0N_normal","reco 1P0N taus - normal",40,-2,2)
h_1P0N_normal.SetStats(0)
h_1P0N_loosened=ROOT.TH1F("h_1P0N_loosened","reco 1P0N taus - loosened",40,-2,2)
h_1P0N_loosened.SetStats(0)
h_1P0N_public=ROOT.TH1F("h_1P0N_public","reco 1P0N taus - public",40,-2,2)
h_1P0N_public.SetStats(0)


###################   1P1N   ###################

#normal
h_reco1P1N_true1P0N_normal=f.Get("h_reco1P1N_true1P0N_normal")
h_reco1P1N_true1P0N_normal.SetFillColor(9)
h_reco1P1N_true1P0N_normal.SetFillStyle(3004)
h_reco1P1N_true1P1N_normal=f.Get("h_reco1P1N_true1P1N_normal")
h_reco1P1N_true1P1N_normal.SetFillColor(2)
h_reco1P1N_true1P1N_normal.SetFillStyle(3005)
h_reco1P1N_true1PXN_normal=f.Get("h_reco1P1N_true1PXN_normal")
h_reco1P1N_true1PXN_normal.SetFillColor(8)
h_reco1P1N_true1PXN_normal.SetFillStyle(3005)
h_reco1P1N_true3P_normal=f.Get("h_reco1P1N_true3P_normal")
h_reco1P1N_true3P_normal.SetFillColor(28)
h_reco1P1N_true3P_normal.SetFillStyle(3005)

#loose
h_reco1P1N_true1P0N_loosened=f.Get("h_reco1P1N_true1P0N_loosened")
h_reco1P1N_true1P0N_loosened.SetFillColor(9)
h_reco1P1N_true1P0N_loosened.SetFillStyle(3004)
h_reco1P1N_true1P1N_loosened=f.Get("h_reco1P1N_true1P1N_loosened")
h_reco1P1N_true1P1N_loosened.SetFillColor(2)
h_reco1P1N_true1P1N_loosened.SetFillStyle(3005)
h_reco1P1N_true1PXN_loosened=f.Get("h_reco1P1N_true1PXN_loosened")
h_reco1P1N_true1PXN_loosened.SetFillColor(8)
h_reco1P1N_true1PXN_loosened.SetFillStyle(3005)
h_reco1P1N_true3P_loosened=f.Get("h_reco1P1N_true3P_loosened")
h_reco1P1N_true3P_loosened.SetFillColor(28)
h_reco1P1N_true3P_loosened.SetFillStyle(3005)

#tight
h_reco1P1N_true1P0N_tightened=f.Get("h_reco1P1N_true1P0N_tightened")
h_reco1P1N_true1P0N_tightened.SetFillColor(9)
h_reco1P1N_true1P0N_tightened.SetFillStyle(3004)
h_reco1P1N_true1P1N_tightened=f.Get("h_reco1P1N_true1P1N_tightened")
h_reco1P1N_true1P1N_tightened.SetFillColor(2)
h_reco1P1N_true1P1N_tightened.SetFillStyle(3005)
h_reco1P1N_true1PXN_tightened=f.Get("h_reco1P1N_true1PXN_tightened")
h_reco1P1N_true1PXN_tightened.SetFillColor(8)
h_reco1P1N_true1PXN_tightened.SetFillStyle(3005)
h_reco1P1N_true3P_tightened=f.Get("h_reco1P1N_true3P_tightened")
h_reco1P1N_true3P_tightened.SetFillColor(28)
h_reco1P1N_true3P_tightened.SetFillStyle(3005)

#public
h_reco1P1N_true1P0N_public=f.Get("h_reco1P1N_true1P0N_public")
h_reco1P1N_true1P0N_public.SetFillColor(9)
h_reco1P1N_true1P0N_public.SetFillStyle(3004)
h_reco1P1N_true1P1N_public=f.Get("h_reco1P1N_true1P1N_public")
h_reco1P1N_true1P1N_public.SetFillColor(2)
h_reco1P1N_true1P1N_public.SetFillStyle(3005)
h_reco1P1N_true1PXN_public=f.Get("h_reco1P1N_true1PXN_public")
h_reco1P1N_true1PXN_public.SetFillColor(8)
h_reco1P1N_true1PXN_public.SetFillStyle(3005)
h_reco1P1N_true3P_public=f.Get("h_reco1P1N_true3P_public")
h_reco1P1N_true3P_public.SetFillColor(28)
h_reco1P1N_true3P_public.SetFillStyle(3005)
 
h_1P1N_tightened=ROOT.TH1F("h_1P1N_tightened","reco 1P1N taus - tightened",40,-2,2)
h_1P1N_tightened.SetStats(0)
h_1P1N_normal=ROOT.TH1F("h_1P1N_normal","reco 1P1N taus - normal",40,-2,2)
h_1P1N_normal.SetStats(0)
h_1P1N_loosened=ROOT.TH1F("h_1P1N_loosened","reco 1P1N taus - loosened",40,-2,2)
h_1P1N_loosened.SetStats(0)
h_1P1N_public=ROOT.TH1F("h_1P1N_public","reco 1P1N taus - public",40,-2,2)
h_1P1N_public.SetStats(0)



#Plot

c1=ROOT.TCanvas("dR")
h_dR_normal.Draw()

c2=ROOT.TCanvas("prong")
h_trueP.Draw()
h_cellP.Draw("same")

c3=ROOT.TCanvas("1P1N normal")
s_1_normal=ROOT.THStack("s_1_normal","normal cell based")
h_1P1N_normal.Add(h_reco1P1N_true1P0N_normal)
h_1P1N_normal.Add(h_reco1P1N_true1P1N_normal)
h_1P1N_normal.Add(h_reco1P1N_true1PXN_normal)
h_1P1N_normal.Add(h_reco1P1N_true3P_normal)
h_1P1N_normal.Draw()

s_1_normal.Add(h_reco1P1N_true1P0N_normal)
s_1_normal.Add(h_reco1P1N_true1P1N_normal)
s_1_normal.Add(h_reco1P1N_true1PXN_normal)
s_1_normal.Add(h_reco1P1N_true3P_normal)
s_1_normal.Draw("same")

c3leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c3leg.SetBorderSize(0)
c3leg.SetFillColor(0)
c3leg.SetTextFont(62)
c3leg.SetTextSize(0.050)

RMS1P0N=h_reco1P1N_true1P0N_normal.GetRMS()-h_reco1P1N_true1P0N_normal.GetRMS()%0.001
RMS1P1N=h_reco1P1N_true1P1N_normal.GetRMS()-h_reco1P1N_true1P1N_normal.GetRMS()%0.001
RMS1PXN=h_reco1P1N_true1PXN_normal.GetRMS()-h_reco1P1N_true1PXN_normal.GetRMS()%0.001
RMS3P=h_reco1P1N_true3P_normal.GetRMS()-h_reco1P1N_true3P_normal.GetRMS()%0.001
RMSnorm=h_1P1N_normal.GetRMS()-h_1P1N_normal.GetRMS()%0.001
c3leg.AddEntry("h_1P1N_normal","All Reco "+str(RMSnorm),"lpf")
c3leg.AddEntry("h_reco1P1N_true1P0N_normal","true 1PON "+str(RMS1P0N),"lpf")
c3leg.AddEntry("h_reco1P1N_true1P1N_normal","true 1P1N "+str(RMS1P1N),"lpf")
c3leg.AddEntry("h_reco1P1N_true1PXN_normal","true 1PXN "+str(RMS1PXN),"lpf")
c3leg.AddEntry("h_reco1P1N_true3P_normal","true 3prong "+str(RMS3P),"lpf")
c3leg.Draw()

c4=ROOT.TCanvas("1P1N loosened")
s_1_loosened=ROOT.THStack("s_1_loosened","loosened cell based")

h_1P1N_loosened.Add(h_reco1P1N_true1P0N_loosened)
h_1P1N_loosened.Add(h_reco1P1N_true1P1N_loosened)
h_1P1N_loosened.Add(h_reco1P1N_true1PXN_loosened)
h_1P1N_loosened.Add(h_reco1P1N_true3P_loosened)
h_1P1N_loosened.Draw()

s_1_loosened.Add(h_reco1P1N_true1P0N_loosened)
s_1_loosened.Add(h_reco1P1N_true1P1N_loosened)
s_1_loosened.Add(h_reco1P1N_true1PXN_loosened)
s_1_loosened.Add(h_reco1P1N_true3P_loosened)
s_1_loosened.Draw("same")


c4leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c4leg.SetBorderSize(0)
c4leg.SetFillColor(0)
c4leg.SetTextFont(62)
c4leg.SetTextSize(0.050)

RMS1P0N=h_reco1P1N_true1P0N_loosened.GetRMS()-h_reco1P1N_true1P0N_loosened.GetRMS()%0.001
RMS1P1N=h_reco1P1N_true1P1N_loosened.GetRMS()-h_reco1P1N_true1P1N_loosened.GetRMS()%0.001
RMS1PXN=h_reco1P1N_true1PXN_loosened.GetRMS()-h_reco1P1N_true1PXN_loosened.GetRMS()%0.001
RMS3P=h_reco1P1N_true3P_loosened.GetRMS()-h_reco1P1N_true3P_loosened.GetRMS()%0.001
RMSloose=h_1P1N_loosened.GetRMS()-h_1P1N_loosened.GetRMS()%0.001
c4leg.AddEntry("h_1P1N_loosened","All reco "+str(RMSloose),"lpf")
c4leg.AddEntry("h_reco1P1N_true1P0N_loosened","1PON "+str(RMS1P0N),"lpf")
c4leg.AddEntry("h_reco1P1N_true1P1N_loosened","1P1N "+str(RMS1P1N),"lpf")
c4leg.AddEntry("h_reco1P1N_true1PXN_loosened","1PXN "+str(RMS1PXN),"lpf")
c4leg.AddEntry("h_reco1P1N_true3P_loosened","3prong "+str(RMS3P),"lpf")
c4leg.Draw()


c5=ROOT.TCanvas("1P1N tight")
s_1_tightened=ROOT.THStack("s_1_tightened","tightened cell based")

h_1P1N_tightened.Add(h_reco1P1N_true1P0N_tightened)
h_1P1N_tightened.Add(h_reco1P1N_true1P1N_tightened)
h_1P1N_tightened.Add(h_reco1P1N_true1PXN_tightened)
h_1P1N_tightened.Add(h_reco1P1N_true3P_tightened)
h_1P1N_tightened.Draw()
s_1_tightened.Add(h_reco1P1N_true1P0N_tightened)
s_1_tightened.Add(h_reco1P1N_true1P1N_tightened)
s_1_tightened.Add(h_reco1P1N_true1PXN_tightened)
s_1_tightened.Add(h_reco1P1N_true3P_tightened)
s_1_tightened.Draw("same")


c5leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c5leg.SetBorderSize(0)
c5leg.SetFillColor(0)
c5leg.SetTextFont(62)
c5leg.SetTextSize(0.050)

RMS1P0N=h_reco1P1N_true1P0N_tightened.GetRMS()-h_reco1P1N_true1P0N_tightened.GetRMS()%0.001
RMS1P1N=h_reco1P1N_true1P1N_tightened.GetRMS()-h_reco1P1N_true1P1N_tightened.GetRMS()%0.001
RMS1PXN=h_reco1P1N_true1PXN_tightened.GetRMS()-h_reco1P1N_true1PXN_tightened.GetRMS()%0.001
RMS3P=h_reco1P1N_true3P_tightened.GetRMS()-h_reco1P1N_true3P_tightened.GetRMS()%0.001
RMStight=h_1P1N_tightened.GetRMS()-h_1P1N_tightened.GetRMS()%0.001
c5leg.AddEntry("h_1P1N_tightened","all Reco "+str(RMStight),"lpf")
c5leg.AddEntry("h_reco1P1N_true1P0N_tightened","1PON "+str(RMS1P0N),"lpf")
c5leg.AddEntry("h_reco1P1N_true1P1N_tightened","1P1N "+str(RMS1P1N),"lpf")
c5leg.AddEntry("h_reco1P1N_true1PXN_tightened","1PXN "+str(RMS1PXN),"lpf")
c5leg.AddEntry("h_reco1P1N_true3P_tightened","3prong "+str(RMS3P),"lpf")
c5leg.Draw()

c6=ROOT.TCanvas("1P1N public")
s_1_public=ROOT.THStack("s_1_public","public cell based")

h_1P1N_public.Add(h_reco1P1N_true1P0N_public)
h_1P1N_public.Add(h_reco1P1N_true1P1N_public)
h_1P1N_public.Add(h_reco1P1N_true1PXN_public)
h_1P1N_public.Add(h_reco1P1N_true3P_public)
h_1P1N_public.Draw()

s_1_public.Add(h_reco1P1N_true1P0N_public)
s_1_public.Add(h_reco1P1N_true1P1N_public)
s_1_public.Add(h_reco1P1N_true1PXN_public)
s_1_public.Add(h_reco1P1N_true3P_public)
s_1_public.Draw("same")

c6leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c6leg.SetBorderSize(0)
c6leg.SetFillColor(0)
c6leg.SetTextFont(62)
c6leg.SetTextSize(0.050)
RMS1P1N=h_reco1P1N_true1P1N_public.GetRMS()-h_reco1P1N_true1P1N_public.GetRMS()%0.001
RMS1P0N=h_reco1P1N_true1P0N_public.GetRMS()-h_reco1P1N_true1P0N_public.GetRMS()%0.001
RMS1PXN=h_reco1P1N_true1PXN_public.GetRMS()-h_reco1P1N_true1PXN_public.GetRMS()%0.001
RMS3P=h_reco1P1N_true3P_public.GetRMS()-h_reco1P1N_true3P_public.GetRMS()%0.001
RMSpublic=h_1P1N_public.GetRMS()-h_1P1N_public.GetRMS()%0.001

c6leg.AddEntry("h_1P1N_public","All reco "+str(RMSpublic),"lpf")
c6leg.AddEntry("h_reco1P1N_true1P0N_public","1PON "+str(RMS1P0N),"lpf")
c6leg.AddEntry("h_reco1P1N_true1P1N_public","1P1N "+str(RMS1P1N),"lpf")
c6leg.AddEntry("h_reco1P1N_true1PXN_public","1PXN "+str(RMS1PXN),"lpf")
c6leg.AddEntry("h_reco1P1N_true3P_public","3prong "+str(RMS3P),"lpf")
c6leg.Draw()

c7=ROOT.TCanvas("1P0N normal")
s_0_normal=ROOT.THStack("s_0_normal","normal cell based")
h_1P0N_normal.Add(h_reco1P0N_true1P0N_normal)
h_1P0N_normal.Add(h_reco1P0N_true1P1N_normal)
h_1P0N_normal.Add(h_reco1P0N_true1PXN_normal)
h_1P0N_normal.Add(h_reco1P0N_true3P_normal)
h_1P0N_normal.Draw()
s_0_normal.Add(h_reco1P0N_true1P1N_normal)
s_0_normal.Add(h_reco1P0N_true1PXN_normal)
s_0_normal.Add(h_reco1P0N_true3P_normal)
s_0_normal.Add(h_reco1P0N_true1P0N_normal)
s_0_normal.Draw("same")

c7leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c7leg.SetBorderSize(0)
c7leg.SetFillColor(0)
c7leg.SetTextFont(62)
c7leg.SetTextSize(0.050)

RMS1P0Nn=h_reco1P0N_true1P0N_normal.GetRMS()-h_reco1P0N_true1P0N_normal.GetRMS()%0.001
RMS1P1Nn=h_reco1P0N_true1P1N_normal.GetRMS()-h_reco1P0N_true1P1N_normal.GetRMS()%0.001
RMS1PXNn=h_reco1P0N_true1PXN_normal.GetRMS()-h_reco1P0N_true1PXN_normal.GetRMS()%0.001
RMS3Pn=h_reco1P0N_true3P_normal.GetRMS()-h_reco1P0N_true3P_normal.GetRMS()%0.001
RMSnorm=h_1P0N_normal.GetRMS()-h_1P0N_normal.GetRMS()%0.001
c7leg.AddEntry("h_1P0N_normal","All Reco "+str(RMSnorm),"lpf")
c7leg.AddEntry("h_reco1P0N_true1P0N_normal","true 1P0N "+str(RMS1P0Nn),"lpf")
c7leg.AddEntry("h_reco1P0N_true1P1N_normal","true 1P1N "+str(RMS1P1Nn),"lpf")
c7leg.AddEntry("h_reco1P0N_true1PXN_normal","true 1PXN "+str(RMS1PXNn),"lpf")
c7leg.AddEntry("h_reco1P0N_true3P_normal","true 3prong "+str(RMS3Pn),"lpf")
c7leg.Draw()

c8=ROOT.TCanvas("1P0N loosened")
s_0_loosened=ROOT.THStack("s_0_loosened","loosened cell based")

h_1P0N_loosened.Add(h_reco1P0N_true1P0N_loosened)
h_1P0N_loosened.Add(h_reco1P0N_true1P1N_loosened)
h_1P0N_loosened.Add(h_reco1P0N_true1PXN_loosened)
h_1P0N_loosened.Add(h_reco1P0N_true3P_loosened)
h_1P0N_loosened.Draw()

s_0_loosened.Add(h_reco1P0N_true1P1N_loosened)
s_0_loosened.Add(h_reco1P0N_true1PXN_loosened)
s_0_loosened.Add(h_reco1P0N_true3P_loosened)
s_0_loosened.Add(h_reco1P0N_true1P0N_loosened)
s_0_loosened.Draw("same")


c8leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c8leg.SetBorderSize(0)
c8leg.SetFillColor(0)
c8leg.SetTextFont(62)
c8leg.SetTextSize(0.050)

RMS1P0Nl=h_reco1P0N_true1P0N_loosened.GetRMS()-h_reco1P0N_true1P0N_loosened.GetRMS()%0.001
RMS1P1Nl=h_reco1P0N_true1P1N_loosened.GetRMS()-h_reco1P0N_true1P1N_loosened.GetRMS()%0.001
RMS1PXNl=h_reco1P0N_true1PXN_loosened.GetRMS()-h_reco1P0N_true1PXN_loosened.GetRMS()%0.001
RMS3Pl=h_reco1P0N_true3P_loosened.GetRMS()-h_reco1P0N_true3P_loosened.GetRMS()%0.001
RMSloose=h_1P0N_loosened.GetRMS()-h_1P0N_loosened.GetRMS()%0.001
c8leg.AddEntry("h_1P0N_loosened","All reco "+str(RMSloose),"lpf")
c8leg.AddEntry("h_reco1P0N_true1P0N_loosened","1PON "+str(RMS1P0Nl),"lpf")
c8leg.AddEntry("h_reco1P0N_true1P1N_loosened","1P1N "+str(RMS1P1Nl),"lpf")
c8leg.AddEntry("h_reco1P0N_true1PXN_loosened","1PXN "+str(RMS1PXNl),"lpf")
c8leg.AddEntry("h_reco1P0N_true3P_loosened","3prong "+str(RMS3Pl),"lpf")
c8leg.Draw()


c9=ROOT.TCanvas("1P0N tight")
s_0_tightened=ROOT.THStack("s_0_tightened","tightened cell based")

h_1P0N_tightened.Add(h_reco1P0N_true1P0N_tightened)
h_1P0N_tightened.Add(h_reco1P0N_true1P1N_tightened)
h_1P0N_tightened.Add(h_reco1P0N_true1PXN_tightened)
h_1P0N_tightened.Add(h_reco1P0N_true3P_tightened)
h_1P0N_tightened.Draw()

s_0_tightened.Add(h_reco1P0N_true1P1N_tightened)
s_0_tightened.Add(h_reco1P0N_true1PXN_tightened)
s_0_tightened.Add(h_reco1P0N_true3P_tightened)
s_0_tightened.Add(h_reco1P0N_true1P0N_tightened)
s_0_tightened.Draw("same")


c9leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c9leg.SetBorderSize(0)
c9leg.SetFillColor(0)
c9leg.SetTextFont(62)
c9leg.SetTextSize(0.050)

RMS1P0Nt=h_reco1P0N_true1P0N_tightened.GetRMS()-h_reco1P0N_true1P0N_tightened.GetRMS()%0.001
RMS1P1Nt=h_reco1P0N_true1P1N_tightened.GetRMS()-h_reco1P0N_true1P1N_tightened.GetRMS()%0.001
RMS1PXNt=h_reco1P0N_true1PXN_tightened.GetRMS()-h_reco1P0N_true1PXN_tightened.GetRMS()%0.001
RMS3Pt=h_reco1P0N_true3P_tightened.GetRMS()-h_reco1P0N_true3P_tightened.GetRMS()%0.001
RMStight=h_1P0N_tightened.GetRMS()-h_1P0N_tightened.GetRMS()%0.001
c9leg.AddEntry("h_1P0N_tightened","all Reco "+str(RMStight),"lpf")
c9leg.AddEntry("h_reco1P0N_true1P0N_tightened","1PON "+str(RMS1P0Nt),"lpf")
c9leg.AddEntry("h_reco1P0N_true1P1N_tightened","1P1N "+str(RMS1P1Nt),"lpf")
c9leg.AddEntry("h_reco1P0N_true1PXN_tightened","1PXN "+str(RMS1PXNt),"lpf")
c9leg.AddEntry("h_reco1P0N_true3P_tightened","3prong "+str(RMS3Pt),"lpf")
c9leg.Draw()

c10=ROOT.TCanvas("1P0N public")
s_0_public=ROOT.THStack("s_0_public","public cell based")

h_1P0N_public.Add(h_reco1P0N_true1P0N_public)
h_1P0N_public.Add(h_reco1P0N_true1P1N_public)
h_1P0N_public.Add(h_reco1P0N_true1PXN_public)
h_1P0N_public.Add(h_reco1P0N_true3P_public)
h_1P0N_public.Draw()


s_0_public.Add(h_reco1P0N_true1P1N_public)
s_0_public.Add(h_reco1P0N_true1PXN_public)
s_0_public.Add(h_reco1P0N_true3P_public)
s_0_public.Add(h_reco1P0N_true1P0N_public)
s_0_public.Draw("same")

c10leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c10leg.SetBorderSize(0)
c10leg.SetFillColor(0)
c10leg.SetTextFont(62)
c10leg.SetTextSize(0.050)

RMS1P0Np=h_reco1P0N_true1P0N_public.GetRMS()-h_reco1P0N_true1P0N_public.GetRMS()%0.001
RMS1P1Np=h_reco1P0N_true1P1N_public.GetRMS()-h_reco1P0N_true1P1N_public.GetRMS()%0.001
RMS1PXNp=h_reco1P0N_true1PXN_public.GetRMS()-h_reco1P0N_true1PXN_public.GetRMS()%0.001
RMS3Pp=h_reco1P0N_true3P_public.GetRMS()-h_reco1P0N_true3P_public.GetRMS()%0.001
RMSpublic=h_1P0N_public.GetRMS()-h_1P0N_public.GetRMS()%0.001

c10leg.AddEntry("h_1P0N_public","All reco "+str(RMSpublic),"lpf")
c10leg.AddEntry("h_reco1P0N_true1P0N_public","1PON "+str(RMS1P0Np),"lpf")
c10leg.AddEntry("h_reco1P0N_true1P1N_public","1P1N "+str(RMS1P1Np),"lpf")
c10leg.AddEntry("h_reco1P0N_true1PXN_public","1PXN "+str(RMS1PXNp),"lpf")
c10leg.AddEntry("h_reco1P0N_true3P_public","3prong "+str(RMS3Pp),"lpf")
c10leg.Draw()

