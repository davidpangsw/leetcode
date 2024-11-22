class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # [print(row) for row in matrix]
        result = 0
        table = defaultdict(int)
        for row in matrix:
            if row[0] == 0:
                # hashValue = sum([str(bit) for bit in row])                s
                key = str(row)
            else:
                key = str([1-bit for bit in row])
            # print(key)
            table[key] += 1




        return max(table.values())
        

