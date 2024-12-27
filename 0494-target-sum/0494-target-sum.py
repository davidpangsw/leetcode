class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        T = sum(nums)

        # Recursive relation
        # f(nums[:k], target) = f(nums[:k-1], target+nums[k-1]) + f(nums[:k-1], target-nums[k-1])
        # 2^20 = 1048576 acceptable
        mem = [[None for _ in range(T+1)] for _ in nums]
        def f(k, t):
            # print(f"f({k},{t})")
            if k == 0:
                return 1 if t == 0 else 0
            if t < 0: # number of combs for -t and t must be the same
                return f(k, -t)
            if t > T:
                return 0

            i, j = k-1, t
            if mem[i][j] is not None:
                return mem[i][j]
            mem[i][j] = f(k-1, t+nums[k-1]) + f(k-1, t-nums[k-1])
            # print(f"f({k},{t}) = {mem[i][j]}")
            return mem[i][j]
        return f(len(nums), target)

