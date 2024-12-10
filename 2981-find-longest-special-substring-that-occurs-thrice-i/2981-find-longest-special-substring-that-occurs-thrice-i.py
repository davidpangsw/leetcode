class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        table = [[] for _ in range(26)]

        count = 1
        for i in range(1, n):
            x = ord(s[i]) - ord('a')
            if s[i] == s[i-1]:
                count += 1
            else:
                prev = ord(s[i-1]) - ord('a')
                table[prev].append(count)
                count = 1

        prev = ord(s[-1]) - ord('a')
        table[prev].append(count)
        print(table)
            
        result = 0
        for x in range(26):
            if not table[x]:
                continue
            s = sorted(table[x])

            if len(s) == 1:
                # 1 number
                # a-2
                result = max(result, s[0] - 2)
            elif len(s) == 2:
                # 2 numbers (a <= b)
                # b-2
                # min(a, b-1)
                # a-1
                # X a-2 X
                result = max(result, s[1]-2, min(s[0], s[1]-1), s[0]-1)
            else:
                # 3 numbers (a <= b <= c)
                # c-2
                # min(b, c-1)  ; X min(a, c-1) X
                # b-1          ; X a-1 X
                # a
                result = max(result, s[-1] - 2, min(s[-2], s[-1]-1), s[-2] - 1, s[-3])




        return result if result > 0 else -1
