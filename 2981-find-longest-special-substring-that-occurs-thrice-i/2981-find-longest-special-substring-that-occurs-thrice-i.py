class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        # counts[i] = #repeated char starting from i
        counts = [1] * n
        count = 1
        for i in range(n-2, -1, -1):
            if s[i] == s[i+1]:
                count += 1
            else:
                count = 1
            counts[i] = count
        
        # "at least twice"
        # countsTwice[i] = min(length of special string before i, counts[i])
        # data[c] = maximum count of character c (before i)
        maxCounts = [0] * 26
        maxCountsTwice = [0] * 26
        result = -1
        for i in range(n):
            x = ord(s[i]) - ord('a')
            countsTwice = min(maxCounts[x], counts[i])
            if maxCountsTwice[x]:
                countsThrice = min(maxCountsTwice[x], counts[i])
                result = max(result, countsThrice)
            maxCountsTwice[x] = max(maxCountsTwice[x], countsTwice)
            maxCounts[x] = max(maxCounts[x], counts[i])
        return result 
