def avrage (lst:list=[])->float:
    """return avrag of list """
    avrage = 0
    for i in lst :
        avrage +=i
    return avrage / len(lst)

def avrage_dic(dic:dict={})->dict:
    """
    a function to give avrage of litrral of dictonirary keys
    and return one dictury
    i find 3 way to my function work
    and i add like comment if u want antoher way
    u can remove coment
    """
    #resault = 0
    avg_dic={}
    for keys , littral in dic.items():
        avg_dic[keys+"_avrage"]=avrage(littral)
        #avg_dic.update({keys:avrage(littral)})
        """for i in littral:
            resault +=i
        avg_dic[keys+"_avrage"]=resault / len(littral)
        resault = 0"""
    return avg_dic
print(avrage_dic({"l1":[1, 2, 3, 5], "l2":[2, 3, 6, 1], "l3":[3, 7, 8, 9]}))
