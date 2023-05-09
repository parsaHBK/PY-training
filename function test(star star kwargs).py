def test (**kwargs)-> float:
    """return a dictionary
    and can input a kay word with value
    like test(a=200,b=300)
    test this function with example avrage
    """
    resault = 0
    rep = 0
    for key,value in kwargs.items():
        resault+=value
        rep+=1
    return resault/rep
    """SECEND WAY
    return sum(kwargs.values())/len(kwargs.values())"""
print(test(a=200,b=500))