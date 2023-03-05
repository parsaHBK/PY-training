number = int (input("number for stars pattern:"))
for i in range (0, number):
    for j in range(0,i+1):
        print("*",end='')
    print()
for a in range (number-1,0,-1):
    for b in range (a,0,-1):
        print("*",end='')
    print()