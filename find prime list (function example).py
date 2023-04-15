from math import sqrt
def find_prime(number:int=0)->list:
    """find prime_numbers before number input"""
    if not isinstance(number,int):
        raise TypeError("input integer!!")
    prims=[]
    flag = False
    for k in range(number,2,-1):
        if prime_yes_no(k)==True:
            prims.append(k)
        #if we havent function prime numbers find we can do bottem code
        """if k%2==0:continue
        for i in range(2,k):
            if k%i == 0:
                flag=False
                break
            else:
                flag=True
        if flag == True:
            prims.append(k)"""
    prims.append(2)
    return prims
def prime_yes_no(number:int)->bool:
    """to know number is prime or not"""
    if not isinstance(number,int):
        raise TypeError("input integer!!")
    if number%2==0:
        return False
    for i in range(3,int(sqrt(number))+1,2):
        if number%i==0:
            return False
    return True
main_number = int(input("use ure number for catch prime list:"))
print("your number prime is:",prime_yes_no(main_number))
print("prime numbers before your number:",find_prime(main_number))