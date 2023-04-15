def odd_equl(numbers_lst:list)->dict:
    if not isinstance(numbers_lst,list):
        raise TypeError("need fix your argoment!")
    show_odd_equal = {"odd":0,"equal":0}
    for i in numbers_lst:
        if i%2==0:
            show_odd_equal["odd"]+=1
        else:
            show_odd_equal["equal"]+=1
    return show_odd_equal
def catch_argoment(size:int=1)->list:
    if not(isinstance(size,int)):
        raise TypeError("need fix your argoment!")
    numbers = list()
    for i in range (0,size):
        print(i+1,"arogment:",end="")
        numbers.append(int(input()))
    return numbers
m_size = int(input("size of argoments:"))
print(odd_equl(catch_argoment(m_size)))

