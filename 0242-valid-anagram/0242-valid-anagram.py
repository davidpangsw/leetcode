class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for x in s:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        
        for x in t:
            if x not in counts or counts[x] == 0:
                return False
            counts[x] -= 1
        return True