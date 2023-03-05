'''
Enter number of rows:5
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * * 
    * * * * *
     * * * *
      * * *
       * *
        *
'''
rows = int(input("Enter number of rows:"))
space = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, space):
        print(end=" ")
    space = space - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

space = rows - 2

for i in range(rows, -1, -1):
    for j in range(space, 0, -1):
        print(end=" ")
    space = space + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")