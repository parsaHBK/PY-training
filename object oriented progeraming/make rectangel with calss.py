class Rectangle:
    def __init__(self,l,w) -> None:
        self.length=l
        self.width=w
    def area(self):
        return self.length * self.width
#make object
r1=Rectangle(l=50,w=10)
#to way to work with area method
print(r1.area())
print(Rectangle.area(r1))