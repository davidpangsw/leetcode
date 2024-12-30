M = 10**9+7
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # f(s) = #different good strings of size = s
        # f(s) = f(s-zero) + f(s-one)
        # f(0) = 1
        # f(s) = 0 for s < 0
        # result = f(high) - f(low-1)

        mem = [0] * (high + 1)
        mem[0] = 1
        for s in range(1, high+1):
            mem[s] = (mem[s-zero] + mem[s-one]) % M
            # if s >= zero:
            #     mem[s] += mem[s-zero] % M
            # if s >= one:
            #     mem[s] += mem[s-one] % M
        # print(mem)
        return sum(mem[low:high+1]) % M
