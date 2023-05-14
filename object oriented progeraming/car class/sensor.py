from random import randint
class Sensor:
    def __init__(self,min,max) -> None:
        self.temp_car = self.send_tempp(min,max)
    def __repr__(self) -> str:
        return f"temp car is : {self.temp_car}"
    def send_tempp(self,min,max):
        """send a temp random number"""
        self.temp_car=randint(min,max)
        return self.temp_car