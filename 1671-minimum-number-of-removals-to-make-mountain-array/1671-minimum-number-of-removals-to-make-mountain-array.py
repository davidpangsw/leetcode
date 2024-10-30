# itertools.islice(iterable, start, stop[, step])
# from itertools import islice
class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:

        # search the place to insert x
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

        # result[i] = the length of the longest increasing subsequence formed by arr[:i]
        # nums[i] must be included in that subsequence
        # accept iterator
        def uphill(arr):
            # subseq stored the longest subsequence (sorted)
            # the elements inside may not be true, but the length would be true
            subseq = []
            result = []
            for x in arr:
                insertAt = binarySearch(subseq, x)
                if insertAt == len(subseq):
                    subseq.append(x)
                else:
                    subseq[insertAt] = x
                
                # as arr[i] must be included, the result would be the insertAt+1
                result.append(insertAt + 1)
            return result
        
        up = uphill(nums)
        down = reversed(uphill(reversed(nums)))

        result = 3
        for i, (u, d) in enumerate(zip(up, down), 1):
            # take nums[i] as mountain, and form uphill and downhill
            if i == len(nums) - 1:
                continue
            # print(f"mountain: nums[{i}] = {nums[i]}")
            # print(f"uphill={u}")
            # print(f"downhill={d}")

            # if the subsequence is only nums[i], skip
            if u == 1:
                continue
            if d == 1:
                continue
            result = max(result, u + d - 1)
        
        return len(nums) - result