class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        curMin = inf
        for x in prices:
            if x > curMin:
                result = max(result, x - curMin)
            else:
                curMin = x
        return result