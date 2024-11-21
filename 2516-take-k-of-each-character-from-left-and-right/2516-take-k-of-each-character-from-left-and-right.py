class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        counts = {
            "a": 0,
            "b": 0,
            "c": 0,
        }
        right = None
        for i, c in enumerate(s):
            counts[c] += 1
            if counts["a"] >= k and counts["b"] >= k and counts["c"] >= k:
                right = i+1
                break
        if right is None:
            return -1
        
        result = right
        right -= 1
        counts[s[right]] -= 1

        n = len(s)
        left = n
        while right >= 0 and left > 0:
            # print(right, left)
            if counts["a"] >= k and counts["b"] >= k and counts["c"] >= k:
                result = min(result, right+n-left)
                right -= 1
                counts[s[right]] -= 1
            else:
                left -= 1
                counts[s[left]] += 1
        return result



