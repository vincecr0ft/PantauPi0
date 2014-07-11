from ROOT import TFile
from ROOT import gDirectory
from ROOT import TH1F,TCanvas,THStack,TLorentzVector
from ROOT import gROOT
import PyCintex
gROOT.ProcessLine('.L rdict.so')


################################################################################
def isGoodDaughter(status, barcode, vxbarcode):
    if((status==2)): return True  # accept all stat==2 daughters
    if( ( status < 200 ) and ( status > 190 )): return True   # for AlpgenJimmy (accept daughters with 190 < stat < 200 )
    # accept daughters with status code 1,1001,2001,... and 1002,2002,... etc if barcode is not too high
    if( ( ( status%1000 == 1) or  (status%1000 == 2 and status > 1000) or (status==2 and vxbarcode<-200000)) and (barcode<200000) ): return True 
    return False 
################################################################################


class Tau(object):
   matched=False
   res=-1
   prong=0
   trueProng=0
   neutrals=0
   def __init__(self,pt,eta,phi,m):
      self.pt=pt
      self.eta=eta
      self.phi=phi
      self.m=m
   def match(self,truept,trueeta,truephi):
       dEta=abs(self.eta-trueeta)
       dPhi=abs(self.phi-truephi)
       dR=(dEta**2 + dPhi**2)**2
       if dR<0.4:
           self.matched=True
           self.res=(self.pt-truept)/truept
#           print "matching %d with %d"%(self.pt,truept)
   def classify(self,nProng,trueProng):
      self.prong=nProng
      self.trueProng=trueProng


class TrueTau(Tau):
   isGood=True

   def __init__(self,pt,eta,phi,m):
      self.pt=pt
      self.eta=eta
      self.phi=phi
      self.m=m
   def childSum(self,pt,eta,phi,m,pdgid,stat,barcode,vxcode):
       existing=TLorentzVector(self.pt,self.eta,self.phi,self.m)
       if abs(pdgid) in [15,13,11]:
           self.isGood=False #skip leptonic decays
       elif abs(pdgid) in [111,311,221,223,130,310]:
           self.neutrals+=1
       elif abs(pdgid) in [211,321,323]:
           self.trueProng+=1

       if self.isGood and isGoodDaughter(stat,barcode,vxcode) and abs(pdgid) not in [12,14,16]:
           new=TLorentzVector(pt,eta,phi,m)
           existing+=new
           self.pt=existing.Pt()
           self.eta=existing.Eta()
           self.phi=existing.Phi()
           self.m=existing.M()
         

   


# Open files
infile = TFile('../pier/ntuples/user.mhodgkin.006921.TauPERF._00344.root')

# retrieve the ntuple of interest
ch = gDirectory.Get( 'tau' )

ch.SetBranchStatus("*",0)
ch.SetBranchStatus("mc_*",1)
ch.SetBranchStatus("tau_*",1)
ch.SetBranchStatus("trueTau_*",1)
ch.SetBranchStatus("EventNumber",1)


entries = ch.GetEntriesFast()
number_of_pairs=0





#define outputs
output = TFile('resolutionHistos.root','RECREATE')
h_oneP = TH1F( 'h_oneP', 'Resolution of all one prong recos', 50, -1., 1. )
h_onePnot = TH1F( 'h_onePnot', 'Resolution of incorrect 1p', 50, -1., 1. )
h_onePone = TH1F( 'h_onePone', 'Resolution of Correct 1p1p', 50, -1., 1. )

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


# get true Vis vector
   mc_taus=[]
   trueVis=[]
   for i in range(ch.mc_n):
       if ch.mc_pdgId[i]==15 and ch.mc_child_index[i].size()>2:
           mc_taus.append(i)
   for i in mc_taus:
       thisTrueTau=TrueTau(0,0,0,0)
       for cc in range(ch.mc_child_index[i].size()):
           cIdx=ch.mc_child_index[i][cc]
           thisTrueTau.childSum(ch.mc_pt[cIdx],ch.mc_eta[cIdx],ch.mc_phi[cIdx],ch.mc_m[cIdx],ch.mc_pdgId[cIdx],ch.mc_status[cIdx],ch.mc_barcode[cIdx],ch.mc_vx_barcode[cIdx])
       if thisTrueTau.isGood:
           trueVis.append(thisTrueTau)




#loop over taus
   cellTaus=[]
   for i in range(ch.tau_n):
      thisTau=Tau(ch.tau_pantau_CellBased_final_pt[i],ch.tau_pantau_CellBased_final_eta[i],ch.tau_pantau_CellBased_final_phi[i],ch.tau_pantau_CellBased_final_m[i])
      for trueTau in trueVis:
          thisTau.match(trueTau.pt,trueTau.eta,trueTau.phi)
          if thisTau.matched:
              thisTau.classify(ch.tau_nProng[i],trueTau.trueProng)
          if thisTau.matched and thisTau.prong==1:
              cellTaus.append(thisTau)
              h_oneP.Fill(thisTau.res)
          if thisTau.trueProng!=1:
              h_onePnot.Fill(thisTau.res)
          else:
              h_onePone.Fill(thisTau.res)



   if jentry%100==0:
      print "I\'m at event %s " %(jentry)


c=TCanvas()

h_oneP.Draw()
h_onePnot.SetFillColor(2)
h_onePone.SetFillColor(38)
h_onePnot.SetFillStyle(3017)
h_onePone.SetFillStyle(3004)

stack=THStack()
stack.Add(h_onePone)
stack.Add(h_onePnot)
stack.Draw("same")


c.Write()
output.Write()
output.Close()
