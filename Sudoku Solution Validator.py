# https://www.codewars.com/kata/529bf0e9bdf7657179000008 not the best way but works
def valid_solution(board):
    k=[1,2,3,4,5,6,7,8,9]
    l=[]
    for i in range(9):
        l=board[i]
        if sorted(l)!=k:
            return False
    l=[]
    for i in range(9):
        for j in range(9):
            l.append(board[j][i])
        if sorted(l)!=k:
            return False
        l=[]
    l=[]
    for i in [0,3,6]:
        for j in [0,3,6]:
            l.append(board[j][i])
            l.append(board[j+1][i])
            l.append(board[j+2][i])
            l.append(board[j][i+1])
            l.append(board[j+1][i+1])
            l.append(board[j+2][i+1])
            l.append(board[j][i+2])
            l.append(board[j+1][i+2])
            l.append(board[j+2][i+2])
            if sum(l)!=45:
                return False
            l=[]            
    return True
