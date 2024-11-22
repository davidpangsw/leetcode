class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        table = defaultdict(int)
        for row in matrix:
            key = hash(tuple([1-bit for bit in row])) if row[0] == 1 else hash(tuple(row))
            table[key] += 1
        return max(table.values())
        

