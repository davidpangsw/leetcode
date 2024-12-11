class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # consider the intervals [nums[i] - k, nums[i] + k]
        # the answer would be the maximum count of overlaps
        # use a queue to store all overlapping intervals (represented by two pointer)
        nums.sort()
        result = 1
        p = 0 # nums[p, i] is like a queue of intervals
        for i in range(1, len(nums)):
            # dequeue all non-overlapping intervals
            # we don't need to dequeue all in practice, as it doesn't affect the maximum count
            if nums[p] < nums[i] - 2 * k:
                p += 1
            # # binary search the left index
            # p = bisect_left(nums, nums[i] - 2 * k, lo=p, hi=i)

            # now, all intervals from p to i are overlapping
            result = max(result, i - p + 1)
        return result

