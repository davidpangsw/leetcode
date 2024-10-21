class Solution:
    def divideAndConquer(self, nums: List[int]) -> int:
        pass

    def maxSubArray(self, nums: List[int]) -> int:
        result = (s := nums[0])
        for right in range(1, len(nums)):
            if s <= 0:
                s = nums[right]
            else:
                s += nums[right]
            result = max(result, s)

        return result
        