from info_number_class import Number_info
from random import randrange
from user_inputs import Number
data_saver = list()
def make_number(min,max):
    """this function will make number and make object with number info class
    and jujing with attribute number_info and user_ number
    i need attribute to find faster number"""
    user_number = Number.give_object(Number)
    while(True):
        ansewr = randrange(min,max)
        #bottem line will add evry single of number is create on list to make sure we havent repeated number and save data of numbers
        data_saver.append(ansewr)
        rand_number=Number_info(ansewr)
        if user_number.eq_2 != rand_number.eq_2 and user_number.eq_2 != "idk":
            continue
        if user_number.eq_3 != rand_number.eq_3 and user_number.eq_3 != "idk":
            continue
        if user_number.eq_5 != rand_number.eq_5 and user_number.eq_5 != "idk":
            continue
        if  data_saver.count(ansewr)>1:
            continue
        print(ansewr)
        temp = input("your number is (bigger) or (smaller) or ansewr is (find) !!!use keywords:(bigger,smaller,find)")
        if temp == "bigger":
            min = ansewr
        elif temp == "smaller":
            max = ansewr
        elif temp == "find":
            print("We find number: ",ansewr)
            break
        elif temp =="quit":
            print("your game is end!!")
            break
        else:
            continue
def make_number_pc(min,max):
    """this function will call
    when pc want create a number 
    and use will guesse"""
    rand_number = randrange(min,max)
    num = Number_info(rand_number)
    print(num)
    while(True):
        number_use=int(input("use your number:"))
        if number_use == rand_number:
            print(f"you win number is find!!!well played")
            break
        if number_use > rand_number:
            print("use smaller number!")
        elif number_use < rand_number:
            print("use bigger number")