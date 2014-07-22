from ROOT import TFile
from ROOT import gDirectory
from ROOT import TLorentzVector
from ROOT import TH1F,TCanvas
from ROOT import gROOT

from calcTauVisibleSum import TauDecayMC
from calcTauSubstructure import TauSubstruct
from TauClass import Tau

# Open files
infile = TFile('../pier/ntuples/user.mhodgkin.006921.TauPERF._00344.root')


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
h_1p=TH1F('h_1p','resolution of all 1 prong taus',40,-2.,2.)
h_1p1p=TH1F('h_1p1p','resolution of all matched 1 prong taus',40,-2.,2.)
h_3p=TH1F('h_3p','resolution of all 3 prong taus',40,-2.,2.)
h_3p3p=TH1F('h_3p3p','resolution of all matched 3 prong taus',40,-2.,2.)
h_trueprong=TH1F('h_trueprong','number of prongs',10,0.,10.)
h_trueneutrals=TH1F('h_trueneutrals','number of neutrals',10,0.,10.)
h_cellprong=TH1F('h_cellprong','number of prongs',10,0.,10.)
h_cellneutrals=TH1F('h_cellneutrals','number of neutrals',10,0.,10.)

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

            if trueTau.trueP==1:
               h_1p.Fill(res)
               if tau.cellP==1:
                  h_1p1p.Fill(res)
            else:
               h_3p.Fill(res)
               if tau.cellP==3:
                  h_3p3p.Fill(res)

   if jentry%100==0: print "event number",jentry



c=TCanvas()

output.Write()
output.Close()
