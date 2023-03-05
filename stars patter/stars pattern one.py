""""
*
**
***
****
*****
******
*******
********
*********

"""
number = int(input("stars patter row:"))
#use outer for loop for rows
for i in range (0,number):
    #use inner for loop clumns / stars
    for j in range(0,i+1):
        #print stars for each row
        print("*",end='')
    #end on line after each row
    print()