import os
import time
import random

board = [""," "," "," "," "," "," "," "," "," "]

def print_header():
    print ("""Welcome to Tic Tac Toe!
The board looks like

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
 
To win the game, get three in a line
Good luck!
""")

def print_board():
    print("")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("---|---|---")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("---|---|---")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("")


def is_winner(board,player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
       (board[4] == player and board[5] == player and board[6] == player) or \
       (board[7] == player and board[8] == player and board[9] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[3] == player and board[6] == player and board[9] == player) or \
       (board[1] == player and board[5] == player and board[9] == player) or \
       (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

def get_computer_move(board,player):
    #check for a win
    for i in range(1,10):
        if board[i] == " ":
            board[i] = player
            if is_winner(board,player):
                board[i] = " "
                return i
            else:
                board[i] = " "
    
    #if the center is empty choose that
    if board[5] == " ":
        return 5
    while True:
        move = random.randint(1,9)
        #if the move is blank, go ahead and return, otherwise try again
        if board[move] == " ":
            return move
            break
    return 5
    


print_header()
print_board()

while True:    
    choice = input("Please choose an empty space for X.")
    choice = int(choice)

    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)

    if is_winner(board,"X"):
        print_board()
        print("X wins! Congratulations!")
        break
        
    print_board()

    if is_board_full(board):
        print("Tie!")
        break

    #get player O input
    choice = get_computer_move(board, "O")

    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)

    if is_winner(board,"O"):
        print_board()
        print("O wins!")
        break
        
    print_board()

    if is_board_full(board):
        print("Tie!")
        break


        
    
