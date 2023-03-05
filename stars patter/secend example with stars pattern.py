number = int(input("use ure numbers for stas pattern:"))
space = number
for i in range (0,number):
    for j in range (space-1, 0,-1):
        print(" ",end="")
    for a in range (0,i+1):
        print("*",end="")
    print()
    space -=1
for i_2 in range (0,number-1):
    for j_2 in range (0,i_2+1):
        print(" ",end='')
    for a_2 in range (i_2,number-1):
        print("*",end="")
    print()