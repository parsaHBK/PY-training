def next_number(lst:list[int]=[])->int:
    """acc a list of intger values
    evry elements will uniquie
    evrt elements will bigger than 1 or equal
    """
    nu_1 = True # to know in list we have number 1 or not
    for i in lst:
        if not isinstance(i,int) or i < 1:
            raise TypeError("worning!!!use integer on list and bigger than 1 ")
        if lst.count(i) == 2:
            raise ValueError("worning!!!your values is not uniquie")
        if i == 1:
            nu_1=True      
    if nu_1 == False:
        return 1
    else:
        info_lst = lst.copy()
        info_lst.sort()
        for i in range(0,len(info_lst)+1):
            for j in range(0,len(info_lst)+1):
                i+=1
                if info_lst[i] > info_lst[j]+1:
                    return info_lst[j]+1
l = [1,3,4,2,11,23,10]          
print(next_number(l))