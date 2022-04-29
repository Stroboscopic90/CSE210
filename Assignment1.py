""""
Assignment 1

1. I need a board 3X3 Board
2. I need two players to  input their  moves.
3. Players must alternate  or flick  play.
4. I need a function to check the win condition. 
      A .  Either  3 XXX  OR  3 OOO  in a row 
      B .  Either   3 XXX  OR  3 OOO   in  A column 
      C    Either   3 XXX  OR 3 OOO  in a Diagonal
      D    All other  condition I will regard as stale mate. Players must replay.
5. The  Blank |   |  will  represent ant empty slot that  the player must fill in. with and X or an O .
Tic Tac Toe Board
The  Board is a 3X3.
There are 9  position that a player can in put.

References : 

You Tube  Videos
Coding Dojo. wwww.codingdojo.com
https://geekflare.com/tic-tac-toe-python-code/
https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
I -learn Code. 



# ************************************  TIC TAC TOE************************************"""

#Function (Method) to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")# \t is a tab key in python
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))# Objects
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')#print the horizontal line s of the board

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD @ BYU Idaho       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")

# Function to check if any player has won
def check_win(player_pos, cur_player):

    # All possible winning combinations
    solution_to_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for x in solution_to_win:
        if all(y in player_pos[cur_player] for y in x):

            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False

# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False

# Function for a single game of Tic Tac Toe
def single_game(cur_player):

    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) # input from player converted to a number(integer)
        except ValueError:# If its not a number  print the below statement
            print("Wrong Input!!! Try Again")
            continue

        # Check the moves 
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Occupied. Try again!!")
            continue

        # Update game information

        # Updating grid status 
        values[move-1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
if __name__ == "__main__": # Main function 

# section 1   Welcome Players to the game and personalize it with their names.
#  welcome the  players to the game
# have them enter their names to make it more personal 
    print("************************     Welcome to BYU -I Tic Tac Toe   *********************")
    player1 = input("Player 1: Please Enter your Name:  " )
    player2 = input("Player 2: Please Enter your name : " ) 
    print()
    print(f"{player1} Your moves are represented by <X>")
    print()
    print(f"{player2},Your moves are respresented by <O>")
    print()
    print("              ^^^^^^^^^^^^^^^    Its a BATTLE of the GIANTS ^^^^^^^^^^^^^^^^^^^^^")
    print()
    print(f"------------ {player1}   OF  BYU IDAHO ENGINEERING ------ VERSUS -----------{player2}-------OF BYU-PROVO COMPUTER SCIENCE" )
    print()
    print("```````````````````````````````Let the Battle Begin``````````````````````````````````")
    # Stores the player who chooses X and O
    cur_player = player1 or player2  # for current player

    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board) # call the  pprint scoreboard function

    # The loop runs until the players quit
    while True:

        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1: # If  player choses X then O is  player 2
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1: # If player 1  2 then  he is the X player
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:# if 3 is  entered  It will print score board  and  break out
            print("Final Scores")
            print_scoreboard(score_board)
            break
        else:
            print("Wrong Choice!!!! Try Again\n")# If any other value other than 1,2 or 3 is enter  code will print this

        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])

        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

