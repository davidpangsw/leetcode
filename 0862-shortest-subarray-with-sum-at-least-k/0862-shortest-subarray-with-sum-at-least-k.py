"""
Idea:
1. Sliding window comes into mind first. Normal implementation is [left, right] with a "while True" loop
2. However, we need to deal with the negative numbers:
    - if [left, right] sums to a number < k, we cannot do right += 1, because left += 1 is also possible.
    - if we can ensure left += 1 is impossible, then our solution is still O(n)
3. The problem is, for an index i, if there exists j > i such that [i, j] sums to negative, then left += 1 would possibly raise the window sum.
4. So, everytime after we extend "right", we also do a check to eliminate these problematic indices ahead, such that left cannot be them
5. To do this, we use a doubly linked queue to manage the possible "left"s
    - array and deque are both okay
"""

# "left" of the sliding windows
# use an array to implement the deque
# lefts = deque()
lefts = [None] * 100001
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # lefts.append((-1, 0))
        lefts[0] = (-1, 0) # (ind=-1, accSum=0)
        lefts_low, lefts_high = 0, 0

        curSum = 0
        result = inf # math.inf
        for right in range(len(nums)):
            curSum += nums[right]
            if nums[right] > 0:
                # can change to binary search, but test cases don't favour this
                ind = None
                while lefts_low <= lefts_high and curSum - lefts[lefts_low][1] >= k:
                    # ind, _ = lefts.popleft()
                    ind = lefts[lefts_low][0]
                    lefts_low += 1
                if ind is not None:
                    result = min(result, right - ind) # ind can be -1
            else:
                # can change to binary search, but test cases don't favour this
                while lefts_low <= lefts_high and lefts[lefts_high][1] >= curSum:
                    lefts_high -= 1
            
            # lefts.append((right, curSum]))
            lefts_high += 1
            lefts[lefts_high] = (right, curSum)

        return result if result < inf else -1