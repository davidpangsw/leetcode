class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elemToLength = {}
        for x in set(nums):
            a = elemToLength.get(x-1, 0)
            b = elemToLength.get(x+1, 0)
            newLength = a + 1 + b
            elemToLength[x-a] = newLength
            elemToLength[x+b] = newLength
        return max(elemToLength.values()) if nums else 0
