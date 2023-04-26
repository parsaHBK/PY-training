def union_intersection(dc:dict={})->dict:
    """
    a function to return inter section and union on set values
    on dictionary

    """
    if not isinstance(dc,dict):
        raise TypeError("worining!!!input dictionary")
    #catch keys for use default
    key=(list(dc.keys())) 
    uni_inter = {"intersection":set(),"union":set()}
    #put littral keys on default value
    uni_inter["intersection"]=dc[key[0]]
    uni_inter["union"]=dc[key[0]]
    for keys , values in dc.items():
        uni_inter["intersection"]=uni_inter["intersection"].intersection(values)
        uni_inter["union"]=uni_inter["union"].union(values)
    return uni_inter
print(union_intersection({"s1": {1,2,3,4}, "s2":{1,5,7,3}, "s3":{2,1,8,9}}))