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


'''(bad)
def get_arrayList(board):
    array_list = np.array([np.ndarray] * 9,dtype=object)
    origin = np.array([1,2,3,4,5,6,7,8,9])
    b = board>0
    #permutations = np.array([],dtype='int8')
    for i in mp(origin):
        i = np.array(i)
        for j in range(9):
            if False in i[b[j]] == board[j][b[j]]:
                continue
            if type(array_list[j]) is type:
                array_list[j] = [i]
            else:
                array_list[j] = np.append(array_list[j], [i], axis=0)
    return  array_list
'''

def isDuplicated(idx, array, board):
    for i in range(9):
        a = idx//3
        b = i//3
        if array[i] in np.delete(board[:,i], idx) or array[i] in np.delete(board[3*a:3*a+3, 3*b:3*b+3], idx%3, 0):
            return True
    return False

def eli_dupl(array_list, board):
    for i in range(9):
        l = np.array([], dtype='int8')
        for j in range(len(array_list[i])):
            if isDuplicated(i, array_list[i][j], board):
                l = np.append(l, j)
        #print(l)
        array_list[i] = np.delete(array_list[i], l, 0)

def get_arrayList(board):
    import sqlite3
    con = sqlite3.connect('sudoku.db')
    crs = con.cursor()
    '''
    from sympy.utilities.iterables import multiset_permutations as mp
    crs.execute("DROP TABLE IF EXISTS Permutations")
    crs.execute("CREATE TABLE Permutations (one INTEGER, two INTEGER, three INTEGER, four INTEGER, five INTEGER, six INTEGER, seven INTEGER, eight INTEGER, nine INTEGER)")
    origin = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in mp(origin):
        i = tuple(i)
        crs.execute(f"INSERT INTO Permutations VALUES {i}")
    con.commit()
    '''
    array_list = np.array([np.ndarray] * 9, dtype=object)
    cols = np.array(crs.execute("SELECT * FROM Permutations").description)[:,0]

    for i in range(len(board)):
        k = str(tuple(cols[board[i]>0])).replace('\'','').replace(',)',')')
        v = str(tuple(board[i][board[i]>0])).replace(',)',')')
        #print(k)
        #print(v)
        data = crs.execute(f"SELECT * FROM Permutations where {k}={v}")
        array_list[i] = np.array(data.fetchall(),dtype="int8")

    eli_dupl(array_list, board)
    return  array_list

def isValid1(array, ans_arrays):
    if not ans_arrays is None:
        for i in range(9):
            if array[i] in ans_arrays[:,i]:
                return False
    return True

def isValid2(i, array, ans_arrays):
    if i % 3 != 0:
        for a in range(0,3):
            for b in range(3*a,3*a+3):
                if array[b] in ans_arrays[-(i%3):,3*a:3*a+3]:
                    return False
    return True

def isValid(idx, array, ans_arrays):
    if not ans_arrays is None:
        if idx%3 == 0:
            for i in range(9):
                if array[i] in ans_arrays[:,i]:
                    return False
        else:
            for i in range(9):
                b = i//3
                if array[i] in ans_arrays[:,i] or array[i] in ans_arrays[-(idx%3):,3*b:3*b+3]:
                    return False
    return True


def validRows(idx,arrays,ans_arrays):
    loc = np.array([],dtype='int8')
    for i in range(len(arrays)):
        if isValid(idx, arrays[i], ans_arrays):
            loc = np.append(loc, i)
    return loc

def findAns_arrays(array_list):
    ans_arrays = None
    count = 0
    i = 0
    idx = np.array([0]*9,dtype='int8')
    row_arrays = np.array([np.ndarray]*9,dtype=object)
    while 0 <= i < 9:
        row_arrays[i] = validRows(i, array_list[i], ans_arrays)
        if len(row_arrays[i]) != 0:
            if ans_arrays is None:
                ans_arrays = np.array([array_list[i][row_arrays[i][idx[i]]]])
            else:
                ans_arrays = np.append(ans_arrays, [array_list[i][row_arrays[i][idx[i]]]], axis=0)
            i += 1
        else:
            ans_arrays = np.delete(ans_arrays, -1, 0)
            i -= 1
            idx[i] += 1
            while idx[i] >= len(row_arrays[i]):
                ans_arrays = np.delete(ans_arrays, -1, 0)
                idx[i] = 0
                i -= 1
                idx[i] += 1
            ans_arrays = np.append(ans_arrays, [array_list[i][row_arrays[i][idx[i]]]], axis=0)
            i += 1

    return ans_arrays

start = time.time()
ans_arrays = findAns_arrays(get_arrayList(board))
end = time.time()
print(ans_arrays)
print('time:', end-start)