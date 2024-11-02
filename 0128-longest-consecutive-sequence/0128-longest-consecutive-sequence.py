class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = list(set(nums))
        elemToLength = {}
        for x in nums:
            if x in elemToLength:
                continue
            a = elemToLength.get(x-1, 0)
            b = elemToLength.get(x+1, 0)
            newLength = a + 1 + b
            elemToLength[x-a] = newLength
            elemToLength[x+b] = newLength
            elemToLength[x] = newLength
        return max(elemToLength.values()) if nums else 0
