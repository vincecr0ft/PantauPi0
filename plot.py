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

#cons
h_reco1P0N_true1P0N_cons=f.Get("h_reco1P0N_true1P0N_cons")
h_reco1P0N_true1P0N_cons.SetFillColor(9)
h_reco1P0N_true1P0N_cons.SetFillStyle(3004)
h_reco1P0N_true1P1N_cons=f.Get("h_reco1P0N_true1P1N_cons")
h_reco1P0N_true1P1N_cons.SetFillColor(2)
h_reco1P0N_true1P1N_cons.SetFillStyle(3005)
h_reco1P0N_true1PXN_cons=f.Get("h_reco1P0N_true1PXN_cons")
h_reco1P0N_true1PXN_cons.SetFillColor(8)
h_reco1P0N_true1PXN_cons.SetFillStyle(3005)
h_reco1P0N_true3P_cons=f.Get("h_reco1P0N_true3P_cons")
h_reco1P0N_true3P_cons.SetFillColor(28)
h_reco1P0N_true3P_cons.SetFillStyle(3005)
 
h_1P0N_tightened=ROOT.TH1F("h_1P0N_tightened","reco 1P0N taus - tightened",40,-2,2)
h_1P0N_tightened.SetStats(0)
h_1P0N_normal=ROOT.TH1F("h_1P0N_normal","reco 1P0N taus - normal",40,-2,2)
h_1P0N_normal.SetStats(0)
h_1P0N_loosened=ROOT.TH1F("h_1P0N_loosened","reco 1P0N taus - loosened",40,-2,2)
h_1P0N_loosened.SetStats(0)
h_1P0N_public=ROOT.TH1F("h_1P0N_public","reco 1P0N taus - public",40,-2,2)
h_1P0N_public.SetStats(0)
h_1P0N_cons=ROOT.TH1F("h_1P0N_cons","reco 1P0N taus - cons",40,-2,2)
h_1P0N_cons.SetStats(0)


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

#cons
h_reco1P1N_true1P0N_cons=f.Get("h_reco1P1N_true1P0N_cons")
h_reco1P1N_true1P0N_cons.SetFillColor(9)
h_reco1P1N_true1P0N_cons.SetFillStyle(3004)
h_reco1P1N_true1P1N_cons=f.Get("h_reco1P1N_true1P1N_cons")
h_reco1P1N_true1P1N_cons.SetFillColor(2)
h_reco1P1N_true1P1N_cons.SetFillStyle(3005)
h_reco1P1N_true1PXN_cons=f.Get("h_reco1P1N_true1PXN_cons")
h_reco1P1N_true1PXN_cons.SetFillColor(8)
h_reco1P1N_true1PXN_cons.SetFillStyle(3005)
h_reco1P1N_true3P_cons=f.Get("h_reco1P1N_true3P_cons")
h_reco1P1N_true3P_cons.SetFillColor(28)
h_reco1P1N_true3P_cons.SetFillStyle(3005)
 
h_1P1N_tightened=ROOT.TH1F("h_1P1N_tightened","reco 1P1N taus - tightened",40,-2,2)
h_1P1N_tightened.SetStats(0)
h_1P1N_normal=ROOT.TH1F("h_1P1N_normal","reco 1P1N taus - normal",40,-2,2)
h_1P1N_normal.SetStats(0)
h_1PN_normal=ROOT.TH1F("h_1PN_normal","reco 1P taus with neutrals - normal",40,-2,2)
h_1PN_normal.SetStats(0)
h_1PN_cons=ROOT.TH1F("h_1PN_cons","reco 1P taus with neutrals - cons",40,-2,2)
h_1PN_cons.SetStats(0)
h_1P1N_loosened=ROOT.TH1F("h_1P1N_loosened","reco 1P1N taus - loosened",40,-2,2)
h_1P1N_loosened.SetStats(0)
h_1P1N_public=ROOT.TH1F("h_1P1N_public","reco 1P1N taus - public",40,-2,2)
h_1P1N_public.SetStats(0)
h_1PN_public=ROOT.TH1F("h_1PN_public","reco 1P taus with neutrals - public",40,-2,2)
h_1PN_public.SetStats(0)
h_1P1N_cons=ROOT.TH1F("h_1P1N_cons","reco 1P1N taus - cons",40,-2,2)
h_1P1N_cons.SetStats(0)




###################   1PXN   ###################

