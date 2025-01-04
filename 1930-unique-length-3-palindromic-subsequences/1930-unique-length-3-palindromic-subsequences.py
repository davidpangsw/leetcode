class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # lasts = {x: i for i, x in enumerate(s)}
        inds = {}
        for i, x in enumerate(s):
            if x in inds:
                inds[x][1] = i
            else:
                inds[x] = [i, i]

        result = 0
        for x, t in inds.items():
            first, last = t
            result += len(set(s[first+1:last]))
    
        return result

        
        