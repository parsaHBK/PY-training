def squere_2d(lst:list=[int])-> bool:
    """a function to return
    true or false
    true : if resaqul_line==resault_cloumn
    false: if resault_line!=resault_clumn
    """
    if len(lst)!=len(lst[0]):
        raise ValueError("input worning!!!need squere list -->cloumn and line is eqaul")
    temp_l=0
    temp_c=0
    for i in range(0,len(lst)):
        for j in range(0,len(lst)):
            temp_l+=lst[i][j]
            temp_c+=lst[j][i]
        if temp_c == temp_l:
            return True
        else:
            temp_l=0
            temp_c=0
    return False
ls=[[2,5,6],[3,7,9],[4,2,4]]
print(squere_2d(ls))