#normal
h_reco1PXN_true1P0N_normal=f.Get("h_reco1PXN_true1P0N_normal")
h_reco1PXN_true1P0N_normal.SetFillColor(9)
h_reco1PXN_true1P0N_normal.SetFillStyle(3004)
h_reco1PXN_true1P1N_normal=f.Get("h_reco1PXN_true1P1N_normal")
h_reco1PXN_true1P1N_normal.SetFillColor(2)
h_reco1PXN_true1P1N_normal.SetFillStyle(3005)
h_reco1PXN_true1PXN_normal=f.Get("h_reco1PXN_true1PXN_normal")
h_reco1PXN_true1PXN_normal.SetFillColor(8)
h_reco1PXN_true1PXN_normal.SetFillStyle(3005)
h_reco1PXN_true3P_normal=f.Get("h_reco1PXN_true3P_normal")
h_reco1PXN_true3P_normal.SetFillColor(28)
h_reco1PXN_true3P_normal.SetFillStyle(3005)

#loose
h_reco1PXN_true1P0N_loosened=f.Get("h_reco1PXN_true1P0N_loosened")
h_reco1PXN_true1P0N_loosened.SetFillColor(9)
h_reco1PXN_true1P0N_loosened.SetFillStyle(3004)
h_reco1PXN_true1P1N_loosened=f.Get("h_reco1PXN_true1P1N_loosened")
h_reco1PXN_true1P1N_loosened.SetFillColor(2)
h_reco1PXN_true1P1N_loosened.SetFillStyle(3005)
h_reco1PXN_true1PXN_loosened=f.Get("h_reco1PXN_true1PXN_loosened")
h_reco1PXN_true1PXN_loosened.SetFillColor(8)
h_reco1PXN_true1PXN_loosened.SetFillStyle(3005)
h_reco1PXN_true3P_loosened=f.Get("h_reco1PXN_true3P_loosened")
h_reco1PXN_true3P_loosened.SetFillColor(28)
h_reco1PXN_true3P_loosened.SetFillStyle(3005)

#tight
h_reco1PXN_true1P0N_tightened=f.Get("h_reco1PXN_true1P0N_tightened")
h_reco1PXN_true1P0N_tightened.SetFillColor(9)
h_reco1PXN_true1P0N_tightened.SetFillStyle(3004)
h_reco1PXN_true1P1N_tightened=f.Get("h_reco1PXN_true1P1N_tightened")
h_reco1PXN_true1P1N_tightened.SetFillColor(2)
h_reco1PXN_true1P1N_tightened.SetFillStyle(3005)
h_reco1PXN_true1PXN_tightened=f.Get("h_reco1PXN_true1PXN_tightened")
h_reco1PXN_true1PXN_tightened.SetFillColor(8)
h_reco1PXN_true1PXN_tightened.SetFillStyle(3005)
h_reco1PXN_true3P_tightened=f.Get("h_reco1PXN_true3P_tightened")
h_reco1PXN_true3P_tightened.SetFillColor(28)
h_reco1PXN_true3P_tightened.SetFillStyle(3005)

#public
h_reco1PXN_true1P0N_public=f.Get("h_reco1PXN_true1P0N_public")
h_reco1PXN_true1P0N_public.SetFillColor(9)
h_reco1PXN_true1P0N_public.SetFillStyle(3004)
h_reco1PXN_true1P1N_public=f.Get("h_reco1PXN_true1P1N_public")
h_reco1PXN_true1P1N_public.SetFillColor(2)
h_reco1PXN_true1P1N_public.SetFillStyle(3005)
h_reco1PXN_true1PXN_public=f.Get("h_reco1PXN_true1PXN_public")
h_reco1PXN_true1PXN_public.SetFillColor(8)
h_reco1PXN_true1PXN_public.SetFillStyle(3005)
h_reco1PXN_true3P_public=f.Get("h_reco1PXN_true3P_public")
h_reco1PXN_true3P_public.SetFillColor(28)
h_reco1PXN_true3P_public.SetFillStyle(3005)


