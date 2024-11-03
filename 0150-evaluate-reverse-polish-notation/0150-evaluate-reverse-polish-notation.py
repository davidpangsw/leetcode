class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = tokens # reuse tokens as stack, to reduce the memory overhead
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