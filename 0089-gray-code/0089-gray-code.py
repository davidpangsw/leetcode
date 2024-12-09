class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 0, 1
        # 00, 01, 11, 10
        # 000, 001, 011, 010, 110, 111, 101, 100
        # ...
        def helper(n: int):
            if n == 1:
                yield 0
                yield 1
                return

            gen = helper(n-1)
            while True:
                try:
                    x = next(gen)
                    y = next(gen)
                    yield (x << 1)
                    yield (x << 1) + 1
                    yield (y << 1) + 1
                    yield (y << 1)
                except StopIteration:
                    break
        return list(helper(n))