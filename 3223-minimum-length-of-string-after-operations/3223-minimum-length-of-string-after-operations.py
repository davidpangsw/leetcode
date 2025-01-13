class Solution:
    def minimumLength(self, s: str) -> int:
        # 0 -> 0
        # odd -> 1
        # even -> 2
        counts = {}
        for c in s:
            if c in counts:
                counts[c] = 3 - counts[c]
            else:
                counts[c] = 1
        return sum(counts.values())