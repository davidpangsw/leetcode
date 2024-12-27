class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = Counter(nums)
        keys = sorted(counts)
        # print([(x, counts[x]) for x in keys])

        COMB = [[None for _ in range(1001)] for _ in range(1001)]
        def C(x, r):
            # print(f"C({x},{r})")
            if r == 0 or r == x:
                return 1
            elif r == 1 or r == x-1:
                return x
            if x == 1:
                return 1
            if COMB[x][r] is None:
                COMB[x][r] = (C(x-1, r-1) * x) // r
            # print(f"C({x},{r}) = {COMB[x][r]}")
            return COMB[x][r]

        # backtracking
        mem = [[None for _ in range(2001)] for _ in range(20)]
        def backtracking(ind: int, t: int):
            # print(ind, t, len(keys))
            if ind == len(keys):
                return 1 if t == 0 else 0
            if t < -1000 or t > 1000:
                return 0

            i, j = ind, t + 1000
            if mem[i][j] is not None:
                return mem[i][j]

            # 5 ->   -5, -3, -1, 1, 3, 5
            # 6 -> -6, -4, -2, 0, 2, 4, 6
            #      6C0, 6C1, ...6C4, 6C5, 6C6
            # k -> [-k, -k+2, ..., k]  (k + 1 choices)
            # (x, k) => k+1 choices, each with (k, r)
            # (1, 5) => 6 choices, each with C(5, r)

            x = keys[ind]
            k = counts[x]
            result = 0
            for r in range(k+1):
                value = (-k + r*2) * x
                combs = C(k, r)
                result += combs * backtracking(ind+1, t - value)
            mem[i][j] = result
            # print(f"backtrack({ind},{t}) = {mem[i][j]}")
            return result
        return backtracking(0, target)

