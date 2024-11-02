class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        elemToLength = {}
        for x in nums:
            # print("Adding ", x)
            if x in elemToLength:
                continue
            elif x+1 in elemToLength and x-1 in elemToLength:
                # merge
                newLength = elemToLength[x-1] + 1 + elemToLength[x+1]
                elemToLength[x-elemToLength[x-1]] = newLength
                elemToLength[x+elemToLength[x+1]] = newLength
                elemToLength[x] = newLength
                result = max(result, newLength)
            elif x+1 in elemToLength:
                newLength = 1 + elemToLength[x+1]
                elemToLength[x-0] = newLength
                elemToLength[x+elemToLength[x+1]] = newLength
                result = max(result, newLength)
            elif x-1 in elemToLength:
                newLength = 1 + elemToLength[x-1]
                elemToLength[x-elemToLength[x-1]] = newLength
                elemToLength[x+0] = newLength
                result = max(result, newLength)
            else:
                elemToLength[x] = 1
                result = max(result, 1)
        return result