#cons
h_reco1PXN_true1P0N_cons=f.Get("h_reco1PXN_true1P0N_cons")
h_reco1PXN_true1P0N_cons.SetFillColor(9)
h_reco1PXN_true1P0N_cons.SetFillStyle(3004)
h_reco1PXN_true1P1N_cons=f.Get("h_reco1PXN_true1P1N_cons")
h_reco1PXN_true1P1N_cons.SetFillColor(2)
h_reco1PXN_true1P1N_cons.SetFillStyle(3005)
h_reco1PXN_true1PXN_cons=f.Get("h_reco1PXN_true1PXN_cons")
h_reco1PXN_true1PXN_cons.SetFillColor(8)
h_reco1PXN_true1PXN_cons.SetFillStyle(3005)
h_reco1PXN_true3P_cons=f.Get("h_reco1PXN_true3P_cons")
h_reco1PXN_true3P_cons.SetFillColor(28)
h_reco1PXN_true3P_cons.SetFillStyle(3005)
 
h_1PXN_tightened=ROOT.TH1F("h_1PXN_tightened","reco 1PXN taus - tightened",40,-2,2)
h_1PXN_tightened.SetStats(0)
h_1PXN_normal=ROOT.TH1F("h_1PXN_normal","reco 1PXN taus - normal",40,-2,2)
h_1PXN_normal.SetStats(0)
h_1PXN_loosened=ROOT.TH1F("h_1PXN_loosened","reco 1PXN taus - loosened",40,-2,2)
h_1PXN_loosened.SetStats(0)
h_1PXN_public=ROOT.TH1F("h_1PXN_public","reco 1PXN taus - public",40,-2,2)
h_1PXN_public.SetStats(0)
h_1PXN_cons=ROOT.TH1F("h_1PXN_cons","reco 1PXN taus - cons",40,-2,2)
h_1PXN_cons.SetStats(0)

#inclusive
h_inc_normal=ROOT.TH1F("h_inc_normal","1Pinclusive - normal",40,-2,2)
h_inc_normal.SetStats(0)
h_inc_loosened=ROOT.TH1F("h_inc_loosened","1Pinclusive - loosened",40,-2,2)
h_inc_loosened.SetStats(0)
h_inc_public=ROOT.TH1F("h_inc_public","1Pinclusive -public",40,-2,2)
h_inc_public.SetStats(0)
h_inc_cons=ROOT.TH1F("h_inc_cons","1Pinclusive - cons",40,-2,2)
h_inc_cons.SetStats(0)





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

RMS1P0Nn=h_reco1P1N_true1P0N_normal.GetRMS()-h_reco1P1N_true1P0N_normal.GetRMS()%0.001
RMS1P1Nn=h_reco1P1N_true1P1N_normal.GetRMS()-h_reco1P1N_true1P1N_normal.GetRMS()%0.001
RMS1PXNn=h_reco1P1N_true1PXN_normal.GetRMS()-h_reco1P1N_true1PXN_normal.GetRMS()%0.001
RMS3Pn=h_reco1P1N_true3P_normal.GetRMS()-h_reco1P1N_true3P_normal.GetRMS()%0.001
RMSnorm_1P1N=h_1P1N_normal.GetRMS()-h_1P1N_normal.GetRMS()%0.001
c3leg.AddEntry("h_1P1N_normal","All Reco "+str(RMSnorm_1P1N),"lpf")
c3leg.AddEntry("h_reco1P1N_true1P0N_normal","true 1PON "+str(RMS1P0Nn),"lpf")
c3leg.AddEntry("h_reco1P1N_true1P1N_normal","true 1P1N "+str(RMS1P1Nn),"lpf")
c3leg.AddEntry("h_reco1P1N_true1PXN_normal","true 1PXN "+str(RMS1PXNn),"lpf")
c3leg.AddEntry("h_reco1P1N_true3P_normal","true 3prong "+str(RMS3Pn),"lpf")
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

RMS1P0Nl=h_reco1P1N_true1P0N_loosened.GetRMS()-h_reco1P1N_true1P0N_loosened.GetRMS()%0.001
RMS1P1Nl=h_reco1P1N_true1P1N_loosened.GetRMS()-h_reco1P1N_true1P1N_loosened.GetRMS()%0.001
RMS1PXNl=h_reco1P1N_true1PXN_loosened.GetRMS()-h_reco1P1N_true1PXN_loosened.GetRMS()%0.001
RMS3Pl=h_reco1P1N_true3P_loosened.GetRMS()-h_reco1P1N_true3P_loosened.GetRMS()%0.001
RMSloose_1P1N=h_1P1N_loosened.GetRMS()-h_1P1N_loosened.GetRMS()%0.001
c4leg.AddEntry("h_1P1N_loosened","All reco "+str(RMSloose_1P1N),"lpf")
c4leg.AddEntry("h_reco1P1N_true1P0N_loosened","1PON "+str(RMS1P0Nl),"lpf")
c4leg.AddEntry("h_reco1P1N_true1P1N_loosened","1P1N "+str(RMS1P1Nl),"lpf")
c4leg.AddEntry("h_reco1P1N_true1PXN_loosened","1PXN "+str(RMS1PXNl),"lpf")
c4leg.AddEntry("h_reco1P1N_true3P_loosened","3prong "+str(RMS3Pl),"lpf")
c4leg.Draw()


