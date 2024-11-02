def isValid(items):
    d = set()
    for x in items:
        if x == '.':
            continue
        if x in d:
            # print("Not valid", items)
            return False
        d.add(x)
    
    return True

def col(board, j):
    for row in board:
        yield row[j]

def grid(board, i, j):
    for di in range(3):
        for dj in range(3):
            yield board[i+di][j+dj]

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            if not isValid(row):
                return False
        
        # cols
        for j in range(9):
            if not isValid([x for x in col(board, j)]):
                return False

        # grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValid([x for x in grid(board, i, j)]):
                    return False

        return True
                