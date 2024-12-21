class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = [False] * (len(s) + 1)
        mem[-1] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                if mem[j] and s[i:j] in wordDict:
                    mem[i] = True
                    break
        return mem[0]
