from color import Color
from heater import Heater
from sensor import Sensor
class Car :
    def __init__(self,color,model,year,temp_car,heater:str) -> None:
        self.color=color
        self.model=model
        self.year=year
        self.temp_car = temp_car
        self.heater = heater
    def __repr__(self) -> str:
        return f"car:Model({self.model}) and color ({self.color}) and years ({self.year}) and heater ({self.heater} and temp_Car ({self.temp_car})"
    def break_car(self):
        """this function if call car will break"""
        return f"the car : {self.model} is use break"
    def set_color(self):
        """this method will change color car"""
        self.color=Color
        return self.color
    def car_temp(self,min,max)-> int:
        """give a temp with minimum and maximum guss
        and use class sensor"""
        self.temp_car=Sensor.send_tempp(self,min,max)
        return self.temp_car
    def set_temp_with_heater(self,temp,temp_car)-> int:
        """set temp with heater in car
        will on or off heater and chagne temperature"""
        self.heater=Heater.on(a)
        temp_car=Heater.temp_changer(a,temp,temp_car)
        self.heater = Heater.off(a)
        return temp_car
a=Car(Color(50,60,10),"BMW",1998,Car.car_temp(Car,12,55),"off")
print(a.set_temp_with_heater(33,a.temp_car))