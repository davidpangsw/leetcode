class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))

        # result = 0
        elemToLength = {}
        for i, x in enumerate(nums):
            # if x in elemToLength:
            #     nums[i] = 0
            #     continue

            a = elemToLength.get(x-1, 0)
            b = elemToLength.get(x+1, 0)
            newLength = a + 1 + b
            elemToLength[x-a] = newLength
            elemToLength[x+b] = newLength
            # elemToLength[x] = newLength
            # result = max(result, newLength)
            nums[i] = newLength
        return max(nums) if nums else 0
        # return result
