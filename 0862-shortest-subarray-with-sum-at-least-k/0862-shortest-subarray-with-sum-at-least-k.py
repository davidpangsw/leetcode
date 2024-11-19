class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i+1] = sums[i] + nums[i]
        # sums[i] = sum(nums[:i])
        # sums[i] - nums[j] = sum[i:j]
        print(sums) 


        result = n+1
        for i in range(n+1):
            for diff in range(1, min(result, n+1-i)):
                if sums[i+diff] - sums[i] >= k:
                    result = diff
                    break
        if result == n+1:
            return -1
        return result
