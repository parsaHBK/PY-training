DNA = "AAAAATTTTTTCCCGGGGGGTTTGGGGCCCAAAATTTCCGGGATCGTGACTG"
info_DNA={}
for i in DNA:
    info_DNA.setdefault(i,0)
    info_DNA[i]+=1
print(info_DNA)