class Listmodifier:
    def __init__(self,lst) -> None:
        self.lst = lst
    def __repr__(self) -> str:
        return f"list object is : {self.lst}"
    def integer(self):
        """return a list of integers
        the object will not change"""
        temp=[]
        for i in self.lst:
            if isinstance(i,int):
                temp+=[i]
        return temp
    def count(self)-> int:
        """return a number
        memebrs of the list"""
        j=0
        for i in self.lst:
            j+=1
        return j
    def eqaul_numbers(self)-> list:
        """return a list with eqaul numbers
        the object will not change"""
        temp=[]
        for i in self.lst:
            if isinstance(i,int):
                if i % 2 == 0:
                    temp +=[i]
        return temp
    def change_member(self,index,member)-> list:
        """change the index of memebr on list
        the object will change"""
        self.lst[index]=member
        return self.lst
    def remove_index(self,index)-> list:
        """remove the elemnt on list with index number
        the object will change"""
        temp = []
        for i in range(0,self.count()):
            if i == index:
                continue
            temp.append(self.lst[i])
        self.lst = temp
        return self.lst
    def clear(self):
        """remove evry of memebrs list
        object will empety list"""
        self.lst=[]
        return self.lst
a=Listmodifier([1,2,3,4,313,2,"11","abc",2,5])
print(a.change_member(4,5))
print(a.count())
print(a.remove_index(2))
print(a.eqaul_numbers())
print(a.integer())
