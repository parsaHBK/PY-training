def eqaul_generator(lst:list=[])->int:
    """
    cath a list and return with yield
    equl number on list
    this function is itration
    """
    for i in lst:
        if i%2==0:
            yield i
def eqaul_non_generator(lst:list=[])->list:
    """this fuction catch a list and return a eqaul list"""
    new_lst=[]
    for i in lst:
        if i % 2 ==0:
            new_lst+=[i]
            #new_lst.append(i)
    return new_lst
    #make with list combaination
    #return [j for j in lst if j%2==0]
for i in eqaul_generator([1,2,3,4,5,6,7,8,10,11,12,13,14]):
    print(i,end='\t')
print()
for i in eqaul_non_generator([1,2,3,4,5,6,7,8,10,11,12,13,14]):
    print(i,end='\t')
