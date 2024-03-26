class List_Modifire:
    lst_int = list()
    def __init__(self,lst = list) -> None:
        self.lst = lst

    def __repr__(self) -> str:
        return f"list is : {self.lst}"
    
    def Int_mem (self):
        """return integer list from main list
        and nothing will happend for main list"""
        int_lst = list()
        for i in self.lst:
            if isinstance(i,int):
                int_lst.append(i)
        return int_lst
    
    def Str_mem (self):
        """retrun a string list from main list
        and will not anything hapeend for main list"""
        str_lst = list()
        for i in self.lst:
            if isinstance(i,str):
                str_lst.append(i)
        return str_lst
    
    def Lst_mem(self):
        """return a list from main list
        and main list will not editing"""
        lst_lst = list()
        for i in self.lst:
            if isinstance(i,list):
                lst_lst.append(i)
        return lst_lst
    
    def Mem(self):
        """yield evry single member from list"""
        for i in self.lst:
            yield i

l = List_Modifire([2,23,4,"z",234,"c",23,'33',"fdasd","2231",[1,2,3,4,"33213"],[2,3,[2,3]]])
print (l)

for i in l.Mem():
    print(i)