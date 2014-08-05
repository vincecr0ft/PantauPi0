#!/usr/bin/env python

##########################################################################################################
# small example script how to run over TauD3PDs and calculate visible 4-vector for taus using mc_ branch
#
# use: python calcTauVisibleSum.py D3PD.root
#
# Author: Felix Friedrich, May 2012
##########################################################################################################


import sys
import os
import ROOT
ROOT.gROOT.SetBatch(True)

from ROOT import gROOT, TFile, TTree
from ROOT import gDirectory
from TauClass import Tau

# use this to access vector<vector<int> > (see end of this file)
import PyCintex
#gROOT.ProcessLine('.L /afs/cern.ch/user/v/vcroft/portal/pyTau/PantauPi0/rdict.so')


###################################################################################
def isGoodDaughter(status, barcode, vxbarcode):
    if((status==2)): return True  # accept all stat==2 daughters
    if( ( status < 200 ) and ( status > 190 )): return True   # for AlpgenJimmy (accept daughters with 190 < stat < 200 )
    # accept daughters with status code 1,1001,2001,... and 1002,2002,... etc if barcode is not too high
    if( ( ( status%1000 == 1) or  (status%1000 == 2 and status > 1000) or (status==2 and vxbarcode<-200000)) and (barcode<200000) ): return True 
    return False 
    

###################################################################################
def TauDecayMC(ch):
    mc_n = ch.mc_n
    visTaus=[]
    for i in range(0,mc_n):
        
        pdgId= ch.mc_pdgId[i]
        stat = ch.mc_status[i]

        # only use taus
        if abs(pdgId)!=15: continue
        
        # skip taus with no/1 child only
        if ch.mc_child_index[i].size()<2: continue

        # skip taus which have a tau as child
        # skip leptonic taus
        doSkip=False
        for cc in range(0,ch.mc_child_index[i].size()):
            cIdx = ch.mc_child_index[i][cc]
            if abs(ch.mc_pdgId[cIdx])==15 or abs(ch.mc_pdgId[cIdx])==11 or abs(ch.mc_pdgId[cIdx])==13:
                doSkip=True
                break
        if doSkip: continue 

        # create TLV for 4vec sum (all + visible)    
        visSum = ROOT.TLorentzVector(0., 0.,0.,0.,)

        nProng=0
        nPi0=0
        # loop on childrens
        for cc in range(0,ch.mc_child_index[i].size()):
            # get index of child inside mc_ collection
            cIdx = ch.mc_child_index[i][cc]

            # create TLV
            c_TLV = ROOT.TLorentzVector(0., 0.,0.,0.,)
            c_TLV.SetPtEtaPhiM( ch.mc_pt[cIdx], ch.mc_eta[cIdx],ch.mc_phi[cIdx], ch.mc_m[cIdx] )

            c_pdgId   = ch.mc_pdgId[cIdx]
            c_stat    = ch.mc_status[cIdx]
            c_barcode = ch.mc_barcode[cIdx]
            c_vxcode  = ch.mc_vx_barcode[cIdx]

            # skip bad children
            if not isGoodDaughter(c_stat, c_barcode, c_vxcode):continue

            # count
            if abs(c_pdgId) in [111,311,221,223,130,310]:
                nPi0+=1
            elif abs(c_pdgId) in [211,321,323]:
                nProng+=1

                
            # skip neutrinos 
            if abs(c_pdgId) in [12,14,16]:
                continue

            # use remaining children for visible 4vec
            visSum+=c_TLV
        # end children loop

        # now we have visible Pt, Et, etc. for this tau
        visTau=Tau(visSum.Pt(),visSum.Eta(),visSum.Phi(),visSum.M())
        visTau.trueP=nProng
        visTau.trueN=nPi0
        visTaus.append(visTau)
        
    #end mc loop
    return visTaus
#end method
############################################################
