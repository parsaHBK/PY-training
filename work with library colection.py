from collections import namedtuple
information_person = namedtuple("person",["name","lastname","work","sex","Age"])
from collections import Counter
st = "egoeeobvriu22233ebe"
print (Counter(st))
print (st.count("g"))
print(Counter(st).most_common)
print (sorted(st))
from collections import OrderedDict
information_person_2 = OrderedDict(name="",lastname="",work="",sex="",age="")
#secend way to work with order dict give velue to list its name kay and make one order dict with method fromkeys
"""keys = ["name","lastname","work","sex","age"]
information_person_2 = OrderedDict.fromkeys(keys,"")"""
#its make a order dictionary like top with kays list
for i in information_person_2:
    print("import value ",i," :",end="")
    #information_person_2[i] = input()
print(information_person_2)

