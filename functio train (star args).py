def avarage (*args:float)->int:
    resault=0
    rep=0
    for i in args:
        resault+=i
        rep+=1
    return resault/rep
    """secend way
    return sum(args)/len(args)"""
    
print(avarage(1,9))