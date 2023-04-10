lst = ["ew","eqew","dasdsa","d",1,5,3,69,4,"j",4,"h","h",2112,3]
dc = {
    "str":0, 
    "int":0
}
temp = 0
for i in lst:
    if isinstance(i , str):
        dc["str"]+=1
    elif isinstance(i , int):
        dc["int"]+=1
print("dictory is : ",dc)