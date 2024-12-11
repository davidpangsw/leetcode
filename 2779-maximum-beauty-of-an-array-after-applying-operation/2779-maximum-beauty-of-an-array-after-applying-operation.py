class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # consider the intervals [nums[i] - k, nums[i] + k]
        # make all interval exclusive
        # combine overlaps and store the counts
        # the answer would be the maximum count
        nums.sort()
        result = 1
        
        # intervals = deque()
        p = 0 # like a deque of intervals
        for i in range(1, len(nums)):
            # dequeue all non-overlapping intervals
            if nums[p] + k < nums[i] - k:
                p += 1
            # now, all intervals from i to p are overlapping
            result = max(result, i - p + 1)
        return result

