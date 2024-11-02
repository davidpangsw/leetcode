def isValid(items):
    d = set()
    for x in items:
        if x == '.':
            continue
        if x in d:
            print("Not valid", items)
            return False
        d.add(x)
    
    return True

def col(board, j):
    for row in board:
        yield row[j]

def grid(board, ind):
    i = (ind // 3) * 3
    j = (ind % 3) * 3
    for di in range(3):
        for dj in range(3):
            yield board[i+di][j+dj]

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for ind in range(9):
            if not isValid(board[ind]):
                return False
            if not isValid(col(board, ind)):
                return False
            if not isValid(grid(board, ind)):
                return False

        return True
                