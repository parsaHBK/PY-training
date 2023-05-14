from sensor import Sensor
class Heater:
    def __init__(self,temp,temp_car) -> None:
        self.temp=temp
        self.temp_car=temp_car
    def __repr__(self) -> str:
        return f"temperature is : {self.temp}"
    def on (self):
        """when want change temprature
        heater sould on"""
        return "on"
    def off(self):
        """when didnt want change temprature
        heater sould off"""
        return "off"
    def mx(self,temp,temp_car)-> int:
        """find maximom between temp and temp_car"""
        if temp > temp_car:
            return temp
        else:
            return temp_car
    def mn (self,temp,temp_car)-> int:
        """find minimum between temp and temp_car"""
        if temp < temp_car:
            return temp
        else:
            return temp_car
    def temp_changer(self,temp,temp_car)-> int:
        """this method will operations fixing temprature
        with down or up temp of car
        1 defree per the level"""
        if temp_car != temp:
            while True:
                if temp == temp_car:
                    return temp_car
                temp_car=Sensor.send_tempp(self,Heater.mn(self,temp,temp_car),Heater.mx(self,temp,temp_car))
