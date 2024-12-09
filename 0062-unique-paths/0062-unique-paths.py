def comb(n, r):
    # n*(n-1) ...(n-r+1)
    # 1*2*...*r
    result = 1
    for i in range(r):
        result = result * (n-i) // (i+1)
    return result

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = (m-1)+(n-1)
        return comb(N, m-1)