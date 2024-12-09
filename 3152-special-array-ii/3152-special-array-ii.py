class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefixCounts = [0] * len(nums)

        count = 0
        for i in range(1, len(nums)):
            count += ((nums[i] & 1)  == (nums[i-1] & 1))
            prefixCounts[i] = count
        # print(prefixCounts)
        
        return [prefixCounts[f] == prefixCounts[t] for f, t in queries]
