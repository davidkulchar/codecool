def drawBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def instuctions() :
    print(' ' + "1" + ' | ' + "2" + ' | ' + "3")
    print('-----------')
    print(' ' + "4" + ' | ' + "5" + ' | ' + "6")
    print('-----------')
    print(' ' + "7" + ' | ' + "8" + ' | ' + "9")
    print("Choose one of these spots to mark it!")

def askForMark():
    player1 = ""
    while not (player1 == "X" or player1 == "O"):
        player1 = input("Choose X or O for player1: ").upper()
   
    return player1

def playerStep(board, currentPlayer):
    step = ""
    isFree = False
    while not isFree:
        while not step in '1 2 3 4 5 6 7 8 9'.split():
            step = input("What is your next move? (1-9)")
        step = int(step)
        isFree = isFreeSpot(board, step)
    board[step] = currentPlayer

def isFreeSpot(board, step):
    return board[step] == ' '

def switchPlayer(currentPlayer):
    if currentPlayer == 'X':
        return 'O'
    else:
        return 'X'

def isWin(board, currentPlayer):
    if board[1] == currentPlayer and board[2] == currentPlayer and board[3] == currentPlayer:
        win(currentPlayer, board)
        return True

    if board[4] == currentPlayer and board[5] == currentPlayer and board[6] == currentPlayer:
        win(currentPlayer, board)
        return True

    if board[7] == currentPlayer and board[8] == currentPlayer and board[9] == currentPlayer:
        win(currentPlayer, board)
        return True

    if board[1] == currentPlayer and board[4] == currentPlayer and board[7] == currentPlayer: 
        win(currentPlayer, board)
        return True

    if board[2] == currentPlayer and board[5] == currentPlayer and board[8] == currentPlayer:
        win(currentPlayer, board)
        return True

    if board[3] == currentPlayer and board[6] == currentPlayer and board[9] == currentPlayer: 
        win(currentPlayer, board)
        return True

    if board[1] == currentPlayer and board[5] == currentPlayer and board[9] == currentPlayer:
        win(currentPlayer, board)
        return True

    if board[3] == currentPlayer and board[5] == currentPlayer and board[7] == currentPlayer:
        win(currentPlayer, board)
        return True
    
    else:
        return False

def win(currentPlayer, board):
    drawBoard(board)
    print ("\nThe Winner is:", currentPlayer, "\n")

def isBoardFull(board):
    for i in range(1,10):
        if isFreeSpot(board, i):                         
            return False
    return True

def isTie(board):
    drawBoard(board)
    print ("\nThe game is tie! \n")
    
def isGameOver(board, currentPlayer):
    if isWin(board, currentPlayer) == True:
        return True
    elif isBoardFull(board) == True:
        isTie(board)
        return True
    return False
   
def startGame():
    print ("****************")
    print ("Welcome in X-s and O-s")
    print ("****************")
    board = [' ']* 10
    instuctions()
    currentPlayer = askForMark()
    while not isGameOver(board, currentPlayer):
        drawBoard(board)
        playerStep(board, currentPlayer)
        if not isGameOver(board, currentPlayer):
            currentPlayer = switchPlayer(currentPlayer)
        elif isGameOver(board, currentPlayer):
            break

startGame()