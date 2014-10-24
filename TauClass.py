from ROOT import TLorentzVector as TLV
class Tau(object):
    matched=False
    res=-10
    cellP=0
    cellN=0
    nClusters=-10
    trueP=0
    trueN=0
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
    def __init__(self,pt,eta,phi,m):
        self.pt=pt
        self.eta=eta
        self.phi=phi
        self.m=m

