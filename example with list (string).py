a = "qwqdwuiqgwfwegpagu@#fewfw!!dqwo?dwq?!"
car = []
for i in a:
    if (i == "@" or i == "#" or i == "!" or i == "?"):
        car.append(i)
        #car +=i
print("list car:",car[0:len(car)])