c5=ROOT.TCanvas("1P1N classification conserved")
s_1_cons=ROOT.THStack("s_1_cons","cons cell based")

h_1P1N_cons.Add(h_reco1P1N_true1P0N_cons)
h_1P1N_cons.Add(h_reco1P1N_true1P1N_cons)
h_1P1N_cons.Add(h_reco1P1N_true1PXN_cons)
h_1P1N_cons.Add(h_reco1P1N_true3P_cons)
h_1P1N_cons.Draw()
s_1_cons.Add(h_reco1P1N_true1P0N_cons)
s_1_cons.Add(h_reco1P1N_true1P1N_cons)
s_1_cons.Add(h_reco1P1N_true1PXN_cons)
s_1_cons.Add(h_reco1P1N_true3P_cons)
s_1_cons.Draw("same")


c5leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c5leg.SetBorderSize(0)
c5leg.SetFillColor(0)
c5leg.SetTextFont(62)
c5leg.SetTextSize(0.050)

RMS1P0Nc=h_reco1P1N_true1P0N_cons.GetRMS()-h_reco1P1N_true1P0N_cons.GetRMS()%0.001
RMS1P1Nc=h_reco1P1N_true1P1N_cons.GetRMS()-h_reco1P1N_true1P1N_cons.GetRMS()%0.001
RMS1PXNc=h_reco1P1N_true1PXN_cons.GetRMS()-h_reco1P1N_true1PXN_cons.GetRMS()%0.001
RMS3Pc=h_reco1P1N_true3P_cons.GetRMS()-h_reco1P1N_true3P_cons.GetRMS()%0.001
RMScons_1P1N=h_1P1N_cons.GetRMS()-h_1P1N_cons.GetRMS()%0.001
c5leg.AddEntry("h_1P1N_cons","all Reco "+str(RMScons_1P1N),"lpf")
c5leg.AddEntry("h_reco1P1N_true1P0N_cons","1PON "+str(RMS1P0Nc),"lpf")
c5leg.AddEntry("h_reco1P1N_true1P1N_cons","1P1N "+str(RMS1P1Nc),"lpf")
c5leg.AddEntry("h_reco1P1N_true1PXN_cons","1PXN "+str(RMS1PXNc),"lpf")
c5leg.AddEntry("h_reco1P1N_true3P_cons","3prong "+str(RMS3Pc),"lpf")
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
RMS1P1Np=h_reco1P1N_true1P1N_public.GetRMS()-h_reco1P1N_true1P1N_public.GetRMS()%0.001
RMS1P0Np=h_reco1P1N_true1P0N_public.GetRMS()-h_reco1P1N_true1P0N_public.GetRMS()%0.001
RMS1PXNp=h_reco1P1N_true1PXN_public.GetRMS()-h_reco1P1N_true1PXN_public.GetRMS()%0.001
RMS3Pp=h_reco1P1N_true3P_public.GetRMS()-h_reco1P1N_true3P_public.GetRMS()%0.001
RMSpublic_1P1N=h_1P1N_public.GetRMS()-h_1P1N_public.GetRMS()%0.001

