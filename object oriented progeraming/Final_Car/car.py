from heater import Heater
class Car:
    def __init__(self,color:str,model:str,year:int) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.heater= Heater()
    def change_temprute(self,temprute):
        self.heater.change_tempurate(temprute)
bmw=Car("black","BMW",1990)
bmw.change_temprute(15)

        