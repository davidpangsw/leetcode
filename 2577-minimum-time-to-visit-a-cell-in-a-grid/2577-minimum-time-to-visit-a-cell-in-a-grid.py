class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = [[0, 0, 0]]
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        while q:
            # print(q)
            cost, x, y = heappop(q)
            if x == m-1 and y == n-1:
                return cost -  (m-1-x+n-1-y)

            if visited[x][y]:
                continue
            visited[x][y] = True

            for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
                X, Y = x+dx, y+dy

                if not (0 <= X < m and 0 <= Y < n):
                    continue

            
                if cost + 1 < grid[X][Y]:
                    if cost == 0: # no grid to go backward, view (0,0) again later
                        visited[0][0] = False
                        continue
                    # go back and forth until time enough
                    # which is equivalent to "wait" even number of seconds
                    # and then go 1 step (that is, odd)
                    if (grid[X][Y] - cost) % 2 == 0:
                        nextCost = grid[X][Y] + 1
                    else:
                        nextCost = grid[X][Y]
                else:
                    nextCost = cost + 1
                heappush(q, [nextCost + (m-1-X+n-1-Y), X, Y])
        return -1
