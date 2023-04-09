size = int (input("size:"))
numbers = []
odd = []
even = []
for i in range (0, size ):
    print("number",i+1,":",end="")
    a=int(input())
    numbers.append(a)
    if (a%2==0):
        odd.append(a)
    else:
        even.append(a)
print("odd list:",odd[0:len(odd)])
print("even list:",even[0:len(even)])
    
