number = (int(input("give your number to know its prime or not:")))
i = 1
flag = 0
resault = 0
while (i<int(number)):
    resault = number % i
    if(resault == 0):
        flag +=1
    if(flag > 1):
        print("your number is not prime!!")
        break
    i+=1
if(flag == 1):
    print("your number is prime!!")