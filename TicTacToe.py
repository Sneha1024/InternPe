import random

# Declare global variable 'board'
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# Declare global variable 'currentP' and initialize it with the string 'X'
currentP = 'X'
winner = None  # No initial value for winner
gameRunning = True

# Print game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)

# Take player input
def playerIp(board):
    i = int(input("Enter a number 1-9: "))
    if i >=1 and i <= 9 and board[i-1] == '-':
        board[i-1] = currentP
    else:
        print("Player has already occupied that position")

# Check win/tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkCol(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print('It is a Tie!')
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkCol(board):
        print(f"The winner is {winner}")
        gameRunning = False

# Switch the player
def switchP():
    global currentP
    if currentP == "X":
        currentP = "O"  # Corrected assignment
    else:
        currentP = "X"

def computer(board):
    while currentP == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchP()



# Main game loop
while gameRunning:
    printBoard(board)
    playerIp(board)
    checkWin()
    checkTie(board)
    switchP()
    #computer(board)
    #checkWin()
   # checkTie(board)
    #currentP = "X"  # Ensuring the player is 'X' before the next turn

#printBoard(board)
