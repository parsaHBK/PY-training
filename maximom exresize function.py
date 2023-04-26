def mx_1(number_1:(float)=0.0,number_2:(float)=0.0)->float or int:
    """"
    catch 2 number and return bigest number
    return is float or int
    cath number float or int
    """
    if not isinstance(number_1,(float,int)):
        raise TypeError("worining!!!fix your input than try again")
    if number_1 > number_2:
        return number_1
    elif number_2 > number_1:
        return number_2
    #if my if is not working this number is equal and it will return first number on else
    else:
        return number_1
def mx_2(number_1:(float)=0.0,number_2:(float)=0.0,number_3:(float)=0.0)->float or int:
    """
    catch 3 number and return bigest
    antoher fucntion in this function work
    its name : mx_1
    """
    if not isinstance(number_1,(float,int)):
        raise TypeError("worining!!!fix your input than try again")
    if number_3 > mx_1(number_1,number_2):
        return number_3
    elif mx_1(number_1,number_2)>number_3:
        return mx_1(number_1,number_2)
    #if they ifes not work its will equal than return last number
    else:
        return number_3
print(mx_2(7,12,3.14))