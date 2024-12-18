OBJECT = 2
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        table = [[1] * n for _ in range(m)]
        for x in chain(guards, walls):
            table[x[0]][x[1]] = OBJECT
        
        # [print(row) for row in table]

        result = m * n - len(guards) - len(walls)
        for x in guards:
            row, col = x[0], x[1]
            for j in range(col-1, -1, -1):
                if table[row][j] is OBJECT:
                    break
                if table[row][j] != 0:
                    result -= 1
                table[row][j] = 0

            for j in range(col+1, n):
                if table[row][j] is OBJECT:
                    break
                if table[row][j] != 0:
                    result -= 1
                table[row][j] = 0

            for i in range(row-1, -1, -1):
                if table[i][col] is OBJECT:
                    break
                if table[i][col] != 0:
                    result -= 1
                table[i][col] = 0

            for i in range(row+1, m):
                if table[i][col] is OBJECT:
                    break
                if table[i][col] != 0:
                    result -= 1
                table[i][col] = 0

        return result
        # return sum([row.count(1) for row in table])
