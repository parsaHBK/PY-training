from color import Color
class point:
    def __init__(self,x,y,color) -> None:
        self.x = x
        self.y = y
        self.size=1
        self.c=color
    def __repr__(self) -> str:
        return f"corner of Rectangle is : x={self.x} and y={self.y} and size={self.size} and color point is: {self.c}"
    def setsize(self,s):
        self.size=s
p=point(0,0,Color(10,50,60))