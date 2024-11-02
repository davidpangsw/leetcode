class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
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
            result = max(result, newLength)
        return result
