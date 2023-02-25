def ratio (number= int):
    score = (float)
    i=0
    resault = 0
    while (i < number):
        score = (float(input("put your score:")))
        resault = resault + score 
        i += 1
    return print("your ratio is: ",resault/number)

number = (int(input("how many score do u want catch ratio? ")))
ratio(number)