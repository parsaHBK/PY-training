class Khodru:
    def __init__(self,name,year,color) -> None:
        self.color = color
        self.name = name
        self.year = year
    def harkat(self):
        print (f"Khodru {self.name} be {self.color} dar harkat ast")
    def tormoz(self):
        print ("Tormoz")
class Electricalkhodru(Khodru):
    pass
c =Electricalkhodru("BMW",1999,"black")
c.harkat()
