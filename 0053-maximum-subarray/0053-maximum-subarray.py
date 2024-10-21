class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        result = (s := nums[0])
        for right in range(1, len(nums)):
            while s <= 0 and left < right:
                s -= nums[left]
                left += 1
            
            s += nums[right]
            result = max(result, s)

        return result
        