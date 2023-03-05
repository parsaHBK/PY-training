"""
***********
**********
*********
********
*******
******
*****
****
***
**
*
"""
number = int(input("stars patter row:"))
#use outer for loop for rows
for i in range(number,0,-1):
    #use inner for loop for clumns / stars
    for j in range (0,i+1):
        #print stars each row
        print("*",end='')
    print()