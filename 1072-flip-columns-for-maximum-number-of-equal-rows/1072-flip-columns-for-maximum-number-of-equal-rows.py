"""
group up same pattern, count, find the size of the biggest group
Two rows are of same pattern if like this:
    10011
    01100

Then after some flips
"""
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(Counter(hash((1-bit for bit in row)) if row[0] == 1 else hash(tuple(row)) for row in matrix).values())