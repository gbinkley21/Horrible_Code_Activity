#This is the bad code version of a tic-tac-toe program

print("welcome to Tic Tac Toe")
print("This program may later include online multiplayer, score tracking, colors, AI, and Tournaments")
print("None of these features are actually included right now.")

def show_board():
    global a, b, c, d, e, f, g, h, i
    print(a + " | " + b + " | " + c)
    print("--+---+--")
    print(d + " | " + e + " | " + f)
    print("--+---+--")
    print(g + " | " + h + " | " + i)

def player_x_turn():
    print("Player X Turn")
    spot = input("Player X, choose a spot 1-9: ")
    if spot == '1':
        a = 'X'
    if spot == '2':
        b = 'X'
    if spot == '3':
        c = 'X'
    if spot == '4':
        d = 'X'
    if spot == '5':
        e = 'X'
    if spot == '6':
        f = 'X'
    if spot == '7':
        g = 'X'
    if spot == '8':
        h = 'X'
    if spot == '9':
        i = 'X'



def player_o_turn():
    print("Player Y Turn")
    spot = input("Player Y, choose a spot 1-9: ")
    if spot == '1':
        a = ('O')
    if spot == '2':
        b = 'O'
    if spot == '3':
        c = 'O'
    if spot == '4':
        d = 'O'
    if spot == '5':
        e = 'O'
    if spot == '6':
        f = 'O'
    if spot == '7':
        g = 'O'
    if spot == '8':
        h = 'O'
    if spot == '9':
        i = 'O'


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