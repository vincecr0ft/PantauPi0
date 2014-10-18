from ROOT import TH1F,TH2F

class ListoHistos(object):
    def __init__(self,name,plots):
        self.name=name
        self.histos={}
        self.histos['Pantau']=TH1F('Pantau'+name,'Pantau'+name,40,-1.,1.)
        self.histos['cellres']=TH1F('cellres'+name,'cellres'+name,41,-1.,1.)
        self.histos['sumRes']=TH1F('sumRes'+name,'sumRes'+name,40,-2.,2.)
        self.histos['leadRes']=TH1F('leadRes'+name,'leadRes'+name,40,-2.,2.)
        self.histos['2D_neutral']=TH2F("neutral"+name,"neutral"+name,40,-1.,1.,4,1,5)
        for plot in plots:
            self.histos[plot]=TH1F(plot+'_'+name,plot,40,-1.,1.)
            self.histos[plot+"_neutral"]=TH1F(plot+'_neutral_'+name,"neutral "+plot,40,-1.,1.)

