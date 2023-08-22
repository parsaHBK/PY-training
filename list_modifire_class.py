class List_modifire:
    def __init__(self,l:list=[]) -> object:
        self.list = l
    def __repr__(self) -> str:
        return f"elements is :{self.list}"
    def count(self):
        count = 0 
        for i in self.list:
            count += 1
        return count
    def integers (self):
        """remove evry element if its not integer"""
        temp  = list()
        for i in self.list:
            if  isinstance(i,int):
                temp.append(i)
        self.list = temp
l = [1,5,2,3,6,4,"dwqd","dwqff","qwe",1.2,1.5]
ob_temp = List_modifire(l)
print(ob_temp)
print(ob_temp.count())
ob_temp.integers()
print(ob_temp)