peaple = int(input("how many peaple do u have ?"))
i = int(1)
while(i<=peaple):
    print(i,end=' ')
    age = int(input("peaple:"))
    if(i == 1):
        old = age ; young = age
    if(old < age):
        old = age
    elif(young > age):
        young = age
    i+=1
print("oldes peaple is :",old,"\nyoungest pleaple is :",young)