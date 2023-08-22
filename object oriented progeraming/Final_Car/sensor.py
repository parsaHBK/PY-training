from random import randint
class Sensor:
    def car_temp(self):
        temp = randint(5,30)
        print(f"Car temp is {temp}")
        return temp