maps = [1, 2, 1]
class Solution:
    def minimumLength(self, s: str) -> int:
        # 0: 0
        # odd: 1
        # even: 2
        # 0 -> 1 -> 2 -> 1 -> ...
        result = 0
        counts = defaultdict(int)
        for x in s:
            change = maps[counts[x]] - counts[x]
            result += change
            counts[x] += change
        return result