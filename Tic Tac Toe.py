#Program will run until someone wins or loses or ends in a draw or given an invalid input.
#Haven't handled exceptions yet
from IPython.display import clear_output
#I'm using this to clear the screen.You can also do this by printing a new line 100 times
#print("\n"*100)
pl1 = []
pl2 = []
replay = True
keepplaying = True
moves =  {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

def check_ans(moves):
    if moves[1] == moves[2] and moves[2] == moves[3] and moves[1] not in " ":
        return "Win"
    elif moves[1] == moves[4] and moves[4] == moves[7] and moves[1] not in " ":
        return "Win"
    elif moves[9] == moves[8] and moves[8] == moves[7] and moves[9] not in " ":
        return "Win"
    elif moves[9] == moves[6] and moves[6] == moves[3] and moves[9] not in " ":
        return "Win"
    elif moves[5] == moves[1] and moves[1] == moves[9] and moves[5] not in " ":
        return "Win"
    elif moves[5] == moves[7] and moves[7] == moves[3] and moves[5] not in " ":
        return "Win"
    elif moves[5] == moves[8] and moves[8] == moves[2] and moves[5] not in " ":
        return "Win"
    elif moves[5] == moves[4] and moves[4] == moves[6] and moves[5] not in " ":
        return "Win"
    elif " " not in moves.values():
        return "Draw"
    else:
        return "None"

def player_turn(player,moves):
    print("Player {}'s turn".format(player[0]))
    place = int(input("Enter place"))
    moves[place] = player[1]


def print_board(moves):
    clear_output()
    print(" {} | {} | {} ".format(moves[7],moves[8],moves[9]))
    print(" {} | {} | {} ".format(moves[4],moves[5],moves[6]))
    print(" {} | {} | {} ".format(moves[1],moves[2],moves[3]))

def play():
    moves =  {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
    pl = input("Player 1 what would you like to be?:").upper()
    if pl=='X':
        pl1 = [1,'X']
        pl2 = [2,'O']
    elif pl == 'O':
        pl1 = [2,'X']
        pl2 = [1,'O']
    else:
        print("Either x or y")
        return 0
    flag = 0
    while keepplaying == True:
        flag += 1
        if flag%2 != 0:
            print_board(moves)
            player_turn(pl1,moves)
            if check_ans(moves) == "Win":
                print_board(moves)
                print("Player {} wins!".format(pl1[0]))
                return True
            elif check_ans(moves) == "Draw":
                print_board(moves)
                print("Draw")
                return True
                
        else:
            print_board(moves)
            player_turn(pl2,moves)
            if check_ans(moves) == "Win":
                print_board(moves)
                print("Player {} wins!".format(pl2[0]))
                return True
            elif check_ans(moves) == "Draw":
                print_board(moves)
                print("Draw")
                return True
                
def playagain(replay):
    print("Do you want to play again?")
    reply = input("Yes or No:").upper()
    if reply == "YES":
        return True
    elif reply == "NO":
        return False

    
    
while replay == True:
    if play():
        replay = playagain(replay)
