class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        table = defaultdict(int)
        for row in matrix:
            key = str([1-bit for bit in row]) if row[0] == 1 else str(row)
            table[key] += 1
        return max(table.values())
        

