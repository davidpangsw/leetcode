class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # BFS with layers, use a set as the queue
        m = len(grid)
        n = len(grid[0])

        col = 0
        queue = set(range(m)) # set of row index
        while queue and col < n - 1:
            newQueue = set()
            for row in queue:
                x = grid[row][col]
                for newRow in range(max(0, row-1), min(m, row+2)):
                    if grid[newRow][col+1] > x:
                        newQueue.add(newRow)
                        # print(newRow)
            queue = newQueue
            col += 1
        
        if not queue:
            col -= 1 # step back if the loop exits because of empty queue
        return col

                

