class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, x in enumerate(temperatures):
            while stack and stack[-1][1] < x:
                j, _ = stack.pop()
                result[j] = i-j
            stack.append((i, x))
        return result