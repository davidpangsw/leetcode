A = ord('a')
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        up_downs = [0 for _ in s] + [0]
        for start, end, direction in shifts:
            if direction:
                up_downs[start] += 1
                up_downs[end+1] -= 1
            else:
                up_downs[start] -= 1
                up_downs[end+1] += 1

        cur = 0
        result = ""
        for i, x in enumerate(s):
            cur += up_downs[i]
            result += chr((ord(x) - A + cur) % 26 + A)
        return result


