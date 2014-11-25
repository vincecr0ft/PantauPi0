from ROOT import TH1F, TH2F

class ListoHistos(object):
    def __init__(self,name,plots):
        self.name=name
        self.histos={}
        self.histos['Miss1P0N']=TH1F('Miss1P0N'+name,'Miss1P0N'+name,120,-1.,1.)
        self.histos['Miss1P1N']=TH1F('Miss1P1N'+name,'Miss1P1N'+name,120,-1.,1.)
        self.histos['Miss1PXN']=TH1F('Miss1PXN'+name,'Miss1PXN'+name,120,-1.,1.)
        self.histos['Miss3P0N']=TH1F('Miss3P0N'+name,'Miss3P0N'+name,120,-1.,1.)
        self.histos['Miss3PXN']=TH1F('Miss3PXN'+name,'Miss3PXN'+name,120,-1.,1.)
        self.histos['cellres']=TH1F('cellres'+name,'cellres'+name,41,-1.,1.)
        self.histos['cellbased']=TH1F('cellbased'+name,'cellbased'+name,120,-1.,1.)
        self.histos['PanTau']=TH1F('PanTau'+name,'PanTau'+name,120,-1.,1.)
        self.histos['sumRes']=TH1F('sumRes'+name,'sumRes'+name,120,-1.,1.)
        self.histos['leadRes']=TH1F('leadRes'+name,'leadRes'+name,120,-1.,1.)
        self.histos['1Pneutral']=TH1F('1prong Neutral '+name,'1prong Neutral '+name,120,-1.,1.)
        self.histos['3Pneutral']=TH1F('3prong Neutral '+name,'3prong Neutral '+name,120,-1.,1.)
        self.histos['2D_neutral']=TH2F("neutral"+name,"neutral"+name,20,-1.,1.,4,0.5,4.5)
        for plot in plots:
            self.histos[plot]=TH1F(plot+'_'+name,plot,120,-1.,1.)

#  LocalWords:  histos PXN cellres cellbased
