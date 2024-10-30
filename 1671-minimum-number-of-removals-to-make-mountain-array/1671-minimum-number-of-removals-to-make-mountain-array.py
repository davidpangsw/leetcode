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

        # return the length of the longest increasing subsequence formed
        def uphill(arr):
            # subseq stored the longest subsequence (sorted)
            # the elements inside may not be true, but the length would be true
            subseq = []
            result = None
            for i, x in enumerate(arr):
                insertAt = binarySearch(subseq, x)
                if insertAt == len(subseq):
                    subseq.append(x)
                else:
                    subseq[insertAt] = x
                result = insertAt + 1 # as last item must be included, the result would be the insertAt+1 of the last item
            return result
        
        result = 3
        subseq_uphill = [nums[0]]
        for i in range(1, n-1):
            # take nums[i] as mountain
            # form uphill and downhill
            # print(f"mountain: nums[{i}] = {nums[i]}")

            x = nums[i]
            insertAt = binarySearch(subseq_uphill, x)
            if insertAt == len(subseq_uphill):
                subseq_uphill.append(x)
            else:
                subseq_uphill[insertAt] = x
            u = insertAt + 1





            # u = uphill(nums[:i+1])
            # print(f"uphill={u}")
            if u == 1:
                continue
            d = uphill(reversed(nums[i:]))
            # print(f"downhill={d}")
            if d == 1:
                continue

            result = max(result, u + d - 1)
        
        return n - result