from ROOT import TLorentzVector as TLV

class Tau(object):
    matched=False
    res=-10.
    cellP=-10
    cellN=-10
    nClusters=-10.
    trueP=-10
    trueN=-10
    ExoticFlag=False
    PanTauFlag=False
    BDTloose=False
    BDTmedium=False
    BDTtight=False
    BDTnone=True
    trueTau=TLV(0.,0.,0.,0.)
    trueSum=0.
    trueLead=0.
    cellSum=0.
    cellLead=0.
    cuts={}
    def __init__(self,cellTau):
        self.pt=cellTau.Pt()
        self.eta=cellTau.Eta()
        self.phi=cellTau.Phi()
        self.m=cellTau.M()
    def AddTau(self,name,cutTau,res,nPi0,neutralSum,neutralLead):
        self.cuts[name]={'vector':TLV(cutTau.Pt(),cutTau.Eta(),cutTau.Phi(),cutTau.M()),'res':res,'nPi0':nPi0,'neutralSum':neutralSum,'neutralLead':neutralLead}

