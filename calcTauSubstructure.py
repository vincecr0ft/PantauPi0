#!/usr/bin/env python

########################################################################################################
# Calculating Tau objects from Substructure informations
#
# use in conjunction with Tau Class and tauRes.py
#
# Author: Vince Croft, June 2014
########################################################################################################


import sys
import os

import ROOT

from ROOT import gROOT, TFile, TTree
from ROOT import gDirectory
from TauClass import Tau
from CutGrid import CutList

###################################################################################
def pi0Cut(BDTScore,eta,nProng,shift):
    if nProng==1:
        if(abs(eta) < 0.8):
            if(BDTScore < 0.46 + shift):return False
        elif(abs(eta) < 1.4):
            if(BDTScore< 0.39 + shift):return False
        elif(abs(eta) < 1.5):
            if(BDTScore< + 0.51 + shift): return False
        elif(abs(eta) < 1.9):
            if(BDTScore < 0.47 + shift): return False
        elif(abs(eta) < 9.9):
            if(BDTScore < 0.54 + shift): return False
    elif nProng==3:
        if(abs(eta) < 0.8):
            if(BDTScore < +0.47 + shift): return False
        elif(abs(eta) < 1.4):
            if(BDTScore < +0.52 + shift): return False
        elif(abs(eta) < 1.5):
            if(BDTScore < +0.60 + shift): return False
        elif(abs(eta) < 1.9):
            if(BDTScore < +0.55 + shift): return False
        elif(abs(eta) < 9.9):
            if(BDTScore < +0.50 + shift): return False 
    if shift<-1: print "shift me sideways with a pitchfork like %f"%shift
    return True

###################################################################################

def ptCut(pt,eta,shift):

    if(abs(eta) < 0.8):
        if(pt < 2100 - shift):return False
    elif(abs(eta) < 1.4):
        if(pt< 2500 - shift):return False
    elif(abs(eta) < 1.5):
        if(pt< + 2600 - shift): return False
    elif(abs(eta) < 1.9):
        if(pt < 2400 - shift): return False
    elif(abs(eta) < 9.9):
        if(pt < 1900 - shift): return False


    return True

###################################################################################


def TauSubstruct(ch):
    tau_n = ch.tau_n
    cellTaus=[]
    
    #loop over all taus
    for i in range(0,tau_n):
        #initialise Tau

        cellPt=ch.tau_pi0Bonn_visTau_pt[i]
        cellEta=ch.tau_pi0Bonn_visTau_eta[i]
        cellPhi=ch.tau_pi0Bonn_visTau_phi[i]
        cellBased = ROOT.TLorentzVector(0.,0.,0.,0.)
        cellBased.SetPtEtaPhiM(cellPt, cellEta,cellPhi,0.,)
        cellTau=Tau(cellBased)
        



        if ch.tau_pantau_CellBased_RecoModePanTau==4:cellTau.PanTauFlag==True
        if ch.tau_JetBDTSigTight[i]>0:cellTau.BDTtight=True
        if ch.tau_JetBDTSigMedium[i]>0:cellTau.BDTmedium=True
        if ch.tau_JetBDTSigLoose[i]>0:cellTau.BDTloose=True

        #truth Match
        trueTau = ROOT.TLorentzVector(0., 0.,0.,0.,)
        for j in range(0,ch.trueTau_n):
            truePt=ch.trueTau_vis_Et[j]
            trueEta=ch.trueTau_vis_eta[j]
            truePhi=ch.trueTau_vis_phi[j]
            trueM=ch.trueTau_vis_m[j]
            trueTauCand=ROOT.TLorentzVector(0.,0.,0.,0.)
            trueTauCand.SetPtEtaPhiM(truePt,trueEta,truePhi,trueM)
            if cellBased.DeltaR(trueTauCand)<0.2:
                cellTau.matched=True
                cellTau.res=((cellBased.Pt()-trueTauCand.Pt())/trueTauCand.Pt())
                cellTau.trueTau=trueTauCand
                cellTau.trueP=ch.trueTau_nProng[j]
                cellTau.trueN=ch.trueTau_nPi0[j]
                trueTau=trueTauCand
        if cellTau.matched==False or cellTau.pt<15000 or abs(cellTau.eta)>2.5: continue

        # create TLV for 4vec sum (all + visible)    
        axis =ROOT.TLorentzVector(0.,0.,0.,0.)
        axis.SetPtEtaPhiM(ch.tau_pt[i],ch.tau_calcVars_interAxis_eta[i],ch.tau_calcVars_interAxis_phi[i],0.)
        chargedSum = ROOT.TLorentzVector(0., 0.,0.,0.,)
        for neutralPt in ch.tau_pi0Bonn_pi0_pt[i]:
            if neutralPt>cellTau.cellLead:cellTau.cellLead=neutralPt
        cellTau.cellSum=ch.tau_pi0Bonn_sumPi0_pt[i]
        nProng=0
        nPi0=0


        if len(ch.tau_pi0Bonn_pi0_pt[i])==1 and abs(ch.tau_pi0Bonn_sumPi0_pt[i]-neutralPt)>5:
            print ch.tau_pi0Bonn_pi0_pt[i]," ",neutralPT

        # add charged EFOs 
        nProng=len(ch.tau_pantau_CellBased_ChargedEFOs_pt[i])

        for j in range(0,nProng):
            chargedCluster=ROOT.TLorentzVector(0.,0.,0.,0.)
            chargedCluster.SetPtEtaPhiM(ch.tau_pantau_CellBased_ChargedEFOs_pt[i][j],ch.tau_pantau_CellBased_ChargedEFOs_eta[i][j],ch.tau_pantau_CellBased_ChargedEFOs_phi[i][j],0.)
            if chargedCluster.DeltaR(axis)<0.2: chargedSum+=chargedCluster
            else: print "cutting spurious track ",chargedCluster.DeltaR(axis)

        # now we have visible Pt, Et, etc. for this tau

        cellTau.cellP=nProng
        cellTau.cellN=ch.tau_pi0Bonn_nPi0[i]        #this should equal nPi0 test later

        #now start adding cuts AddTau(name,cutTau,res,neutralSum,neutralLeadPt)
        cuts=CutList()
        
        #start loop
        for cut in cuts:
            cellSum = ROOT.TLorentzVector(0., 0.,0.,0.,)
            neutralSum = ROOT.TLorentzVector(0., 0.,0.,0.,)
            neutralLead=0.
            nPi0=0.
        #Get number of neutrals
            for j in range(0,ch.tau_pi0Bonn_Pi0Cluster_pt[i].size()):
                BDTScore=ch.tau_pi0Bonn_Pi0Cluster_BDTScore[i][j]
                pt=ch.tau_pi0Bonn_Pi0Cluster_pt[i][j]
                eta=ch.tau_pi0Bonn_Pi0Cluster_eta[i][j]
                phi=ch.tau_pi0Bonn_Pi0Cluster_phi[i][j]
                m=135.
                #public case
                if cut["BDTvalue"]<-1 and ptCut(pt,eta,cut["Cutvalue"]): 
                    nPi0+=1
                    neutralCluster=ROOT.TLorentzVector(0.,0.,0.,0.)
                    neutralCluster.SetPtEtaPhiM(pt,eta,phi,m)
                    if neutralCluster.DeltaR(axis)<0.2:
                        neutralSum+=neutralCluster
                        if neutralCluster.Pt()>neutralLead:neutralLead=neutralCluster.Pt()

                #normal case
                elif cut["BDTvalue"]>-1 and pi0Cut(BDTScore,eta,nProng,cut["BDTvalue"]) and ptCut(pt,eta,cut["Cutvalue"]): 
                    nPi0+=1
                    neutralCluster=ROOT.TLorentzVector(0.,0.,0.,0.)
                    neutralCluster.SetPtEtaPhiM(pt,eta,phi,m)
                    if neutralCluster.DeltaR(axis)<0.2:
                        neutralSum+=neutralCluster
                        if neutralCluster.Pt()>neutralLead:neutralLead=neutralCluster.Pt()
            cellSum=neutralSum+chargedSum               #should equal cellTau.Pt() must test
            res=(cellSum.Pt()-trueTau.Pt())/trueTau.Pt()
            cellTau.AddTau(cut["name"],cellSum,res,nPi0,neutralSum.Pt(),neutralLead)
            if nPi0==1 and abs(neutralSum.Pt()-neutralLead)>5:
                print cut['name'],' gives error: ',neutralSum.Pt(),' ',neutralLead
        #add this cellTau to list of taus            
        cellTaus.append(cellTau)


        
    #end tau loop
    return cellTaus
