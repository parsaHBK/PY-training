class Car:
    def __init__(self,color:str,model:str,year:int) -> None:
        self.color = self.input_color()
        self.model = model
        self.year = year
    def __repr__(self) -> str:
        return f"Car attribute is : Model : {self.model} and Year : {self.year} Coler : {self .color}"
    def input_color(self,red:int,green:int,blue: int):
        self.color = f"(Red : {red} Green : {green} Blue : {blue})"

car=Car("blue","BMW",1990)
print(car)
