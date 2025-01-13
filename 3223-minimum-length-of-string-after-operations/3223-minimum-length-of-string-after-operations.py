maps = [1, 2, 1]
class Solution:
    def minimumLength(self, s: str) -> int:
        # 0: 0
        # odd: 1
        # even: 2
        # 0 -> 1 -> 2 -> 1 -> ...
        counts = defaultdict(int)
        for c in s:
            counts[c] = maps[counts[c]]
        return sum(counts.values())