c6leg.AddEntry("h_1P1N_public","All reco "+str(RMSpublic_1P1N),"lpf")
c6leg.AddEntry("h_reco1P1N_true1P0N_public","1PON "+str(RMS1P0Np),"lpf")
c6leg.AddEntry("h_reco1P1N_true1P1N_public","1P1N "+str(RMS1P1Np),"lpf")
c6leg.AddEntry("h_reco1P1N_true1PXN_public","1PXN "+str(RMS1PXNp),"lpf")
c6leg.AddEntry("h_reco1P1N_true3P_public","3prong "+str(RMS3Pp),"lpf")
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
RMSnorm_1P0N=h_1P0N_normal.GetRMS()-h_1P0N_normal.GetRMS()%0.001
c7leg.AddEntry("h_1P0N_normal","All Reco "+str(RMSnorm_1P0N),"lpf")
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
RMSloose_1P0N=h_1P0N_loosened.GetRMS()-h_1P0N_loosened.GetRMS()%0.001
c8leg.AddEntry("h_1P0N_loosened","All reco "+str(RMSloose_1P0N),"lpf")
c8leg.AddEntry("h_reco1P0N_true1P0N_loosened","1PON "+str(RMS1P0Nl),"lpf")
c8leg.AddEntry("h_reco1P0N_true1P1N_loosened","1P1N "+str(RMS1P1Nl),"lpf")
c8leg.AddEntry("h_reco1P0N_true1PXN_loosened","1PXN "+str(RMS1PXNl),"lpf")
c8leg.AddEntry("h_reco1P0N_true3P_loosened","3prong "+str(RMS3Pl),"lpf")
c8leg.Draw()


c9=ROOT.TCanvas("1P0N cons")
s_0_cons=ROOT.THStack("s_0_cons","cons cell based")

h_1P0N_cons.Add(h_reco1P0N_true1P0N_cons)
h_1P0N_cons.Add(h_reco1P0N_true1P1N_cons)
h_1P0N_cons.Add(h_reco1P0N_true1PXN_cons)
h_1P0N_cons.Add(h_reco1P0N_true3P_cons)
h_1P0N_cons.Draw()

s_0_cons.Add(h_reco1P0N_true1P1N_cons)
s_0_cons.Add(h_reco1P0N_true1PXN_cons)
s_0_cons.Add(h_reco1P0N_true3P_cons)
s_0_cons.Add(h_reco1P0N_true1P0N_cons)
s_0_cons.Draw("same")


c9leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c9leg.SetBorderSize(0)
c9leg.SetFillColor(0)
c9leg.SetTextFont(62)
c9leg.SetTextSize(0.050)

RMS1P0Nc=h_reco1P0N_true1P0N_cons.GetRMS()-h_reco1P0N_true1P0N_cons.GetRMS()%0.001
RMS1P1Nc=h_reco1P0N_true1P1N_cons.GetRMS()-h_reco1P0N_true1P1N_cons.GetRMS()%0.001
RMS1PXNc=h_reco1P0N_true1PXN_cons.GetRMS()-h_reco1P0N_true1PXN_cons.GetRMS()%0.001
RMS3Pc=h_reco1P0N_true3P_cons.GetRMS()-h_reco1P0N_true3P_cons.GetRMS()%0.001
RMScons_1P0N=h_1P0N_cons.GetRMS()-h_1P0N_cons.GetRMS()%0.001
c9leg.AddEntry("h_1P0N_cons","all Reco "+str(RMScons_1P0N),"lpf")
c9leg.AddEntry("h_reco1P0N_true1P0N_cons","1PON "+str(RMS1P0Nc),"lpf")
c9leg.AddEntry("h_reco1P0N_true1P1N_cons","1P1N "+str(RMS1P1Nc),"lpf")
c9leg.AddEntry("h_reco1P0N_true1PXN_cons","1PXN "+str(RMS1PXNc),"lpf")
c9leg.AddEntry("h_reco1P0N_true3P_cons","3prong "+str(RMS3Pc),"lpf")
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
RMSpublic_1P0N=h_1P0N_public.GetRMS()-h_1P0N_public.GetRMS()%0.001

c10leg.AddEntry("h_1P0N_public","All reco "+str(RMSpublic_1P0N),"lpf")
c10leg.AddEntry("h_reco1P0N_true1P0N_public","1PON "+str(RMS1P0Np),"lpf")
c10leg.AddEntry("h_reco1P0N_true1P1N_public","1P1N "+str(RMS1P1Np),"lpf")
c10leg.AddEntry("h_reco1P0N_true1PXN_public","1PXN "+str(RMS1PXNp),"lpf")
c10leg.AddEntry("h_reco1P0N_true3P_public","3prong "+str(RMS3Pp),"lpf")
c10leg.Draw()



