class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            match x:
                case '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))
                case _:
                    stack.append(int(x))
            # print(stack[-1])
        return stack[0]