class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        # consider the intervals [nums[i] - k, nums[i] + k]
        # make all interval exclusive
        # combine overlaps and store the counts
        # the answer would be the maximum count

        result = 1
        # intervals = deque()
        p = 0 # like a deque of intervals
        for i in range(1, n):
            # dequeue all non-overlapping intervals
            if nums[p] + k < nums[i] - k:
                p += 1
            

            # now, all intervals from i to p are overlapping
            result = max(result, i - p + 1)
        return result




        # # store all left bound and counts (right bound = next left bound)
        # intervals = [[-inf, 0]]
        # for x in nums:
        #     # print(intervals)
        #     a, b = x-k, x + k + 1
        #     ind = bisect_left(intervals, a, key=lambda interval : interval[0])
        #     if ind == len(intervals): # a is larger than all bounds
        #         intervals.append([a, 1])
        #         intervals.append([b, 0])
        #     elif a < intervals[ind][0]:
        #         # split the prev interval
        #         intervals.insert(ind, [a, intervals[ind-1][1]])

        #         # increment all overlapped intervals
        #         for i in range(ind, len(intervals)):
        #             if intervals[i][0] < b:
        #                 intervals[i][1] += 1
        #             else:
        #                 raise ("Unknown situation", intervals, (a, b))
        #                 # break
                
        #         # append new ending interval
        #         if b > intervals[-1][0]:
        #             intervals.append([b, 0])
        #     else: # if a == intervals[ind][0]:

        #         # increment all overlapped intervals
        #         for i in range(ind, len(intervals)):
        #             if intervals[i][0] < b:
        #                 intervals[i][1] += 1

        #         # append new ending interval
        #         if b > intervals[-1][0]:
        #             intervals.append([b, 0])
        # # print(intervals)

        # result = 1
        # for a, count in intervals:
        #     result = max(result, count)
        # return result
            



