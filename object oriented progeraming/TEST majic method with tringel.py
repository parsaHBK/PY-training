class Tringle:
    def __init__(self,height,rule) -> None:
        self.height = height
        self.rule = rule
        self.tringle_cal_counter=0
    #to give feed back from object
    def __repr__(self) -> str:
        return f"Tringle is :height {self.height} and rule {self.rule} and area {self.area()} and primeter {self.primeter()}"
    #for know 2 object is eqaul or not
    def __eq__(self,other: object) -> bool:
        return self.area()==other.area()
    #for know first object area bigger than secend object
    def __gt__(self,other: object)-> bool:
        return self.area()>other.area()
    def area(self):
        self.tringle_cal_counter+=1
        return self.height * self.rule
    def primeter(self):
        self.tringle_cal_counter+=1
        return (self.height * self.rule)/2
def reducer(tr):
    return tr.primeter()*0.1
tr1 = Tringle(10,5)
tr2 = Tringle(15,5)
tr1.tringle_cal_counter