class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        elemToLength = {}
        for x in nums:
            a = elemToLength.get(x-1, 0)
            b = elemToLength.get(x+1, 0)
            elemToLength[x-a] = a + 1 + b
            elemToLength[x+b] = a + 1 + b
        return max(elemToLength.values()) if nums else 0
        # return result
