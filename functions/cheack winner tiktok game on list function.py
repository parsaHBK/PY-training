def cheack_winner(tic_tac: list=[["","",""],["","",""],["","",""]])-> str:
    """the funccti0on catch a list tic tac game
    and return winner or havent winner
    """
    temp_l=""
    temp_c=""
    temp_g=""
    temp_g_2=""
    for i in range(0,3):
        for j in range(0,3):
            temp_l+=tic_tac[i][j]
            temp_c+=tic_tac[j][i]
            if (i==0 and j==2)or(i==1 and j==1)or(i==2 and j==0):
                temp_g_2+=tic_tac[i][j]
            if i==j:
                temp_g+=tic_tac[i][j]
        if temp_l =="OOO" or temp_g == "OOO" or temp_g == "OOO" or temp_g_2=="OOO":
            return "O"
        elif temp_l=="XXX" or temp_g == "XXX" or temp_g == "XXX"or temp_g_2=="XXX":
            return "X"
        temp_l=""
        temp_c=""
    return"no winner"
l=[["X","O",""],
   ["O","X","O"],
   ["","O","X"]]
print(cheack_winner(l))