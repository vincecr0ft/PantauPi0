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

###################################################################################
def pi0Cut(BDTScore,eta,nProng,shift):
    if nProng==1:
        if(abs(eta) < 0.8):
            if(BDTScore < -0.06 + shift):return False
        elif(abs(eta) < 1.4):
            if(BDTScore< -0.14 + shift):return False
        elif(abs(eta) < 1.5):
            if(BDTScore< + 0.01 + shift): return False
        elif(abs(eta) < 1.9):
            if(BDTScore < -0.10 + shift): return False
        elif(abs(eta) < 9.9):
            if(BDTScore < -0.01 + shift): return False
    elif nProng==3:
        if(abs(eta) < 0.8):
            if(BDTScore < +0.43 + shift): return False
        elif(abs(eta) < 1.4):
            if(BDTScore < +0.51 + shift): return False
        elif(abs(eta) < 1.5):
            if(BDTScore < +0.48 + shift): return False
        elif(abs(eta) < 1.9):
            if(BDTScore < +0.66 + shift): return False
        elif(abs(eta) < 9.9):
            if(BDTScore < +0.65 + shift): return False 
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


def TauSubstruct(ch,flux,Cutvalue):
    tau_n = ch.tau_n
    cellTaus=[]
    
    #loop over all taus
    for i in range(0,tau_n):
        # create TLV for 4vec sum (all + visible)    
        cellSum = ROOT.TLorentzVector(0., 0.,0.,0.,)
        neutralSum = ROOT.TLorentzVector(0., 0.,0.,0.,)
        neutralLead = ROOT.TLorentzVector(0., 0.,0.,0.,)
        nProng=0
        nPi0=0
        
        # add charged EFOs 
        nProng=ch.tau_pantau_CellBased_ChargedEFOs_pt[i].size()

        for j in range(0,nProng):
            chargedCluster=ROOT.TLorentzVector(0.,0.,0.,0.)
            chargedCluster.SetPtEtaPhiM(ch.tau_pantau_CellBased_ChargedEFOs_pt[i][j],ch.tau_pantau_CellBased_ChargedEFOs_eta[i][j],ch.tau_pantau_CellBased_ChargedEFOs_phi[i][j],0)

            cellSum+=chargedCluster

        #first get regular number of neutrals
        for j in range(0,ch.tau_pi0Bonn_Pi0Cluster_pt[i].size()):
            BDTScore=ch.tau_pi0Bonn_Pi0Cluster_BDTScore[i][j]
            pt=ch.tau_pi0Bonn_Pi0Cluster_pt[i][j]
            eta=ch.tau_pi0Bonn_Pi0Cluster_eta[i][j]

            if pi0Cut(BDTScore,eta,nProng,0.0) and ptCut(pt,eta,0.0): 
                nPi0+=1
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

            #add closest to vectors
            cellSum+=neutralCluster
            neutralSum+=neutralCluster
            #if highest pt make it lead
            if neutralCluster.Pt()>neutralLead.Pt():neutralLead=neutralCluster
        # now we have visible Pt, Et, etc. for this tau
        cellTau=Tau(cellSum.Pt(),cellSum.Eta(),cellSum.Phi(),0)
        cellTau.cellP=nProng
        cellTau.cellN=nPi0
        cellTau.cellPt=ch.tau_pi0Bonn_visTau_pt[i]

        if nPi0>0:
            cellTau.cellSum=neutralSum.Pt()        
            cellTau.cellLead=neutralLead.Pt()
        if ch.tau_pantau_CellBased_RecoModePanTau==4:cellTau.PanTauFlag==True
        if ch.tau_JetBDTSigTight[i]>0:cellTau.BDTtight=True
        if ch.tau_JetBDTSigMedium[i]>0:cellTau.BDTmedium=True
        if ch.tau_JetBDTSigLoose[i]>0:cellTau.BDTloose=True

        cellTaus.append(cellTau)


    #end tau loop
    return cellTaus
#end method
############################################################
