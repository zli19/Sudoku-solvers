import numpy as np
import time

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

def get_l(board):
    l = np.array([])
    for i in range(81):
        r = i//9
        c = i % 9
        if board[r,c] != 0:
            l = np.append(l, i)
    return l

def isValid(r,c,num,board):
    a = r//3
    b = c//3
    if num in np.delete(board[r,:], c) or num in np.delete(board[:,c], r) \
            or num in np.delete(board[3*a:3*a+3,3*b:3*b+3], 3*(r%3)+(c%3)):
        return False
    return True

def get_answer(board):
    l = get_l(board)
    i = 0
    while 0 <= i < 81:
        while i in l and i != 80:
            i += 1
        r = i//9
        c = i % 9
        board[r,c] += 1
        while board[r, c] <= 9 and not isValid(r,c,board[r,c],board):
            board[r, c] += 1
        if board[r, c] > 9:
            board[r, c] = 0
            i -= 1
            while i in l and i != 0:
                i -= 1
        else:
            i += 1
    return board
start = time.time()
answer = get_answer(board)
end = time.time()

print(answer)
print('time:', end-start)