class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        counts = [0, 0, 0]
        for c in s:
            counts[ord(c) - ord("a")] += 1
        if not (counts[0] >= k and counts[1] >= k and counts[2] >= k):
            return -1
        right = n
        
        result = n
        left = n
        while right >= 0 and left > 0:
            # print(right, left)
            if counts[0] >= k and counts[1] >= k and counts[2] >= k:
                result = min(result, right + (n - left))
                right -= 1
                counts[ord(s[right]) - ord("a")] -= 1 # in python, it is not an index error if right < 0 (doesn't matter here)
            else:
                left -= 1
                counts[ord(s[left]) - ord("a")] += 1
        return result



