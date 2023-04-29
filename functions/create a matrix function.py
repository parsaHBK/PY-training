def create_matrix(line:int=0,culomn:int=0)-> list:
    """a function to creat a matrix
    """
    temp=[]
    mtx=[]
    for li in range(0,line):
        for cu in range(0,culomn):
            print("[",li,"]","[",cu,"]","=",end="")
            temp+=(input())
        mtx+=[temp]
        temp=[]
    return mtx
l = int (input("input your line of matrix:"))
c = int(input("input your culomn matrix:"))
mx=create_matrix(l,c)
mx[2][4]=5555