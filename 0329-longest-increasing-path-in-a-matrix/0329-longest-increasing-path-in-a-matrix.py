class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # consider the matrix as a directed graph
        results = [[None for _ in range(n)] for _ in range(m)]
        adjLists = [[[] for _ in range(n)] for _ in range(m)]

        # DFS

        # # find all starting points
        # for i, row in enumerate(matrix):
        #     for j, cell in enumerate(row):
        #         inDegree = 0
        #         for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        #             I, J = i+di, j+dj
        #             if 0 <= I < m and 0 <= J < n:
        #                 if matrix[I][J] < matrix[i][j]:
        #                     adjLists[I][J].append((i, j))
        #                     inDegree += 1
        #         if inDegree == 0:
        #             q.append((i, j))
               
        def dfs(i, j):
            if results[i][j]:
                return results[i][j]
            l = 1
            # for I, J in adjLists[i][j]:
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                I, J = i+di, j+dj
                if 0 <= I < m and 0 <= J < n:
                    if matrix[I][J] > matrix[i][j]:
                        l = max(l, 1 + dfs(I, J))
            results[i][j] = l
            return l

        result = 0
        for x in range(m):
            for y in range(n):
                result = max(result, dfs(x, y))
        return result
        

