class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                result[j] = i - stack.pop()
            stack.append(i)
        return result