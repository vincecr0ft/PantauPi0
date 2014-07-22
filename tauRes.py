from ROOT import TFile
from ROOT import gDirectory
from ROOT import TLorentzVector
from ROOT import TH1F,TCanvas
from ROOT import gROOT

from calcTauVisibleSum import TauDecayMC
from calcTauSubstructure import TauSubstruct
from TauClass import Tau

# Open files
infile = TFile('../../pier/ntuples/user.mhodgkin.006921.TauPERF._00344.root')


# retrieve the ntuple of interest
ch = gDirectory.Get( 'tau' )

ch.SetBranchStatus("*",0)
ch.SetBranchStatus("mc_*",1)
ch.SetBranchStatus("tau_*",1)
ch.SetBranchStatus("tau_*",1)
ch.SetBranchStatus("trueTau_*",1)
ch.SetBranchStatus("EventNumber",1)

entries = ch.GetEntriesFast()

output = TFile('resolutionHistos.root','RECREATE')
h_reco1P1N=TH1F('h_reco1P1N','All reco 1p1n taus',20,-2.,2.)
h_reco1P1N_true1P0N=TH1F('h_reco1P1N_true1P0N','Reco 1P1N true 1P0N',20,-2.,2.)
h_reco1P1N_true1PXN=TH1F('h_reco1P1N_true1PXN','Reco 1P1N true 1PXN',20,-2.,2.)
h_reco1P1N_true3P=TH1F('h_reco1P1N_true3p','Reco 1P1N true 3P',20,-2.,2.)


h_3p=TH1F('h_3p','All 3 prong taus',20,-2.,2.)
h_3p3p=TH1F('h_3p3p','True and reco 3 prong taus',20,-2.,2.)

h_trueprong=TH1F('h_trueprong','number of prongs',5,0.,5.)
h_trueneutrals=TH1F('h_trueneutrals','number of neutrals',5,0.,5.)
h_cellprong=TH1F('h_cellprong','number of prongs',5,0.,5.)
h_cellneutrals=TH1F('h_cellneutrals','number of neutrals',5,0.,5.)

for jentry in xrange( entries ):
 # get the next tree in the ch and verify
   ientry = ch.LoadTree( jentry )
   if ientry < 0:
      break

 # copy next entry into memory and verify
   nb = ch.GetEntry( jentry )
   if nb <= 0:
      continue

 # use the values directly from the tree
   EventNumber = int(ch.EventNumber)
   if EventNumber < 0:
     continue
   

   visTaus=TauDecayMC(ch)
   cellTaus=TauSubstruct(ch)
   for tau in cellTaus:
      for trueTau in visTaus:
         dEta=tau.eta-trueTau.eta
         dPhi=tau.phi-trueTau.phi
         dR=(dEta*dEta+dPhi*dPhi)**0.5

         if dR<0.4:
            
            res=(tau.pt-trueTau.pt)/trueTau.pt
            h_trueneutrals.Fill(trueTau.trueN)
            h_cellneutrals.Fill(tau.cellN)
            h_trueprong.Fill(trueTau.trueP)
            h_cellprong.Fill(tau.cellP)

            if tau.cellP==1 and tau.cellN==1:
               if trueTau.trueP==1:
                  if trueTau.trueN==1:
                     h_reco1P1N.Fill(res)
                  elif trueTau.trueN==0:
                     h_reco1P1N_true1P0N.Fill(res)
                  else:
                     h_reco1P1N_true1PXN.Fill(res)
               else:
                  h_reco1P1N_true3p.Fill(res)

            else:
               h_3p.Fill(res)
               if tau.cellP==3:
                  h_3p3p.Fill(res)

   if jentry%100==0: print "event number",jentry

output.Write()
output.Close()
