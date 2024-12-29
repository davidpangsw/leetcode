M = 10 ** 9 + 7
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        T = len(target)
        P = len(words[0])
        if T > P:
            return 0

        # posCharCounts[i][x] = counts of character x at position i
        posCharCounts = [defaultdict(int) for _ in words[0]]
        for w in words:
            for i, x in enumerate(w):
                posCharCounts[i][x] += 1
        

        # f(p, t) = #ways that given words until position, match target until position t
        # f(p, t) = posCharCounts[p][target[t]] * f(p-1, t-1) + f(p-1, t)
        # f(p, t) = 0 if p < t
        # f(0, 0) = posCharCounts[0][target[0]]
        # f(p, 0) = posCharCounts[p][target[t]] + f(p-1, t)  (for p > 0)
        # t = 0
        curRow = [None] * P
        curRow[0] = posCharCounts[0][target[0]]
        for p in range(1, P):
            curRow[p] = posCharCounts[p][target[0]] + curRow[p-1]
        # print(curRow)
        for t in range(1, T):
            prevRow = [x for x in curRow]
            # for p in range(t):
                # curRow[p] = 0
            curRow[t-1] = 0
            for p in range(t, P):
                curRow[p] = (posCharCounts[p][target[t]] * prevRow[p-1] + curRow[p-1]) % M
            # print(curRow)
        return curRow[-1]

        
        # # recursive dp, much cleaner
        # @cache
        # def f(pos: int, t: int):
        #     if t == len(target):
        #         return 1
        #     if pos == len(data):
        #         return 0
        #     return (data[pos][target[t]] * f(pos+1, t+1) + f(pos+1, t)) % M
        # return f(0, 0)
