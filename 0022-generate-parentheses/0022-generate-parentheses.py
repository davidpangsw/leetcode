def generateParenthesis(n: int):
    if n == 0:
        yield ''
        return
    if n == 1:
        yield '()'
        return

    for i in range(1, n+1):
        # i + (n-i) brackets
        # left part must be in a big bracket
        # i = 1, ..., n
        for left in generateParenthesis(i-1):
            for right in generateParenthesis(n-i):
                yield f"({left}){right}"

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return [x for x in generateParenthesis(n)]