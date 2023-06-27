import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

Currentplayer = "X"
winner = None
gameRunning = True

# print the game board
def printBoard(board):
    print("----------")
    print(board[0] + " | "+ board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | "+ board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | "+ board[7] + " | " + board[8])
    print("----------")

# Take player input
def playerInput(board):
    if not gameRunning:
        return
    inp = int(input("Enter a number between 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = Currentplayer
    else:
        print("Error spot is occupied pick another spot!")

# check for win or a tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] and board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] and board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] and board[8] != "-":
        winner = board[6]
        return True

def CheckVertically(board):
    global winner
    if board[0] == board[3] == board[6] and board [0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board [1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board [2] != "-":
        winner = board[2]
        return True

def CheckDiagnal(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    if '-' not in board:
        printBoard(board)
        print("Please play again. The Game Has Ended In A Tie")
        gameRunning = False


def CheckWin():
    if CheckDiagnal(board) or checkHorizontal(board) or CheckVertically(board):
        printBoard(board)
        print(f"The winner is {winner}")
        global gameRunning
        gameRunning = False

# switch the player

def switchPlayer():
    global Currentplayer
    if Currentplayer == "X":
        Currentplayer = "O"
    else:
        Currentplayer = "X"




while gameRunning:
    printBoard(board)
    playerInput(board)
    CheckWin()
    checkTie(board)
    switchPlayer()
