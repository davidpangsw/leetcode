# TODO: how to make it faster?
# itertools.islice(iterable, start, stop[, step])
# from itertools import islice
class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        # search the place to insert
        def binarySearch(arr, x):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < x:
                    left = mid + 1
                elif arr[mid] > x:
                    right = mid
                else:
                    return mid
            return left

        # result[i] = the length of the longest increasing subsequence formed from arr[:i]
        # nums[i] must be included in that subsequence
        def uphill(arr):
            # subseq stored the longest subsequence (sorted)
            # the elements inside may not be true, but the length would be true
            subseq = []
            result = [] 
            for i, x in enumerate(arr):
                insertAt = binarySearch(subseq, x)
                if insertAt == len(subseq):
                    subseq.append(x)
                else:
                    subseq[insertAt] = x
                result.append(insertAt + 1) # as arr[i] must be included, the result would be the insertAt+1
            return result
        
        up = uphill(nums)
        down = uphill(reversed(nums))
        down.reverse()

        result = 3
        for i in range(1, n-1):
            # take nums[i] as mountain
            # form uphill and downhill
            # print(f"mountain: nums[{i}] = {nums[i]}")
            u, d = up[i], down[i]
            # print(f"uphill={u}")
            # print(f"downhill={d}")
            if u == 1:
                continue
            if d == 1:
                continue

            result = max(result, u + d - 1)
        
        return n - result