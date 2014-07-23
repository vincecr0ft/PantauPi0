from ROOT import TH1F

class ListoHistos(object):
    def __init__(self,name):
        self.name=name
        self.h_reco1P1N=TH1F('h_reco1P1N_'+name,'Correctly identified 1p1n taus',40,-2.,2.)
        self.h_reco1P1N_true1P0N=TH1F('h_reco1P1N_true1P0N_'+name,'Reco 1P1N true 1P0N',40,-2.,2.)
        self.h_reco1P1N_true1PXN=TH1F('h_reco1P1N_true1PXN_'+name,'Reco 1P1N true 1PXN',40,-2.,2.)
        self.h_reco1P1N_true3P=TH1F('h_reco1P1N_true3P_'+name,'Reco 1P1N true 3P',40,-2.,2.)

        self.h_3p=TH1F('h_3p_'+name,'Reco 3 prong taus',40,-2.,2.)
        self.h_3p3p=TH1F('h_3p3p_'+name,'Correct reco 3 prong taus',40,-2.,2.)
        self.h_trueprong=TH1F('h_trueprong_'+name,'number of prongs',5,0.,5.)
        self.h_trueneutrals=TH1F('h_trueneutrals_'+name,'number of neutrals',5,0.,5.)
        self.h_cellprong=TH1F('h_cellprong_'+name,'number of prongs',5,0.,5.)
        self.h_cellneutrals=TH1F('h_cellneutrals_'+name,'number of neutrals',5,0.,5.)


