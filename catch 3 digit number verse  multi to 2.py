number = (int(input("pelase use your tree digits number:")))

digit_1=number % 10
number = int(number / 10)
digit_2=number % 10
number = int(number / 10)
digit_3=number % 10
number = int(number / 10)

new_number=(digit_1*100)+(digit_2*10)+(digit_3*1)
print("new number is:",new_number*2)