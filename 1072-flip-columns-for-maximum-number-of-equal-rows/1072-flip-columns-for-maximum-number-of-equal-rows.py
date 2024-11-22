class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        [print(row) for row in matrix]
        result = 0
        for prev_good in [True, False]:
            queue = deque(range(m))
            for j in range(1, n):
                q_good = deque()
                q_bad = deque()
                while queue:
                    i = queue.popleft()
                    if (matrix[i][j] == matrix[i][j-1]) == prev_good:
                        q_good.append(i)
                    else:
                        q_bad.append(i)

                # print(q_good, q_bad)
                if len(q_good) >= len(q_bad):
                    # print(j, "good")
                    queue = q_good
                    prev_good = True
                else:
                    # print(j, "flip")
                    queue = q_bad
                    prev_good = False
            result = max(result, len(queue))
        return result
        

