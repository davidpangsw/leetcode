class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lefts = [-1] * n
        rights = [n] * n
        results = [0] * n

        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                rights[j] = i
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                lefts[j] = i
            stack.append(i)

        for i in range(n):
            results[i] = (rights[i] - lefts[i] - 1) * results[i]
        
        return max(results)
