# TODO: using bisection, can form uphill / downhill faster?
class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        # return the minimum number to form uphill in [0, i]
        # where nums[i] will be kept
        @cache
        def uphill(i):
            if i == 0:
                return 0
            x = nums[i]

            result = i
            for j in range(i-1, -1, -1):
                # assume j+1, ..., i-1 are all removed
                if nums[j] >= x: # must be removed
                    continue
                
                # can remove or not
                # if not remove, form uphill in [0, j], and add the #removals 
                result = min(result, i - (j+1) + uphill(j))

                # if remove, just do another iteration
            
            return result
        
        # return the minimum number to form downhill in [i, n-1]
        # where nums[i] will be kept
        # similar as uphill()
        @cache
        def downhill(i):
            if i == n-1:
                return 0
            x = nums[i]

            result = n - 1 - i
            for j in range(i+1, n):
                # assume i+1, i+2..., j-1 are all removed
                if nums[j] >= x: # must be removed
                    continue
                
                # can remove or not
                # if not remove, form uphill in [j, n-1], and add the #removals 
                result = min(result, j - (i+1) + downhill(j))

                # if remove, just do another iteration
            
            return result

        result = n-3
        for i in range(1, n-1):
            # print(f"mountain: nums[{i}] = {nums[i]}")
            # print(f"uphill={uphill(i)}, downhill={downhill(i)}")
            u = uphill(i)
            if u >= i:
                continue
            d = downhill(i)
            if d >= n-1-i:
                continue

            # take nums[i] as mountain
            # form uphill and downhill
            result = min(result, uphill(i) + downhill(i))
        
        return result