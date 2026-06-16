#This is the bad code version of a tic-tac-toe program
#Author: Gavin Binkley
#Date: 6/16/26
print("welcome to Tic Tac Toe")
print("This program may later include online multiplayer, score tracking, colors, AI, and Tournaments")
print("None of these features are actually included right now.")

def show_board():
    global a, b, c, d, e, f, g, h, i
    print()
    print(a + " | " + b + " | " + c)
    print("--+---+--")
    print(d + " | " + e + " | " + f)
    print("--+---+--")
    print(g + " | " + h + " | " + i)
    print()

def player_x_turn():
    print("Player X Turn")
    global a, b, c, d, e, f, g, h, i
    spot = input("Player X, choose a spot 1-9: ")
    if spot == "1" and a == "1":
        a = "X"
    elif spot == "2" and b == "2":
        b = "X"
    elif spot == "3" and c == "3":
        c = "X"
    elif spot == "4" and d == "4":
        d = "X"
    elif spot == "5" and e == "5":
        e = "X"
    elif spot == "6" and f == "6":
        f = "X"
    elif spot == "7" and g == "7":
        g = "X"
    elif spot == "8" and h == "8":
        h = "X"
    elif spot == "9" and i == "9":
        i = "X"
    else:
        print("That spot is taken or invalid. You lose your turn.")



def player_o_turn():
    print("Player O Turn")
    global a, b, c, d, e, f, g, h, i
    spot = input("Player O, choose a spot 1-9: ")

    if spot == "1" and a == "1":
        a = "O"
    elif spot == "2" and b == "2":
        b = "O"
    elif spot == "3" and c == "3":
        c = "O"
    elif spot == "4" and d == "4":
        d = "O"
    elif spot == "5" and e == "5":
        e = "O"
    elif spot == "6" and f == "6":
        f = "O"
    elif spot == "7" and g == "7":
        g = "O"
    elif spot == "8" and h == "8":
        h = "O"
    elif spot == "9" and i == "9":
        i = "O"
    else:
        print("That spot is taken or invalid. You lose your turn.")


def check_stuff():
    global a, b, c, d, e, f, g, h, i

    if a == "X" and b == "X" and c == "X":
        print("X wins!")
        quit()
    if d == "X" and e == "X" and f == "X":
        print("X wins!")
        quit()
    if g == "X" and h == "X" and i == "X":
        print("X wins!")
        quit()
    if a == "X" and d == "X" and g == "X":
        print("X wins!")
        quit()
    if b == "X" and e == "X" and h == "X":
        print("X wins!")
        quit()
    if c == "X" and f == "X" and i == "X":
        print("X wins!")
        quit()
    if a == "X" and e == "X" and i == "X":
        print("X wins!")
        quit()
    if c == "X" and e == "X" and g == "X":
        print("X wins!")
        quit()

    if a == "O" and b == "O" and c == "O":
        print("O wins!")
        quit()
    if d == "O" and e == "O" and f == "O":
        print("O wins!")
        quit()
    if g == "O" and h == "O" and i == "O":
        print("O wins!")
        quit()
    if a == "O" and d == "O" and g == "O":
        print("O wins!")
        quit()
    if b == "O" and e == "O" and h == "O":
        print("O wins!")
        quit()
    if c == "O" and f == "O" and i == "O":
        print("O wins!")
        quit()
    if a == "O" and e == "O" and i == "O":
        print("O wins!")
        quit()
    if c == "O" and e == "O" and g == "O":
        print("O wins!")
        quit()
def useless_future_features():
    print("Maybe one day this will save scores ")
    print("Maybe one day this will have multiplayer")
    print("Maybe one day this will have AI")

a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
f = '6'
g = '7'
h = '8'
i = '9'

show_board()

#Turn #1
player_x_turn()
show_board()
check_stuff()

#Turn #2
player_o_turn()
show_board()
check_stuff()

#Turn #3
player_x_turn()
show_board()
check_stuff()

#Turn #4
player_o_turn()
show_board()
check_stuff()

#Turn #5
player_x_turn()
show_board()
check_stuff()

#Turn #6
player_o_turn()
show_board()
check_stuff()

#Turn #7
player_x_turn()
show_board()
check_stuff()

#Turn #8
player_o_turn()
show_board()
check_stuff()

#Turn #9
player_x_turn()
show_board()
check_stuff()

print('The game is a tie')