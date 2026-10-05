class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        count = 0
        for c in s:
            if (c == '('):
                count += 1
            else:
                count -= 1
                if (prev == '('):
                    score += 1 << count
            prev = c
        return score
        