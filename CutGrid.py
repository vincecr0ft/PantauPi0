def CutList():
    a={"name":"Normal-Normal","BDTvalue":0.0,"Cutvalue":0.0} 
    b={"name":"Loose-Normal","BDTvalue":-0.25,"Cutvalue":0.0} 
    c={"name":"ExtraLoose-Normal","BDTvalue":-0.5,"Cutvalue":0.0} 
    d={"name":"Public-Normal","BDTvalue":-2.0,"Cutvalue":0.0} 
    e={"name":"Tight-Normal","BDTvalue":0.25,"Cutvalue":0.0} 
     
    f={"name":"Normal-Loose","BDTvalue":0.0,"Cutvalue":250} 
    g={"name":"Loose-Loose","BDTvalue":-0.25,"Cutvalue":250} 
    h={"name":"ExtraLoose-Loose","BDTvalue":-0.5,"Cutvalue":250} 
    i={"name":"Public-Loose","BDTvalue":-2,"Cutvalue":250} 
    j={"name":"Tight-Loose","BDTvalue":0.25,"Cutvalue":250} 
    
    k={"name":"Normal-Looser","BDTvalue":0.0,"Cutvalue":500} 
    l={"name":"Loose-Looser","BDTvalue":-0.25,"Cutvalue":500} 
    m={"name":"ExtraLoose-Looser","BDTvalue":-0.5,"Cutvalue":500} 
    n={"name":"Public-Looser","BDTvalue":-2,"Cutvalue":500} 
    o={"name":"Tight-Looser","BDTvalue":0.25,"Cutvalue":500} 

    p={"name":"Normal-ExtraLoose","BDTvalue":0.0,"Cutvalue":1000} 
    q={"name":"Loose-ExtraLoose","BDTvalue":-0.25,"Cutvalue":1000} 
    r={"name":"ExtraLoose-ExtraLoose","BDTvalue":-0.5,"Cutvalue":1000} 
    s={"name":"Public-ExtraLoose","BDTvalue":-2,"Cutvalue":1000} 
    t={"name":"Tight-ExtraLoose","BDTvalue":0.25,"Cutvalue":1000} 
    
    u={"name":"Normal-Tight","BDTvalue":0.0,"Cutvalue":-250} 
    v={"name":"Loose-Tight","BDTvalue":-0.25,"Cutvalue":-250} 
    w={"name":"ExtraLoose-Tight","BDTvalue":-0.5,"Cutvalue":-250} 
    x={"name":"Public-Tight","BDTvalue":-2,"Cutvalue":-250} 
    y={"name":"Tight-Tight","BDTvalue":0.25,"Cutvalue":-250} 


#cuts=
    return [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y]