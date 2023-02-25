def pre_hour (salary,hour):
    if(hour>8):
        return print("eror!you work so match")
    else:
        return print("you catch this money you didnt catch wage",hour * salary)
    
time = (float(input("give me you working time: ")))
wage = (float(input("give me your wage per hour: ")))
pre_hour(wage,time)