
a={"name":"Normal-Normal","BDTvalue":0.0,"Cutvalue":0.0} 
b={"name":"Loose-Normal","BDTvalue":-0.25,"Cutvalue":0.0} 
c={"name":"ExtraLoose-Normal","BDTvalue":-0.5,"Cutvalue":0.0} 
d={"name":"Public-Normal","BDTvalue":-2.0,"Cutvalue":0.0} 

cuts=[a,b,c,d]
bdtcuts=['BDTnone','BDTloose','BDTmedium','BDTtight']

for cut in cuts:
    cut['selection']=bdtcuts

for cut in cuts:
    for bdt in cut['selection']:
        print bdt

print cuts
