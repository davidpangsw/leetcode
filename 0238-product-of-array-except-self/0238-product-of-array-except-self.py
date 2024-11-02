class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        suffix = 1
        for i in range(n-1, 0, -1):
            result = prefix[i-1] * suffix
            suffix *= nums[i]
            nums[i] = result
        nums[0] = suffix

        return nums