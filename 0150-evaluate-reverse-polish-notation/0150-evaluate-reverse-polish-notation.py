class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [None] * 10000
        size = 0
        for x in tokens:
            match x:
                case '+':
                    stack[size-2] += stack[size-1]
                    size -= 1
                case '-':
                    stack[size-2] -= stack[size-1]
                    size -= 1
                case '*':
                    stack[size-2] *= stack[size-1]
                    size -= 1
                case '/':
                    stack[size-2] = int(stack[size-2] / stack[size-1])
                    size -= 1
                case _:
                    stack[size] = int(x)
                    size += 1
        return stack[0]