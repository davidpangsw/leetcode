class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # BFS + priority queue
        m, n = len(grid), len(grid[0])
        mem = [[inf for j in range(n)] for i in range(m)]
        mem[0][0] = 0

        # cost, x, y
        # q = [(0, 0, 0)]
        q = deque([(0, 0, 0)])

        def update(cost, X, Y):
            if mem[X][Y] > cost + grid[X][Y]:
                mem[X][Y] = cost + grid[X][Y]
                if grid[X][Y]:
                    q.append((cost + grid[X][Y], X, Y))
                else:
                    q.appendleft((cost + grid[X][Y], X, Y))

        while q:
            cost, x, y = q.popleft()
            # print(cost, x, y)

            if x == m-1 and y == n-1:
                return cost

            if x > 0:
                update(cost, x-1, y)
                # X, Y = x - 1, y
                # if mem[X][Y] > cost + grid[X][Y]:
                #     mem[X][Y] = cost + grid[X][Y]
                #     heappush(q, (cost + grid[X][Y], X, Y))
            if x < m-1:
                update(cost, x+1, y)
                # X, Y = x + 1, y
                # if mem[X][Y] > cost + grid[X][Y]:
                #     mem[X][Y] = cost + grid[X][Y]
                #     heappush(q, (cost + grid[X][Y], X, Y))
            if y > 0:
                update(cost, x, y - 1)
                # X, Y = x, y - 1
                # if mem[X][Y] > cost + grid[X][Y]:
                #     mem[X][Y] = cost + grid[X][Y]
                #     heappush(q, (cost + grid[X][Y], X, Y))
            if y < n-1:
                update(cost, x, y + 1)
                # X, Y = x, y + 1
                # if mem[X][Y] > cost + grid[X][Y]:
                #     mem[X][Y] = cost + grid[X][Y]
                #     heappush(q, (cost + grid[X][Y], X, Y))

        raise "Path not found"

