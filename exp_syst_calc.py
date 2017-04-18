def calc(x):
    ver_var_Teso = {0:0.1, 1:1, 2:1, 5:1, 7:0}
    ver_var_WoW = {0:0.1, 1:1, 3:1, 4:1, 7:0}
    ver_var_Rev = {0:0.5, 1:1, 7:0.8}
    ver_var_BnS = {0:0.3, 1:1, 7:0.7}
    ver_var_EVE = {0:0.1, 1:1, 8:0.6, 7:0}
    ver_var_Lin = {0:0.1, 1:1, 6:1, 7:0.6}
    ver_var_Sky = {0:0.1, 1:1, 6:1, 7:0.5}
    ver_var_All = {0:0.1, 1:1, 6:1, 7:0.4}
    ver_var_Star = {0:0.1, 1:1, 7:0}
    ver_var_Tera = {0:0.1, 1:1, 6:1, 7:0.3}
    for i in range(0,len(x)-1):
        for j in range(0,len(ver_var_Teso)-1):
            if i==list(ver_var_Teso.keys())[j]:
                Teso = x[i]*list(ver_var_Teso.values())[j]
        for k in range(0,len(ver_var_WoW)-1):
            if i==list(ver_var_WoW.keys())[k]:
                WoW = x[i]*list(ver_var_WoW.values())[k]
        for l in range(0,len(ver_var_Rev)-1):
            if i==list(ver_var_Rev.keys())[l]:
                Rev = x[i]*list(ver_var_Rev.values())[l]
        for m in range(0,len(ver_var_BnS)-1):
            if i==list(ver_var_BnS.keys())[m]:
                BnS = x[i]*list(ver_var_BnS.values())[m]
        for n in range(0,len(ver_var_EVE)-1):
            if i==list(ver_var_EVE.keys())[n]:
                EvE = x[i]*list(ver_var_EVE.values())[n]
        for o in range(0,len(ver_var_Lin)-1):
            if i==list(ver_var_Lin.keys())[o]:
                Lin = x[i]*list(ver_var_Lin.values())[o]
        for p in range(0,len(ver_var_Sky)-1):
            if i==list(ver_var_Sky.keys())[p]:
                Sky = x[i]*list(ver_var_Sky.values())[p]
        for q in range(0,len(ver_var_All)-1):
            if i==list(ver_var_All.keys())[q]:
                All = x[i]*list(ver_var_All.values())[q]
        for r in range(0,len(ver_var_Star)-1):
            if i==list(ver_var_Star.keys())[r]:
                Star = x[i]*list(ver_var_Star.values())[r]
        for s in range(0,len(ver_var_Tera)-1):
            if i==list(ver_var_Tera.keys())[s]:
                Tera = x[i]*list(ver_var_Tera.values())[s]
    y=[str(Teso),str(WoW),str(Rev),str(BnS),str(EvE),str(Lin),str(Sky),str(All),str(Star),str(Tera)]
    return y
