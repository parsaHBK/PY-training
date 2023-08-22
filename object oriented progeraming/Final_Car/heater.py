from sensor import Sensor
from time import sleep
class Heater :
    def __init__(self) -> None:
        self.car_temp = Sensor.car_temp(self)
    def heater_on (self):
        print("Heater is ON!")
    def heater_off(self):
        print("Heater is OFF!")
    def change_tempurate(self,tempurate):
        self.heater_on()
        if tempurate > self.car_temp:
            while self.car_temp < tempurate:
                sleep(1.2)
                self.car_temp+=1
                print(f"car temp is : {self.car_temp}")
        elif tempurate < self.car_temp:
            while self.car_temp > tempurate:
                sleep(1.2)
                self.car_temp -= 1
                print(f"car temp is : {self.car_temp}")
        self.heater_off()
