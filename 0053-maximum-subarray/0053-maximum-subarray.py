class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = 1
        
        s = nums[0]
        result = nums[0]

        while right < n:
            if s <= 0 and left <= right - 1:
                s -= nums[left]
                left += 1
                continue
            
            s += nums[right]
            result = max(result, s)

            right += 1

        return result
        