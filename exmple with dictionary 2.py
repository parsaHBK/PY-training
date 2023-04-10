numbers = [ 1,2,4,4,3,2,1,2,"a","a","b","a"]
dc = {}
for i in numbers:
    dc.setdefault(i ,0)
for i in numbers:
    if i in dc:
        dc[i]+=1
print(dc)   
#secend way 
dc_2={}
for i in numbers:
    dc_2.setdefault(i ,0)
    dc_2[i]+=1
print(dc_2)