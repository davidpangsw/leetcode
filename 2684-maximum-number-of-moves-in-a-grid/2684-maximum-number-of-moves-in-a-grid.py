# BFS and DFS are both O(mn)
# DFS: potentially early return if we meet the end
class Solution:
    # DFS 
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        result = 0
        for start in range(m):
            stack = [(start, 0)]
            while stack:
                row, col = stack.pop()
                if col == n-1:
                    return col
                x = grid[row][col]
                for newRow in range(max(0, row-1), min(m, row+2)):
                    if grid[newRow][col+1] > x:
                        stack.append((newRow, col+1))
                result = max(result, col)
                grid[row][col] = -1 # mark as visited
        
        return result




    # BFS
    def maxMovesBFS(self, grid: List[List[int]]) -> int:
        # BFS with layers, use a set as the queue
        m = len(grid)
        n = len(grid[0])

        col = 0
        queue = set(range(m)) # set of row index
        while col < n - 1:
            newQueue = set()
            for row in queue:
                x = grid[row][col]
                for newRow in range(max(0, row-1), min(m, row+2)):
                    if grid[newRow][col+1] > x:
                        newQueue.add(newRow)

            if not newQueue:
                return col
            queue = newQueue
            col += 1
        
        return col
