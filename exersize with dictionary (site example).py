lst = [{"city":"shiraz",  "pop(million)":1.57, "Area(km^2)":240},
     {"city":"isfahan", "pop(million)":1.96, "Area(km^2)":551},
     {"city":"ahvaz",   "pop(million)":1.18, "Area(km^2)":185},
     {"city":"tabriz",  "pop(million)":1.60, "Area(km^2)":324},
     {"city":"mashhad", "pop(million)":3.00, "Area(km^2)":328}]
max_pop={"citi":"","max(pop)":0}
min_pop={"citi":"","min(pop)":lst[0]["pop(million)"]}
max_area={"citi":"","max(area)":0}
min_area={"citi":"","min(area)":lst[0]["Area(km^2)"]}
for i in lst:
    for key,value in i.items():
        if (key == "pop(million)"):
            if(value>max_pop["max(pop)"]):
                max_pop["citi"]=i["city"]
                max_pop["max(pop)"]=value
            if(value<min_pop["min(pop)"]):
                min_pop["citi"]=i["city"]
                min_pop["min(pop)"]=value
        elif(key == "Area(km^2)"):
            if(value>max_area["max(area)"]):
                max_area["citi"]=i["city"]
                max_area["max(area)"]=value
            if(value<=min_area["min(area)"]):
                min_area["citi"]=i["city"]
                min_area["min(area)"]=value
print("max pop is:",max_pop,"\nmin pop is :",min_pop,"\nmax are is:",max_area,"\nmin are is:",min_area)
#i dont know what is max iteger on py to use on minimom but i thin (1e11) its max
        