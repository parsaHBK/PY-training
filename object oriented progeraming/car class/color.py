class Color:
    def __init__(self,red,green,blue) -> None:
        self.red=red
        self.green=green
        self.blue=blue
    def __repr__(self) -> str:
        return f"red:{self.red} green:{self.green} and blue:{self.blue}"
    def setblue(self,blue):
        self.blue=blue
    def setred(self,red):
        self.red=red
    def setgreen(self,green):
        self.green=green
c=Color(10,5,6)