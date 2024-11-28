DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # BFS + priority queue
        m, n = len(grid), len(grid[0])
        mem = [[inf for j in range(n)] for i in range(m)]

        # cost, x, y
        q = [(0, 0, 0)]

        while q:
            cost, x, y = heappop(q)
            # print(cost, x, y)
            if mem[x][y] <= cost:
                continue

            if x == m-1 and y == n-1:
                return cost
            mem[x][y] = cost

            # if x > 0:
            #     X, Y = x - 1, y
            #     if 0 <= X < m and 0 <= Y < n and mem[X][Y] > cost + grid[X][Y]:
            #         heappush(q, (cost + grid[X][Y], X, Y))
            # if x > 0:
            #     X, Y = x - 1, y
            #     if 0 <= X < m and 0 <= Y < n and mem[X][Y] > cost + grid[X][Y]:
            #         heappush(q, (cost + grid[X][Y], X, Y))
            # if x > 0:
            #     X, Y = x - 1, y
            #     if 0 <= X < m and 0 <= Y < n and mem[X][Y] > cost + grid[X][Y]:
            #         heappush(q, (cost + grid[X][Y], X, Y))
            # if x > 0:
            #     X, Y = x - 1, y
            #     if 0 <= X < m and 0 <= Y < n and mem[X][Y] > cost + grid[X][Y]:
            #         heappush(q, (cost + grid[X][Y], X, Y))
            
            for dx, dy in DIRS:
                X, Y = x + dx, y + dy
                if 0 <= X < m and 0 <= Y < n and mem[X][Y] > cost + grid[X][Y]:
                    heappush(q, (cost + grid[X][Y], X, Y))
        raise "Path not found"

