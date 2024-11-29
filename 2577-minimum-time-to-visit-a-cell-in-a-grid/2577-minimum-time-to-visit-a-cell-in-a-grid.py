class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = []
        visited = [[False for _ in range(n)] for _ in range(m)]

        # special handling for (0, 0): it cannot go back and forth
        # (we need to visit it back)
        for X, Y in [[1,0], [0,1]]:
            if 1 >= grid[X][Y]:
                # heappush(q, [1, X, Y])
                heappush(q, [1 + (m-1+n-1-1), 1, X, Y])
        
        while q:
            # print(q)
            # cost, x, y = heappop(q)
            weight, cost, x, y = heappop(q)

            for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
                X, Y = x+dx, y+dy

                if not (0 <= X < m and 0 <= Y < n):
                    continue

                if visited[X][Y]:
                    continue
                visited[X][Y] = True
            
                if cost + 1 < grid[X][Y]:
                    # go back and forth until time enough
                    # which is equivalent to "wait" even number of seconds
                    # and then go 1 step (that is, odd)
                    if (grid[X][Y] - cost) % 2 == 0:
                        nextCost = grid[X][Y] + 1
                    else:
                        nextCost = grid[X][Y]
                else:
                    nextCost = cost + 1

                if X == m-1 and Y == n-1:
                    return nextCost

                # heappush(q, [nextCost, X, Y])
                heappush(q, [nextCost + (m-1-X+n-1-Y), nextCost, X, Y])

        return -1
