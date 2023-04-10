lst = "wepoqiewognjlekrg@@@!!!!???##dwwqww??@@21!!!ig##"
dc= {}
jug= "@!#?"
for i in lst : 
    if i in jug:
        dc.setdefault(i,0)
        dc[i]+=1
print(dc)