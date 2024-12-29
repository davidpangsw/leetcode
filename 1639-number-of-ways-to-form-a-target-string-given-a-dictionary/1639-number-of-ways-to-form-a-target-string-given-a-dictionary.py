M = 10 ** 9 + 7
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        data = [defaultdict(int) for _ in words[0]]
        for w in words:
            for i, x in enumerate(w):
                data[i][x] += 1
        
        @cache
        def f(cur: int, t: int):
            if t == len(target):
                return 1
            if cur == len(data):
                return 0
            return (data[cur][target[t]] * f(cur+1, t+1) + f(cur+1, t)) % M
        return f(0, 0)

    def numWaysSampleAnswer(self, words: List[str], target: str) -> int:
        m = len(target)
        num_word = len(words)
        n = len(words[0])

        MOD = 10**9 + 7

        pos_cnt = []
        for j in range(n):
            char2cnt = collections.defaultdict(int)
            for i in range(num_word):
                char2cnt[words[i][j]] += 1
            pos_cnt.append(char2cnt)

        dp = [[0]*n for _ in range(2)]
        for j in range(n-m+1):
            if j == 0:
                dp[0][0] = pos_cnt[0][target[0]] % MOD
            else:
                dp[0][j] = (dp[0][j-1] + pos_cnt[j][target[0]])%MOD
        for i in range(1, m):
            dp[i%2] = [0]*n
            for j in range(i, n-m+i+1):
                dp[i%2][j] = (dp[i%2][j-1] + dp[(i-1)%2][j-1] * pos_cnt[j][target[i]]) % MOD
        return dp[(m-1)%2][n-1]
