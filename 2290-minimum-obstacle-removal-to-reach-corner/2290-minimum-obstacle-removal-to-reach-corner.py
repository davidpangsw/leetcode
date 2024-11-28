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
            
            for dx, dy in DIRS:
                X, Y = x + dx, y + dy
                if 0 <= X < m and 0 <= Y < n:
                    if grid[X][Y] == 1:
                        # if mem[X][Y] <= cost + 1:
                        #     continue
                        heappush(q, (cost + 1, X, Y))
                    else:
                        # if mem[X][Y] <= cost:
                        #     continue
                        heappush(q, (cost, X, Y))
        raise "Path not found"

