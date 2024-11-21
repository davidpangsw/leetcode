OBJECT = 2

class Solution:

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # bitwise to make it faster? still O(m, n)
        result = 0
        table = [[1 for _ in range(n)] for _ in range(m)]
        for x in guards:
            table[x[0]][x[1]] = OBJECT
        for x in walls:
            table[x[0]][x[1]] = OBJECT
        
        for x in guards:
            row, col = x[0], x[1]
            for j in range(col-1, -1, -1):
                i, j = row, j
                if table[i][j] is OBJECT:
                    break
                table[i][j] = 0

            for j in range(col+1, n):
                i, j = row, j
                if table[i][j] is OBJECT:
                    break
                table[i][j] = 0

            for i in range(row-1, -1, -1):
                i, j = i, col
                if table[i][j] is OBJECT:
                    break
                table[i][j] = 0

            for i in range(row+1, m):
                i, j = i, col
                if table[i][j] is OBJECT:
                    break
                table[i][j] = 0
        # print(table)
        return sum([sum(row) for row in table]) - len(guards) * OBJECT - len(walls) * OBJECT