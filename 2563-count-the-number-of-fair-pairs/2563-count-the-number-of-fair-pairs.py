class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        result = 0
        for k, x in enumerate(nums):
            i = bisect_left(nums, lower - x, lo=k+1)
            j = bisect_right(nums, upper - x, lo=k+1)
            result += j - i
        return result