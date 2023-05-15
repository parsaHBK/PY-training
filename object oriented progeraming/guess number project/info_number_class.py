class Number_info:
    """this class return attribute of numbers
    so if u make a object with this class its will
    calcute attribute"""
    def __init__(self,number) -> None:
        self.number = number
        self.eq_2=self.eq_2(self.number)
        self.eq_3=self.eq_3(self.number)
        self.eq_5=self.eq_5(self.number)
    def __repr__(self) -> str:
        return f"number is : eqal to 2 ({self.eq_2}) and eqaul to 3 ({self.eq_3}) and  equal to 5 ({self.eq_5})"
    def eq_2(self,number):
        if number%2 == 0:
            return "yes"
        else:
            return "no"
    def eq_3(self,number):
        if number%3 == 0 :
            return "yes"
        else:
            return "no"
    def eq_5(self,number):
        if number % 5 == 0:
            return "yes"
        else:
            return "no"