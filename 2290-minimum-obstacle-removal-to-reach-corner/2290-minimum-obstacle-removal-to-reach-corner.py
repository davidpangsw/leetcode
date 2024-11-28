class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # BFS + priority queue
        m, n = len(grid), len(grid[0])
        mem = [[inf for j in range(n)] for i in range(m)]
        mem[0][0] = 0
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()
            cost = mem[x][y]
            # print(cost, x, y)

            if x == m-1 and y == n-1:
                return cost

            if x > 0:
                X, Y = x - 1, y
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    if grid[X][Y]:
                        q.append((X, Y))
                    else:
                        q.appendleft((X, Y))
            if x < m-1:
                X, Y = x + 1, y
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    if grid[X][Y]:
                        q.append((X, Y))
                    else:
                        q.appendleft((X, Y))
            if y > 0:
                X, Y = x, y - 1
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    if grid[X][Y]:
                        q.append((X, Y))
                    else:
                        q.appendleft((X, Y))
            if y < n-1:
                X, Y = x, y + 1
                if mem[X][Y] > cost + grid[X][Y]:
                    mem[X][Y] = cost + grid[X][Y]
                    if grid[X][Y]:
                        q.append((X, Y))
                    else:
                        q.appendleft((X, Y))

        raise "Path not found"

