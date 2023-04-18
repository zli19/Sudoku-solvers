import numpy as np
import time

def solve(board):
    find = find_empty(board)
    if find:
        pos = find
    else:
        return True

    for i in range(1,10):
        if isValid(i, pos, board):
            board[pos] = i
            if solve(board):
                return True
            board[pos] = 0
    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def isValid(i, pos, board):
    a = pos[0]//3
    b = pos[1]//3
    if i in np.delete(board[pos[0], :], pos[1]) or i in np.delete(board[:, pos[1]], pos[0]) \
            or i in np.delete(board[3 * a:3 * a + 3, 3 * b:3 * b + 3], 3 * (pos[0] % 3) + (pos[1] % 3)):
        return False
    return True

board = np.array(
    [[0,0,0,0,0,1,0,7,2],
     [3,2,0,0,7,0,0,0,4],
     [6,0,0,0,0,0,0,0,0],
     [7,4,0,0,1,0,0,0,3],
     [0,0,8,0,0,0,0,0,0],
     [0,0,0,5,0,0,9,0,0],
     [0,0,6,0,2,0,0,0,0],
     [2,8,0,0,0,9,3,0,0],
     [0,0,1,0,0,0,0,0,8]]
)


if solve(board):
    print(board)
else:
    print('no solution')

