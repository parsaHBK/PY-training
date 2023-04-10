dc= {
    "group_1":[1,86,3,4,15,6,7,8,9],
    "group_2":[11,22,33,22,11,33,44,]
}
mx={}
for k,v in dc.items():
    #thirds way is simple than evry ways
    #mx.setdefault(k,max(v))    can use this order
    mx.setdefault(k,0)
    for i in v:
        if i > mx[k]:
            mx[k]=i
    #secend way to use function max not need a plus for
    #mx[k]=max(v)
print(mx)