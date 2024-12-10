class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 0, 1
        # 00, 10, 11, 01
        # 000, 100, 110, 010, 011, 111, 101, 001

        # 0  ,                               1
        # 00 ,           01 , 11 ,           10
        # 000, 001, 011, 010, 110, 111, 101, 100
        # ...
        def helper(n: int, result):
            if n == 1:
                result.append(0)
                result.append(1)
                return

            helper(n-1, result)
            m = len(result)
            for i in range(m):
                result[i] = result[i] << 1
            for i in range(m-1, -1, -1):
                result.append(result[i] + 1)
        result = []
        helper(n, result)
        return result