class Solution:
    def divideAndConquer(self, nums: List[int]) -> int:
        pass

    def maxSubArray(self, nums: List[int]) -> int:
        result = (s := nums[0])
        for right in range(1, len(nums)):
            if s <= 0:
                s = nums[right]

                # to prevent all items are negative
                result = max(result, s)
            else:
                s += nums[right]
                result = max(result, s)

        return result
        