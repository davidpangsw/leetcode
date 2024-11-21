GUARD = 11
WALL = 12
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # bitwise to make it faster? still O(m, n)
        result = 0
        table = [[True for _ in range(n)] for _ in range(m)]
        for x in guards:
            table[x[0]][x[1]] = GUARD
        for x in walls:
            table[x[0]][x[1]] = WALL

        for i in range(m):
            curObj = None
            for j in range(n):
                if table[i][j] in [GUARD, WALL]:
                    curObj = table[i][j]
                else:
                    if curObj is GUARD:
                        table[i][j] = False

            curObj = None
            for j in range(n-1, -1, -1):
                if table[i][j] in [GUARD, WALL]:
                    curObj = table[i][j]
                else:
                    if curObj is GUARD:
                        table[i][j] = False

        for j in range(n):
            curObj = None
            for i in range(m):
                if table[i][j] in [GUARD, WALL]:
                    curObj = table[i][j]
                else:
                    if curObj is GUARD:
                        table[i][j] = False

            curObj = None
            for i in range(m-1, -1, -1):
                if table[i][j] in [GUARD, WALL]:
                    curObj = table[i][j]
                else:
                    if curObj is GUARD:
                        table[i][j] = False

                    if table[i][j] is True:
                        result += 1
        # print(table)
        return result