class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        result = 0
        for col in range(len(grid[0])):
            cur = grid[0][col]
            for row in range(1, len(grid)):
                if grid[row][col] <= cur:
                    cur += 1
                    result += cur - grid[row][col]
                else:
                    cur = grid[row][col]
        return result