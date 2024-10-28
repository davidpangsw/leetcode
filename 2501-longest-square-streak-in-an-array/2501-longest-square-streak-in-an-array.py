class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        
        streaks = {}
        result = 0
        for x in nums:
            square = x**2
            if x in streaks:
                s = streaks[x]
                streaks[square] = s+1
            else:
                streaks[square] = 1
            result = max(result, streaks[square])
        return result if result > 1 else -1