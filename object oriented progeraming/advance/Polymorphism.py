class Circle:
    def __init__(self,r) -> None:
        self.r = r
    
    def area(self):
        return self.r**2*3.14
    
class Square:
    def __init__(self,s) -> None:
        self.s = s
    
    def area(self):
        return self.s**2

c1 = Circle(6)
s1 = Square(4)
for o in (c1,s1):
    print(o.area())