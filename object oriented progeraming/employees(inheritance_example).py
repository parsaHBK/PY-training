from random import randint

class Employees:
    def __init__(self,first_name,last_name,age) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.id_cart = Employees.make_id(self)
        self.age = age

    def make_id(self):
        return randint(1,1000)
    
    def __repr__(self) -> str:
        return f"Name = {self.first_name} last name = {self.last_name} age = {self.age} id cart = {self.id_cart}"
    
    def access(self) -> str:
        print ("General access!")
    
class IT_emp(Employees):
    
    def __init__(self, first_name, last_name,age) -> None:
        super().__init__(first_name, last_name, age)
        self.it_code = IT_emp.it_code_maker(self)
    
    def it_code_maker(self):
        return randint(1000,2000)
    
    def __repr__(self) -> str:
        return super().__repr__() + f"  IT CODE = {self.it_code}"

    def access(self) -> str:
        return "It admin access!"
    
e1 = Employees("Ahmad","Abyar",56)
print(e1)
i1 = IT_emp("parsa","abyar",23)
print(i1)
print(i1.access())