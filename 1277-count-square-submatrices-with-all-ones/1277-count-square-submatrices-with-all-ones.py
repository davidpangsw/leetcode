class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # [print(row) for row in matrix]
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                
        total = 0
        for i in range(0, m):
            for j in range(0, n):
                total += matrix[i][j]

                # print(rect[i][j], streak, total)
            # print(rect)
        # print()
        # [print(row) for row in matrix]
        return total
                

