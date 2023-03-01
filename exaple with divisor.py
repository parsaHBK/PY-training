def divisor (rep = (int)):
    i= int(1)
    count = int(0)
    while (i <= rep):
        if (rep % i == 0):
            count += 1
        i+=1
    return count
div = int(0)
big_number = int (0)
for i in range (0,20):
    print(i+1,' ',end='')
    number = int(input("number:"))  
    if(divisor(number)>div):
        most_div_number = number
        div = divisor(number)
    elif(divisor(number)==div and most_div_number>big_number):
            big_number = most_div_number
print("most have divisor:",big_number,"\ndivisor number is:",div)