def sum_positive(lst:list=[])->list:
    """return a integer
    mean plus evry integer > 0  on list
    for exmaple [1,2,3,4,-4,-9]
    it will return = 10"""
    if not isinstance(lst,list):
        raise TypeError("worning!!input a list not other format")
    resault = 0
    for values in lst:
        if values>0:
            resault+=values
    if resault == 0 or len(lst)==0:
        return 0
    return resault
def count_evens(lst:list=[])-> int:
    """a function to catch a list
    and retuern count number % 2 = 0
    the fucntion return zero if list is empty
    """
    if not isinstance(lst,list):
        raise TypeError("worning!!input a list not other format")
    if len(lst)==0:
        return 0
    count=0
    for i in lst:
        if i % 2 == 0:
            count+=1
    return count