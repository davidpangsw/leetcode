maps = [1, 2, 1]
class Solution:
    def minimumLength(self, s: str) -> int:
        # 0: 0
        # odd: 1
        # even: 2
        # 0 -> 1 -> 2 -> 1 -> ...
        result = 0
        counts = defaultdict(int)
        for c in s:
            result += (maps[counts[c]] - counts[c])
            counts[c] = maps[counts[c]]
        return result