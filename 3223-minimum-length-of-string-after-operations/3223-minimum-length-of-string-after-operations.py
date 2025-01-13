maps = [1, 2, 1]
changes = [1, 1, -1]
class Solution:
    def minimumLength(self, s: str) -> int:
        # 0: 0
        # odd: 1
        # even: 2
        # 0 -> 1 -> 2 -> 1 -> ...
        result = 0
        counts = defaultdict(int)
        for x in s:
            c = counts[x]
            result += changes[c]
            counts[x] = maps[c]
        return result