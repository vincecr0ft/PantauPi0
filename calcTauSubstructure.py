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
def deltaR(eta1,eta2,phi1,phi2):
    dEta=eta1-eta2
    dPhi=phi1-phi2
    return (dEta*dEta+dPhi*dPhi)**0.5

def pi0Cut(BDTScore,eta,nProng,flux):
    if nProng==1:
        if(abs(eta) < 0.8):
            if(BDTScore < -0.06 + flux):return False
        elif(abs(eta) < 1.4):
            if(BDTScore< -0.14 + flux):return False
        elif(abs(eta) < 1.5):
            if(BDTScore< + 0.01 + flux): return False
        elif(abs(eta) < 1.9):
            if(BDTScore < -0.10 + flux): return False
        elif(abs(eta) < 9.9):
            if(BDTScore < -0.01 + flux): return False
    elif nProng==3:
        if(abs(eta) < 0.8):
            if(BDTScore < +0.43 + flux): return False
        elif(abs(eta) < 1.4):
            if(BDTScore < +0.51 + flux): return False
        elif(abs(eta) < 1.5):
            if(BDTScore < +0.48 + flux): return False
        elif(abs(eta) < 1.9):
            if(BDTScore < +0.66 + flux): return False
        elif(abs(eta) < 9.9):
            if(BDTScore < +0.65 + flux): return False 

    return True

###################################################################################
def TauSubstruct(ch,flux):
    tau_n = ch.tau_n
    cellTaus=[]
    for i in range(0,tau_n):
        
        # create TLV for 4vec sum (all + visible)    
        cellSum = ROOT.TLorentzVector(0., 0.,0.,0.,)
        nProng=0
        nPi0=0
        
        # add charged EFOs 
        nProng=ch.tau_pantau_CellBased_ChargedEFOs_pt[i].size()

        for j in range(0,nProng):
            chargedCluster=ROOT.TLorentzVector(0.,0.,0.,0.)
            chargedCluster.SetPtEtaPhiM(ch.tau_pantau_CellBased_ChargedEFOs_pt[i][j],ch.tau_pantau_CellBased_ChargedEFOs_eta[i][j],ch.tau_pantau_CellBased_ChargedEFOs_phi[i][j],ch.tau_pantau_CellBased_ChargedEFOs_m[i][j])

            cellSum+=chargedCluster
        pi0s=[]
        for j in range(0,ch.tau_pi0Bonn_Pi0Cluster_pt[i].size()):
            BDTScore=ch.tau_pi0Bonn_Pi0Cluster_BDTScore[i][j]
            eta=ch.tau_pi0Bonn_Pi0Cluster_eta[i][j]
            if pi0Cut(BDTScore,eta,nProng,flux):
                neutralCluster=ROOT.TLorentzVector(ch.tau_pi0Bonn_Pi0Cluster_pt[i][j],ch.tau_pi0Bonn_Pi0Cluster_eta[i][j],ch.tau_pi0Bonn_Pi0Cluster_phi[i][j],ch.tau_pi0Bonn_Pi0Cluster_E[i][j])
                pi0s.append(neutralCluster)
        nPi0=len(pi0s)
        for pi0 in pi0s:
            neutralCluster=ROOT.TLorentzVector(0.,0.,0.,0.)
            minDeltaR=10.
            minDeltaPt=10000.
            for j in range(0,ch.tau_pantau_CellBased_NeutralEFOs_pt[i].size()):
                thisCluster=ROOT.TLorentzVector(ch.tau_pantau_CellBased_NeutralEFOs_pt[i][j],ch.tau_pantau_CellBased_NeutralEFOs_eta[i][j],ch.tau_pantau_CellBased_NeutralEFOs_phi[i][j],ch.tau_pantau_CellBased_NeutralEFOs_m[i][j])

                if deltaR(pi0.Eta(),thisCluster.Eta(),pi0.Phi(),thisCluster.Phi())<minDeltaR and abs(pi0.Pt()-thisCluster.Pt())<minDeltaPt:
                    minDeltaR=deltaR(pi0.Eta(),thisCluster.Eta(),pi0.Phi(),thisCluster.Phi())
                    minDeltaPt = abs(pi0.Pt()-thisCluster.Pt())
                    
                    neutralCluster=thisCluster
                    


                cellSum+=neutralCluster

        # now we have visible Pt, Et, etc. for this tau
        cellTau=Tau(cellSum.Pt(),cellSum.Eta(),cellSum.Phi(),cellSum.M())
        cellTau.cellP=nProng
        cellTau.cellN=nPi0
        cellTaus.append(cellTau)



    #end tau loop
    return cellTaus
#end method
############################################################
