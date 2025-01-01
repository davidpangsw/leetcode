class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones = [0] * n
        count = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                count += 1
            ones[i] = count
        # print(ones)

        result = 0
        for i in range(1, n):
            one = ones[i]
            zero = i - (ones[0] - ones[i])
            result = max(result, zero + one)
        return result
