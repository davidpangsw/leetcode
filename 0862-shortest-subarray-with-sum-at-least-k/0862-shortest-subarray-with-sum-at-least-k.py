"""
Idea:
1. Sliding window comes into mind first. Normal implementation is [left, right] with a "while True" loop
2. However, we need to deal with the negative numbers:
    - if [left, right] sums to a number < k, we cannot do right += 1. left += 1 is also possible.
    - if we can ensure left += 1 is impossible, then our solution is still O(n)
3. The problem is, for an index i, if there exists j > i such that [i, j] sums to negative, then left += 1 would possibly raise the window sum.
4. So, everytime after we extend "right", we also do a check to eliminate these problematic i
5. To do this, we use a deque to manage the possible "left"s
"""

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # "left" of the sliding windows
        # use an array to implement the deque
        # q = deque()
        lefts = [None] * (n+1)
        lefts_from, lefts_to = 0, 0

        curSum = 0
        result = n+1
        for i in range(n+1):
            while lefts_to - lefts_from > 0 and curSum - lefts[lefts_from][1] >= k:
                result = min(result, i-lefts[lefts_from][0])
                lefts_from += 1
            
            # larger prefix sum => cannot be the left of the subarray
            while lefts_to - lefts_from > 0 and lefts[lefts_to-1][1] >= curSum:
                lefts_to -= 1
            lefts[lefts_to] = [i, curSum]
            lefts_to += 1
            if i < n:
                curSum += nums[i]

            # # use binary search as lefts is monotone
            # ind = bisect_left(lefts, sums[i], lo=lefts_from, hi=lefts_to, key=lambda left: sums[left])
            # lefts[ind] = i
            # lefts_to = ind + 1
        if result == n+1:
            return -1
        return result