class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        return sum(
            [bisect_right(nums, upper - x, lo=k+1) - bisect_left(nums, lower - x, lo=k+1)
                for k, x in enumerate(nums)]
            )