
def golf_scorecard_bot(num: int = int(input("How many players are playing? \n> "))):
    id = 0
    player = {}
    player_score = {}
    score = {}
    current_leader = None

    while id < num:
        id += 1
        player[id] = input("What is the name of player " + str(id) + "? \n> ")
        player_score[id] = int(input("What is the score of player " + str(id) + "? \n> "))
        score[id] = {player[id]: player_score[id]}

    id = 1  # Reset id for the next loop
    while id <= num:
        if current_leader is None or score[id][player[id]] < score[current_leader][player[current_leader]]:
            current_leader = id
        id += 1    
    
    print("The winner is " + str(player[current_leader]) + "!")
        
        
    
golf_scorecard_bot()