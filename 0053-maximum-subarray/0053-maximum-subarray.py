class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 1
        s = nums[0]
        result = nums[0]
        while right < len(nums):
            while s <= 0 and left < right:
                s -= nums[left]
                left += 1
            
            s += nums[right]
            result = max(result, s)

            right += 1

        return result
        