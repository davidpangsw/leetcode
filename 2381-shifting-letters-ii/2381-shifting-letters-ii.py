class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        up_downs = [0] * (n+1)
        for start, end, direction in shifts:
            if direction:
                up_downs[start] += 1
                up_downs[end+1] -= 1
            else:
                up_downs[start] -= 1
                up_downs[end+1] += 1

        cur = 0
        result = ""
        A = ord('a')
        for i, x in enumerate(s):
            cur += up_downs[i]
            x = (ord(x) - A + cur) % 26
            x = chr(x + A)
            result += x
        return result


