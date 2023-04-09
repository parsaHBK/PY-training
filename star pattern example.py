rep=int(input("number of pattern rep:"))
for i in range(0,rep):
    for j in range (0,i+1):
        print("*",end="")
    print() 
for i in range(rep-1,0,-1):   
    for j in range(0,i):
        print("*",end="")
    print()
    