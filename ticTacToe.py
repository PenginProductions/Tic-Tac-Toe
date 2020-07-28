## Robert Giglio III
## 9/24/2016
##
## Tic Tac Toe Game
## Plays the game of tic-tac-toe against an AI
   
# constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Display game instructions."""  
    print(
    """
              Welcome to Tic-Tac-Toe!!!
        This will be between you and the computer.  

You will make your move known by entering a number, 0 - 8.  The number 
will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

Prepare yourself....The ultimate battle is about to begin. \n
    """
    )


def ask_yes_no(question):
    """Ask a yes or no question."""
    answer = None
    while answer not in ("y", "n"):
        answer = input(question).lower()
    return answer


def ask_number(question, low, high):
    """Ask for a number within a range."""
    answer = None
    while answer not in range(low, high):
        answer = int(input(question))
    return answer


def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Would you care to go first? (y/n): ")
    if go_first == "y":
        print("\nOkay, then you'll be 'X'.")
        human = X
        computer = O
    else:
        print("\nOkay, then you'll be 'O'.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    """Get human move."""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied....Please choose another.\n")
    print("Alright...")
    return move


def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I will choose square number", end=" ")
    
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
    
    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checkin this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("It seems as though the computer has won.\n\nBetter luck next time!")

    elif the_winner == human:
        print("Great Job! You've won!\n")
        print("Play again and see if you can win another time!")

    elif the_winner == TIE:
        print("Well it would seem as though you tied...")
        print("\nYou should try again.")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# start the program
main()
input("\n\nPress the enter key to quit.")
