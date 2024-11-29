DIRS = [(-1,0), (1,0), (0,-1), (0,1)]
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # ensure we can go back and forth first
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        q = [(0, 0, 0)]
        # q = [(0, 0, 0, 0)]
        visited = [[False] * n for _ in range(m)]
        while q:
            # print(q)
            cost, x, y = heappop(q)
            # weight, cost, x, y = heappop(q)

            for dx, dy in DIRS:
                X, Y = x+dx, y+dy

                if not (0 <= X < m and 0 <= Y < n):
                    continue

                if visited[X][Y]:
                    continue
            
                nextCost = cost + 1
                if nextCost < grid[X][Y]:
                    # go back and forth until time enough
                    # which is equivalent to "wait" even number of seconds
                    nextCost = grid[X][Y] + ((grid[X][Y] & 1) ^ (nextCost & 1))

                if X == m-1 and Y == n-1:
                    return nextCost

                visited[X][Y] = True
                heappush(q, (nextCost, X, Y))
                # heappush(q, (nextCost + (m-1-X+n-1-Y), nextCost, X, Y))

        return -1
