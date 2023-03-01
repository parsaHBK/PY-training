resault = 0
#for know game lose or win or equal
win = int (0)                    
lose = int (0)
equal = int (0)
#catch how many game have one team
game = int(input("how many game do you play?"))
rep = int (1)
while (rep <= game):
    print(rep,end = ' ')
    score = int(input("game:"))
    if (score == 3):
        win+=1
    elif(score == 1):
        equal+=1
    elif(score == 0):
        lose+=1
    else:
        print("worning!! you put worng number i removed from scorebord")
        rep -= 1
    resault = score + resault
    rep+=1
#for know avrage of score    
avrage = resault/game                
print("your win is:",win,"\nyour lose is:",lose,"\nyour equal is:",equal)