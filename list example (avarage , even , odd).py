size = int (input("size:"))
numbers = []
odd = []
even = []
for i in range (0, size ):
    print("number",i+1,":",end="")
    i=int(input())
    numbers.append(i)
    #secend way to catch parametrs for list is bottem its not good for knowing code
    #   numbers += [i]
    if (i%2==0):
        odd.append(i)
    else:
        even.append(i)
print("odd list:",odd[0:len(odd)])
print("even list:",even[0:len(even)])
