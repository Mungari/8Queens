import numpy as np
import random

board = np.ndarray((8,8), int)
board.fill(0)
numQueens = 0

def queenPlace(rowT, colT, boardT):
    global numQueens
    for i in range(0, 8):
        boardT[i, colT] = 1
    for s in range(0, 8):
        boardT[rowT, s] = 1
        
    for diag in range(0,8):
        try:
            if(colT - diag < 0):
                pass
            else:
                boardT[rowT + diag, colT - diag] = 1 # leftDown
        except IndexError:
            pass
        try:
            if(colT - diag < 0 or rowT - diag < 0):
                pass
            else:
                boardT[rowT - diag, colT - diag] = 1 # leftUp
        except IndexError:
            pass
        try:
            if(rowT - diag < 0):
                pass
            else:
                boardT[rowT - diag, colT + diag] = 1 # rightUp
        except IndexError:
            pass
            
        try:
            boardT[rowT + diag, colT + diag] = 1 # rightDown
        except IndexError:
            pass
    boardT[rowT , colT] = 2
    numQueens = numQueens + 1
        


        
while(numQueens < 8):
    row = random.randrange(0, 8)
    col = random.randrange(0, 8)
    a = np.isin(board, 0)
    if(a.any()):
        if(board[row, col] == 0):
            queenPlace(row,col,board)
    else:
        print(board)
        board.fill(0)
        numQueens = 0
        print("Hai perso")
        input()


print(board)
input()