#need 1PXN
h_1PXN_normal.Add(h_reco1PXN_true1P0N_normal)
h_1PXN_normal.Add(h_reco1PXN_true1P1N_normal)
h_1PXN_normal.Add(h_reco1PXN_true1PXN_normal)
h_1PXN_normal.Add(h_reco1PXN_true3P_normal)
h_1PXN_loosened.Add(h_reco1PXN_true1P0N_loosened)
h_1PXN_loosened.Add(h_reco1PXN_true1P1N_loosened)
h_1PXN_loosened.Add(h_reco1PXN_true1PXN_loosened)
h_1PXN_loosened.Add(h_reco1PXN_true3P_loosened)
h_1PXN_public.Add(h_reco1PXN_true1P0N_public)
h_1PXN_public.Add(h_reco1PXN_true1P1N_public)
h_1PXN_public.Add(h_reco1PXN_true1PXN_public)
h_1PXN_public.Add(h_reco1PXN_true3P_public)
h_1PXN_cons.Add(h_reco1PXN_true1P0N_cons)
h_1PXN_cons.Add(h_reco1PXN_true1P1N_cons)
h_1PXN_cons.Add(h_reco1PXN_true1PXN_cons)
h_1PXN_cons.Add(h_reco1PXN_true3P_cons)



c11=ROOT.TCanvas("Neutral Comparison")

h_1PN_normal.Add(h_1P1N_normal)
h_1PN_normal.Add(h_1PXN_normal)
h_1PN_normal.SetFillColor(2)
h_1PN_normal.SetFillStyle(3001)
h_1PN_normal.Draw()
h_1PN_public.Add(h_1P1N_public)
h_1PN_public.Add(h_1PXN_public)
h_1PN_public.SetFillColor(6)
h_1PN_public.SetFillStyle(3001)
h_1PN_public.Draw("same")
h_1PN_cons.Add(h_1P1N_cons)
h_1PN_cons.Add(h_1PXN_cons)
h_1PN_cons.SetFillColor(6)
h_1PN_cons.SetFillStyle(3001)
h_1PN_cons.Draw("same")


c11leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c11leg.SetBorderSize(0)
c11leg.SetFillColor(0)
c11leg.SetTextFont(62)
c11leg.SetTextSize(0.050)

RMSnNorm=h_1PN_normal.GetRMS()-h_1PN_normal.GetRMS()%0.001
RMSnPub=h_1PN_public.GetRMS()-h_1PN_public.GetRMS()%0.001
RMSnCons=h_1PN_cons.GetRMS()-h_1PN_cons.GetRMS()%0.001

c11leg.AddEntry("h_1PN_normal","1P1N +1PXN normal","lpf")
c11leg.AddEntry("h_1PN_normal","RMS"+str(RMSnNorm),"lpf")
c11leg.AddEntry("h_1PN_public","1P1N +1PXN public","lpf")
c11leg.AddEntry("h_1PN_public","RMS"+str(RMSnPub),"lpf")
c11leg.Draw()


c12=ROOT.TCanvas("1Pinc normal")

h_inc_normal.Add(h_1P0N_normal)
h_inc_normal.Add(h_1P1N_normal)
h_inc_normal.Add(h_1PXN_normal)
h_inc_normal.SetFillColor(2)
h_inc_normal.SetFillStyle(3001)
h_inc_normal.Draw()

h_inc_loosened.Add(h_1P0N_loosened)
h_inc_loosened.Add(h_1P1N_loosened)
h_inc_loosened.Add(h_1PXN_loosened)
h_inc_loosened.SetFillColor(12)
h_inc_loosened.SetFillStyle(3001)
h_inc_loosened.Draw("same")

h_inc_public.Add(h_1P0N_public)
h_inc_public.Add(h_1P1N_public)
h_inc_public.Add(h_1PXN_public)
h_inc_public.SetFillColor(38)
h_inc_public.SetFillStyle(3001)
h_inc_public.Draw("same")

h_inc_cons.Add(h_1P0N_cons)
h_inc_cons.Add(h_1P1N_cons)
h_inc_cons.Add(h_1PXN_cons)
h_inc_cons.SetFillColor(8)
h_inc_cons.SetFillStyle(3001)
h_inc_cons.Draw("same")

c12leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c12leg.SetBorderSize(0)
c12leg.SetFillColor(0)
c12leg.SetTextFont(62)
c12leg.SetTextSize(0.050)

RMSn=h_inc_normal.GetRMS()-h_inc_normal.GetRMS()%0.001
RMSl=h_inc_loosened.GetRMS()-h_inc_loosened.GetRMS()%0.001
RMSp=h_inc_public.GetRMS()-h_inc_public.GetRMS()%0.001
RMSc=h_inc_cons.GetRMS()-h_inc_cons.GetRMS()%0.001

