class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # consider the matrix as a directed graph
        adjLists = [[[] for _ in range(n)] for _ in range(m)]

        # BFS
        q = deque()

        # find all starting points
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                inDegree = 0
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    I, J = i+di, j+dj
                    if 0 <= I < m and 0 <= J < n:
                        if matrix[I][J] < matrix[i][j]:
                            adjLists[I][J].append((i, j))
                            inDegree += 1
                if inDegree == 0:
                    q.append((i, j))

        result = 0
        while q:
            qSize = len(q)
            for _ in range(qSize):
                i, j = q.popleft()
                for I, J in adjLists[i][j]:
                    q.append((I, J))
            result += 1
        return result

