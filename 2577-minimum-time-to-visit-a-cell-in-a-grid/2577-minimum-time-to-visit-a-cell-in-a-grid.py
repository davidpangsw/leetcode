class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # ensure we can go back and forth first
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        q = [(0, 0, 0)]
        # q = [(0, 0, 0, 0)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        while q:
            # print(q)
            cost, x, y = heappop(q)
            # weight, cost, x, y = heappop(q)

            for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
                X, Y = x+dx, y+dy

                if not (0 <= X < m and 0 <= Y < n):
                    continue

                if visited[X][Y]:
                    continue
            
                if cost + 1 < grid[X][Y]:
                    # go back and forth until time enough
                    # which is equivalent to "wait" even number of seconds
                    # and then go 1 step (that is, odd)
                    nextCost = grid[X][Y] + (1 - (grid[X][Y] - cost) % 2)
                else:
                    nextCost = cost + 1

                if X == m-1 and Y == n-1:
                    return nextCost

                visited[X][Y] = True
                heappush(q, (nextCost, X, Y))
                # heappush(q, (nextCost + (m-1-X+n-1-Y), nextCost, X, Y))

        return -1
