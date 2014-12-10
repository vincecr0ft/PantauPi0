from ROOT import TH1F, TH2F

class ListoHistos(object):
    def __init__(self,name,plots):
        self.name=name
        self.histos={}
        self.histos['Miss1P0N']=TH1F('Miss1P0N'+name,'Miss1P0N'+name,101,-1.01,1.01)
        self.histos['Miss1P1N']=TH1F('Miss1P1N'+name,'Miss1P1N'+name,101,-1.01,1.01)
        self.histos['Miss1PXN']=TH1F('Miss1PXN'+name,'Miss1PXN'+name,101,-1.01,1.01)
        self.histos['Miss3P0N']=TH1F('Miss3P0N'+name,'Miss3P0N'+name,101,-1.01,1.01)
        self.histos['Miss3PXN']=TH1F('Miss3PXN'+name,'Miss3PXN'+name,101,-1.01,1.01)
        self.histos['NonMiss']=TH1F('NonMiss'+name,'NonMiss'+name,101,-1.01,1.01)


        self.histos['cellres']=TH1F('cellres'+name,'cellres'+name,41,-1.01,1.01)
        self.histos['cellbased']=TH1F('cellbased'+name,'cellbased'+name,101,-1.01,1.01)
        self.histos['PanTau']=TH1F('PanTau'+name,'PanTau'+name,101,-1.01,1.01)
        self.histos['sumRes']=TH1F('sumRes'+name,'sumRes'+name,101,-1.01,1.01)
        self.histos['leadRes']=TH1F('leadRes'+name,'leadRes'+name,101,-1.01,1.01)
        self.histos['1Pneutral']=TH1F('1prong Neutral '+name,'1prong Neutral '+name,101,-1.01,1.01)
        self.histos['3Pneutral']=TH1F('3prong Neutral '+name,'3prong Neutral '+name,101,-1.01,1.01)
        self.histos['2D_neutral']=TH2F("neutral"+name,"neutral"+name,101,-1.01,1.01,4,0.5,4.5)
        self.histos['PanTau_CellBased']=TH2F("correlation"+name,"correlations"+name,101,-1.01,1.01,101,-1.01,1.01)
        for plot in plots:
            self.histos[plot]=TH1F(plot+'_'+name,plot,101,-1.01,1.01)

#  LocalWords:  histos PXN cellres cellbased
