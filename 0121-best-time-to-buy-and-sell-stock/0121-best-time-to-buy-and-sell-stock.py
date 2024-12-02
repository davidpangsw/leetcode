class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        curMin = inf
        for x in prices:
            if x > curMin:
                if result < x - curMin:
                    result = x - curMin
            else:
                curMin = x
        return result