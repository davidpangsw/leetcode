# TABLE = 
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        print("{")
        for i in range(1000):
            sq = i**2
            if sq > 100000:
                break
            print(f"{sq}: {i},")
        print("}")
        # {sq : i for i in range(1000) if }
        return

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