class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = [[0, 0, 0]]
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        while q:
            # print(q)
            cost, x, y = heappop(q)
            # print(cost, x, y)
            if x == m-1 and y == n-1:
                return cost
            # print(visited[x][y])
            if visited[x][y]:
                continue
            visited[x][y] = True

            for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
                X, Y = x+dx, y+dy
                # print(X, Y)

                if not (0 <= X < m and 0 <= Y < n):
                    continue

            
                if cost + 1 < grid[X][Y]:
                    if cost == 0: # no grid to go backward, view it later
                        visited[0][0] = False
                        continue
                    # go back and forth until time enough
                    # which is equivalent to "wait" even number of seconds
                    # and then go 1 step (that is, odd)
                    if (grid[X][Y] - cost) % 2 == 0:
                        heappush(q, [grid[X][Y] + 1, X, Y])
                    else:
                        heappush(q, [grid[X][Y], X, Y])
                else:
                    heappush(q, [cost + 1, X, Y])
        return -1
