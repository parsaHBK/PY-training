st = "wqnffqw@@##!!!???dwqwdwq??!!!@@??oqwfbdwqd"
finder = "#!?@"
resaul = set ()
for i in st:
    if i in finder:
        resaul.add(i)
print (resaul)
#secend way wiht method intersection
resault_2=set(st).intersection(set(finder))
print(resault_2)