#end method
############################################################
"""
                

        pi0s=[]
        #loop over neturals to add to pi0s
        for j in range(0,ch.tau_pi0Bonn_Pi0Cluster_pt[i].size()):
            BDTScore=ch.tau_pi0Bonn_Pi0Cluster_BDTScore[i][j]
            pt=ch.tau_pi0Bonn_Pi0Cluster_pt[i][j]
            eta=ch.tau_pi0Bonn_Pi0Cluster_eta[i][j]

            #regular cuts
            if flux>-1 and flux<1 and pi0Cut(BDTScore,eta,nProng,flux) and ptCut(pt,eta,Cutvalue):
                neutralCluster=ROOT.TLorentzVector(ch.tau_pi0Bonn_Pi0Cluster_pt[i][j],ch.tau_pi0Bonn_Pi0Cluster_eta[i][j],ch.tau_pi0Bonn_Pi0Cluster_phi[i][j],0)
                pi0s.append(neutralCluster)
            #public
            elif flux<-1 and ptCut(pt,eta,Cutvalue):
                neutralCluster=ROOT.TLorentzVector(ch.tau_pi0Bonn_Pi0Cluster_pt[i][j],ch.tau_pi0Bonn_Pi0Cluster_eta[i][j],ch.tau_pi0Bonn_Pi0Cluster_phi[i][j],0)
                pi0s.append(neutralCluster)

        nClusters=len(pi0s)



        #get neutral EFOs
        EFOs=[]
        for j in range(0,ch.tau_pantau_CellBased_NeutralEFOs_pt[i].size()):
            EFOs.append(ROOT.TLorentzVector(ch.tau_pantau_CellBased_NeutralEFOs_pt[i][j],ch.tau_pantau_CellBased_NeutralEFOs_eta[i][j],ch.tau_pantau_CellBased_NeutralEFOs_phi[i][j],0.))


        #Get EFO closest to pi0
        for pi0 in pi0s:
            minDeltaR=10.
            minDeltaPt=10000000.
            for EFO in EFOs:
                if pi0.DeltaR(EFO)<minDeltaR and abs(pi0.Pt()-EFO.Pt())<minDeltaPt:
                    minDeltaR=pi0.DeltaR(EFO)
                    minDeltaPt = abs(pi0.Pt()-EFO.Pt())
                    neutralCluster=EFO
                    EFOs.remove(EFO)
            #add closest to vectors
            cellSum+=neutralCluster
            neutralSum+=neutralCluster
            #if highest pt make it lead
            if neutralCluster.Pt()>neutralLead.Pt():neutralLead=neutralCluster
"""