c12leg.AddEntry("h_inc_normal","normal "+str(RMSn),"lpf")
c12leg.AddEntry("h_inc_loosened","loosened "+str(RMSl),"lpf")
c12leg.AddEntry("h_inc_public","public "+str(RMSp),"lpf")
c12leg.AddEntry("h_inc_cons","cons "+str(RMSc),"lpf")

c12leg.Draw()


c13=ROOT.TCanvas("1PXN normal")
s_X_normal=ROOT.THStack("s_X_normal","normal cell based")
h_1PXN_normal.Draw()

s_X_normal.Add(h_reco1PXN_true1P0N_normal)
s_X_normal.Add(h_reco1PXN_true1P1N_normal)
s_X_normal.Add(h_reco1PXN_true1PXN_normal)
s_X_normal.Add(h_reco1PXN_true3P_normal)
s_X_normal.Draw("same")

c13leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c13leg.SetBorderSize(0)
c13leg.SetFillColor(0)
c13leg.SetTextFont(62)
c13leg.SetTextSize(0.050)

RMS1P0Nn=h_reco1PXN_true1P0N_normal.GetRMS()-h_reco1PXN_true1P0N_normal.GetRMS()%0.001
RMS1PXNn=h_reco1PXN_true1P1N_normal.GetRMS()-h_reco1PXN_true1P1N_normal.GetRMS()%0.001
RMS1PXNn=h_reco1PXN_true1PXN_normal.GetRMS()-h_reco1PXN_true1PXN_normal.GetRMS()%0.001
RMS3Pn=h_reco1PXN_true3P_normal.GetRMS()-h_reco1PXN_true3P_normal.GetRMS()%0.001
RMSnorm_1PXN=h_1PXN_normal.GetRMS()-h_1PXN_normal.GetRMS()%0.001
c13leg.AddEntry("h_1PXN_normal","All Reco "+str(RMSnorm_1PXN),"lpf")
c13leg.AddEntry("h_reco1PXN_true1P0N_normal","true 1PON "+str(RMS1P0Nn),"lpf")
c13leg.AddEntry("h_reco1PXN_true1P1N_normal","true 1PXN "+str(RMS1P1Nn),"lpf")
c13leg.AddEntry("h_reco1PXN_true1PXN_normal","true 1PXN "+str(RMS1PXNn),"lpf")
c13leg.AddEntry("h_reco1PXN_true3P_normal","true 3prong "+str(RMS3Pn),"lpf")
c13leg.Draw()

c14=ROOT.TCanvas("1PXN loosened")
s_X_loosened=ROOT.THStack("s_X_loosened","loosened cell based")

h_1PXN_loosened.Draw()

s_X_loosened.Add(h_reco1PXN_true1P0N_loosened)
s_X_loosened.Add(h_reco1PXN_true1P1N_loosened)
s_X_loosened.Add(h_reco1PXN_true1PXN_loosened)
s_X_loosened.Add(h_reco1PXN_true3P_loosened)
s_X_loosened.Draw("same")


c14leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c14leg.SetBorderSize(0)
c14leg.SetFillColor(0)
c14leg.SetTextFont(62)
c14leg.SetTextSize(0.050)

RMS1P0Nl=h_reco1PXN_true1P0N_loosened.GetRMS()-h_reco1PXN_true1P0N_loosened.GetRMS()%0.001
RMS1PXNl=h_reco1PXN_true1P1N_loosened.GetRMS()-h_reco1PXN_true1P1N_loosened.GetRMS()%0.001
RMS1PXNl=h_reco1PXN_true1PXN_loosened.GetRMS()-h_reco1PXN_true1PXN_loosened.GetRMS()%0.001
RMS3Pl=h_reco1PXN_true3P_loosened.GetRMS()-h_reco1PXN_true3P_loosened.GetRMS()%0.001
RMSloose_1PXN=h_1PXN_loosened.GetRMS()-h_1PXN_loosened.GetRMS()%0.001
c14leg.AddEntry("h_1PXN_loosened","All reco "+str(RMSloose_1PXN),"lpf")
c14leg.AddEntry("h_reco1PXN_true1P0N_loosened","1PON "+str(RMS1P0Nl),"lpf")
c14leg.AddEntry("h_reco1PXN_true1P1N_loosened","1PXN "+str(RMS1P1Nl),"lpf")
c14leg.AddEntry("h_reco1PXN_true1PXN_loosened","1PXN "+str(RMS1PXNl),"lpf")
c14leg.AddEntry("h_reco1PXN_true3P_loosened","3prong "+str(RMS3Pl),"lpf")
c14leg.Draw()


