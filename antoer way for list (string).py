a = "qwqdwuiqgwfwegpagu@#fewfw!!dqwo?dwq?!"
car = []
car_target = "@!?#"
for i in a:
    if i in car_target:
        car.append(i)
        #car +=i
print("list car:",car[0:len(car)])