M = 10**9+7
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # f(s) = #different good strings of size = s
        # f(s) = f(s-zero) + f(s-one)
        # f(0) = 1
        # f(s) = 0 for s < 0
        # result = sum(mem[low:high+1])
        

        mem = [1] + [0] * high
        for s in range(1, high+1):
            # if s-zero is negative, it goings to the end (negative index in python)
            # it is genrally saf:e
            # (high+1)+(s-x) < s iff high + 1 < x
            # But x=zero and x=one are not that large
            mem[s] = (mem[s-zero] + mem[s-one]) % M
        # print(mem)

        # (high+1-low) <= 10^5
        # the total sum <= 10^5 * M ~= 10**14
        # (python doesn't have overflow anyway...?)
        result = 0
        for i in range(low, high+1):
            result += mem[i]
        return result % M
        # return sum(mem[low:high+1]) % M
