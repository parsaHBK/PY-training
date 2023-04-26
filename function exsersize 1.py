def maximom_minimom_len(lst:list=[])->dict:
    """
    catch a list a return a dict
    with key maximom and minimom and len list

    """
    if not isinstance(lst ,list):
        raise TypeError("input list!!!worng inputer")
    info = {"maximom":0,"minimum":1e112,"len":0}
    for i in lst:
        if i > info["maximom"]:
            info["maximom"] = i
        if i < info ["minimum"]:
            info["minimum"]= i
        info["len"] += 1
    return info
print (maximom_minimom_len([1, 2, 3, 6, 2, 43]))

