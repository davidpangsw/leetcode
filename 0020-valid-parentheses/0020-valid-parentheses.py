class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ['(', '[', '{']:
                stack.append(x)
                continue
            
            if stack and stack[-1]+x in ['()', '[]', '{}']:
                stack.pop()
            else:
                return False
        return not stack