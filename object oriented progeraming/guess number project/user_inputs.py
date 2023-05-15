from info_number_class import Number_info
def user_input()->object:
    """this function will do it simple
    evry of attribute on user number
    will catch from user and use this fucntion
    to main file"""
    print("Game Guid!!!plese use key word --> (yes)(no)(idk) -->idk : i dont know")
    user_object=Number()
    answer=input("your number % 2 = 0 ?")
    if answer == "yes":
        user_object.eq_2="yes"
    elif answer == "no":
        user_object.eq_2="no"
    else:
        user_object.eq_2="idk"
    answer=input("your number % 3 = 0 ?")
    if answer == "yes":
        user_object.eq_3="yes"
    elif answer == "no":
        user_object.eq_3="no"
    else:
        user_object.eq_3="idk"
    answer=input("your number % 5 = 0 ?")
    if answer == "yes":
        user_object.eq_5="yes"
    elif answer == "no":
        user_object.eq_5="no"
    else:
        user_object.eq_5="idk"
    return user_object
class Number:
    """this class will make a object and return object with method to know
    attribute of number user used
    we will use this attribute and class make number
    to make sure guesse faster"""
    def __init__(self) -> None:
        """make a object with attribute user use"""
        self.eq_2=""
        self.eq_3=""
        self.eq_5=""
    def __repr__(self) -> str:
        return f"eq_2={self.eq_2} and eq_3={self.eq_3} and eq_5= {self.eq_5}"
    def make_object(self):
        return user_input()
    def give_object(self):
        a = user_input()
        return a