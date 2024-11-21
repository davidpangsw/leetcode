OBJECT = 2

class Solution:

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        table = [[0 for _ in range(n)] for _ in range(m)]
        for x in chain(guards, walls):
            table[x[0]][x[1]] = OBJECT
        
        for x in guards:
            row, col = x[0], x[1]
            for j in range(col-1, -1, -1):
                if table[row][j] is OBJECT:
                    break
                table[row][j] = 1

            for j in range(col+1, n):
                if table[row][j] is OBJECT:
                    break
                table[row][j] = 1

            for i in range(row-1, -1, -1):
                if table[i][col] is OBJECT:
                    break
                table[i][col] = 1

            for i in range(row+1, m):
                if table[i][col] is OBJECT:
                    break
                table[i][col] = 1

        # print(table)
        # return sum([sum(row) for row in table]) - (len(guards) + len(walls)) * OBJECT
        return sum([row.count(0) for row in table])
