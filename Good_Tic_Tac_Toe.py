#This is the updated python file with the "good code" that derives from the "bad code"
#Author: Gavin Binkley
#Date: 6/16/26
#from Bad_Tic_Tac_Toe import player_o_turn

print("welcome to Tic Tac Toe")
def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def make_move(board, player):
    while True:
        choice = input(f"Player {player}, choose a spot (1-9): ")

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        position = int(choice) - 1

        if position < 0 or position > 8:
            print("Choose a number between 1 and 9.")
            continue

        if board[position] in ["X", "O"]:
            print("That spot is already taken.")
            continue

        board[position] = player
        break


def check_winner(board):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        if (
            board[combo[0]] ==
            board[combo[1]] ==
            board[combo[2]]
        ):
            return True

    return False


def tic_tac_toe():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"

    for turn in range(9):
        display_board(board)
        make_move(board, current_player)

        if check_winner(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            return

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    display_board(board)
    print("It's a tie!")


tic_tac_toe()