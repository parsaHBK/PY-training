old = int(0)
old_2 = int(0)
rep = int(0)
print("quide!!for end program use (age < 0)")
while(True):
    rep+=1
    print(rep,' ',end='')
    age = int(input("age: "))
    if(age<0):
        break
    if(old_2 < age):
        old_2 = age
    if(old < age):
        old_2 = old
        old = age
print(old,' ', old_2)

