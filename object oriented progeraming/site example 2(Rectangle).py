class Rectangle:
    def __init__(self,width,length) -> None:
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        return f"Rectangle with width = {self.width} and  height = {self.length}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other,Rectangle):
            return self.area == other.area

    def __gt__(self,other):
        if isinstance(other,Rectangle):
            return self.width > other.width
    
    def area(self):
            return (self.width*self.length)
    
    def perimeter(self):
        return ((self.length + self.width) * 2)
    
class Square(Rectangle):

    def __init__(self, width,) -> None:
        self.width = width

    def __repr__(self) -> str:
        return f"Square with width = {self.width}"
    
r1 = Rectangle(10,20)
print(r1)
print(r1.area())
print(r1.perimeter())
r2 = Rectangle(10,10)
print(r1==r2)
print(r1 > r2)
s = Square(5)
print(s)