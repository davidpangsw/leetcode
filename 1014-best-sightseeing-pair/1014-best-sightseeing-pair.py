class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        curMax = values[0] + 0
        result = -1
        for j in range(1, n):
            result = max(result, values[j] - j + curMax)
            curMax = max(curMax, values[j] + j)
        return result