c15=ROOT.TCanvas("1PXN classification conserved")
s_X_cons=ROOT.THStack("s_X_cons","cons cell based")

h_1PXN_cons.Draw()
s_X_cons.Add(h_reco1PXN_true1P0N_cons)
s_X_cons.Add(h_reco1PXN_true1P1N_cons)
s_X_cons.Add(h_reco1PXN_true1PXN_cons)
s_X_cons.Add(h_reco1PXN_true3P_cons)
s_X_cons.Draw("same")


c15leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c15leg.SetBorderSize(0)
c15leg.SetFillColor(0)
c15leg.SetTextFont(62)
c15leg.SetTextSize(0.050)

RMS1P0Nc=h_reco1PXN_true1P0N_cons.GetRMS()-h_reco1PXN_true1P0N_cons.GetRMS()%0.001
RMS1P1Nc=h_reco1PXN_true1P1N_cons.GetRMS()-h_reco1PXN_true1P1N_cons.GetRMS()%0.001
RMS1PXNc=h_reco1PXN_true1PXN_cons.GetRMS()-h_reco1PXN_true1PXN_cons.GetRMS()%0.001
RMS3Pc=h_reco1PXN_true3P_cons.GetRMS()-h_reco1PXN_true3P_cons.GetRMS()%0.001
RMScons_1PXN=h_1PXN_cons.GetRMS()-h_1PXN_cons.GetRMS()%0.001
c15leg.AddEntry("h_1PXN_cons","all Reco "+str(RMScons_1PXN),"lpf")
c15leg.AddEntry("h_reco1PXN_true1P0N_cons","1PON "+str(RMS1P0Nc),"lpf")
c15leg.AddEntry("h_reco1PXN_true1P1N_cons","1P1N "+str(RMS1P1Nc),"lpf")
c15leg.AddEntry("h_reco1PXN_true1PXN_cons","1PXN "+str(RMS1PXNc),"lpf")
c15leg.AddEntry("h_reco1PXN_true3P_cons","3prong "+str(RMS3Pc),"lpf")
c15leg.Draw()

c16=ROOT.TCanvas("1PXN public")
s_X_public=ROOT.THStack("s_X_public","public cell based")

h_1PXN_public.Draw()

s_X_public.Add(h_reco1PXN_true1P0N_public)
s_X_public.Add(h_reco1PXN_true1P1N_public)
s_X_public.Add(h_reco1PXN_true1PXN_public)
s_X_public.Add(h_reco1PXN_true3P_public)
s_X_public.Draw("same")

c16leg=ROOT.TLegend(0.58,0.42,0.86,0.88)
c16leg.SetBorderSize(0)
c16leg.SetFillColor(0)
c16leg.SetTextFont(62)
c16leg.SetTextSize(0.050)
RMS1PXNp=h_reco1PXN_true1P1N_public.GetRMS()-h_reco1PXN_true1P1N_public.GetRMS()%0.001
RMS1P0Np=h_reco1PXN_true1P0N_public.GetRMS()-h_reco1PXN_true1P0N_public.GetRMS()%0.001
RMS1PXNp=h_reco1PXN_true1PXN_public.GetRMS()-h_reco1PXN_true1PXN_public.GetRMS()%0.001
RMS3Pp=h_reco1PXN_true3P_public.GetRMS()-h_reco1PXN_true3P_public.GetRMS()%0.001
RMSpublic=h_1PXN_public.GetRMS()-h_1PXN_public.GetRMS()%0.001

c16leg.AddEntry("h_1PXN_public","All reco "+str(RMSpublic),"lpf")
c16leg.AddEntry("h_reco1PXN_true1P0N_public","1PON "+str(RMS1P0Np),"lpf")
c16leg.AddEntry("h_reco1PXN_true1P1N_public","1P1N "+str(RMS1P1Np),"lpf")
c16leg.AddEntry("h_reco1PXN_true1PXN_public","1PXN "+str(RMS1PXNp),"lpf")
c16leg.AddEntry("h_reco1PXN_true3P_public","3prong "+str(RMS3Pp),"lpf")
c16leg.Draw()

