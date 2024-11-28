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

            if x == m-1 and y == n-1:
                return cost

            if x > 0:
                X, Y = x - 1, y
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    heappush(q, (cost + grid[X][Y], X, Y))
            if x < m-1:
                X, Y = x + 1, y
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    heappush(q, (cost + grid[X][Y], X, Y))
            if y > 0:
                X, Y = x, y - 1
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    heappush(q, (cost + grid[X][Y], X, Y))
            if y < n-1:
                X, Y = x, y + 1
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    heappush(q, (cost + grid[X][Y], X, Y))

        raise "Path not found"

