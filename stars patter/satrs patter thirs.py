"""
      *
     **
    ***
   ****
  *****
 ******
*******
"""

number = int(input("stars patter row:"))
space = number
#use outer for loop for rows
for i in range (0,number):
    #use inner for loop 1 for sapce before stars
    for j in range(0,space):
        print(" ",end='')
    #use inner for loop 2 for clumns / stars
    for a in range(0,i+1):
        print("*",end='')
    #decrese space after loop stars drowing complet(importent)
    space-=1
    #use space after one row
    print()