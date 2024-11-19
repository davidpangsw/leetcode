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

lefts = [None] * 100001
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # "left" of the sliding windows
        # use an array to implement the deque
        # q = deque()
        lefts[0] = (0, 0) # [ind=0, curSum=0]
        lefts_low, lefts_high = 0, 0

        curSum = 0
        result = inf # math.inf
        for right in range(len(nums)):
            curSum += nums[right]
            if nums[right] > 0:
                # can change to binary search
                temp = None
                found = False
                while lefts_low <= lefts_high and curSum - lefts[lefts_low][1] >= k:
                    found = True
                    temp = lefts[lefts_low]
                    lefts_low += 1
                if temp:
                    result = min(result, right+1-lefts[lefts_low-1][0])
                
                # ind = bisect_right(lefts, curSum-k, lo=lefts_from, hi=lefts_to, key=lambda item: item[1])
                # # print(lefts[lefts_from:lefts_to], curSum-k, ind)
                # if ind > 0:
                #     lefts_from = ind
                #     result = min(result, right+1-lefts[lefts_from-1][0])
            else:
                # can change to binary search
                while lefts_low <= lefts_high and lefts[lefts_high][1] >= curSum:
                    lefts_high -= 1
            
            # lefts.append([right+1, curSum])
            lefts_high += 1
            lefts[lefts_high] = (right+1, curSum)

        return result if result < inf else -1