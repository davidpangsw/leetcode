# itertools.islice(iterable, start, stop[, step])
# from itertools import islice
class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # result[i] = the length of the longest increasing subsequence formed by nums[:i-1],
        #             strictly bounded above by nums[i]
        def uphill(arr: Iterator[int]) -> Iterator[int]:
            # subseq stored the longest subsequence (sorted)
            # the elements inside may not be true, but the length would be true
            subseq = []
            for x in arr:
                insertAt = bisect_left(subseq, x)
                if insertAt == len(subseq):
                    subseq.append(x)
                else:
                    subseq[insertAt] = x
                
                yield insertAt
        
        # up = uphill(nums)
        # down = reversed(list(uphill(reversed(nums))))
        up = list(uphill(nums))
        down = list(uphill(reversed(nums)))[::-1]


        result = 3
        for i in range(1, len(nums)-1):
        # for i, (u, d) in enumerate(zip(up, down)):
            # take nums[i] as mountain, and form uphill and downhill
            # if i == 0 or i == len(nums) - 1:
                # continue
            u, d = up[i], down[i]
            # print(f"mountain: nums[{i}] = {nums[i]}")
            # print(f"uphill={u}")
            # print(f"downhill={d}")

            if u > 0 and d > 0:
                result = max(result, u + d + 1)
        
        return len(nums) - result