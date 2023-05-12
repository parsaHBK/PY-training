from point import point
from color import Color
class Rectangle:
    def __init__(self,lenght,width,point,color) -> None:
        self.lenght=lenght
        self.width=width
        self.corner = point
        self.color=color
    def __repr__(self) -> str:
        return f"Rectangle is:lenght {self.lenght} and width {self.width}and with {self.corner} and rectangle color={self.color}"
rec1=Rectangle(10,20,point(0,0,Color(10,50,60)),Color(30,50,40))
print(rec1)