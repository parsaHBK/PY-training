"""
    * 
   * *  
  * * *
 * * * *
* * * * *
"""

number = int(input("stars patter row:"))
space = number
for i in range (0,number):
    for j in range (0,space):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    space -=1
    print()