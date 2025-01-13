class Solution:
    def minimumLength(self, s: str) -> int:
        # 1 -> 1
        # 2 -> 2
        # 3 -> 1
        # 4 -> 2
        # 5 -> 1
        return sum([1 if x % 2 == 1 else 2 for x in Counter(s).values()])