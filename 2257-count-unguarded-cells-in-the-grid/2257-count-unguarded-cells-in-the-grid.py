class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # bitwise to make it faster? still O(m, n)
        result = 0
        table = [[True for _ in range(n)] for _ in range(m)]
        GUARD = "G"
        WALL = "W"
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

        # rows = [[] for _ in range(m)]
        # cols = [[] for _ in range(n)]
        # for x in guards:
        #     i, j = x[0], x[1]
        #     rows[i].append(j, GUARD)
        #     cols[j].append(i, GUARD)
        #     table[i][j] = GUARD
        # for x in walls:
        #     i, j = x[0], x[1]
        #     rows[i].append(j, WALL)
        #     cols[j].append(i, WALL)
        #     table[i][j] = WALL

        # for i in m:
        #     rows[i].sort()
        # for j in range(n):
        #     cols[j].sort()

        # # given i, j, 
        # # want: closest forward guard/wall in the same row
        # result = 0
        # prevObj = EMPTY
        # curObj = EMPTY
        # for i in range(m):
        #     for j in range(n):
        #         curObj = table[i][j]
        #         if (curObj == EMPTY and 
        #             (prevObj == WALL and nextObj == WALL) and
        #             (prevColObj == WALL and nextColObj == WALL)
        #             ):
        #             result += 1
        
        # return result
        