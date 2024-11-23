class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lefts = [-1] * n
        rights = [n] * n

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
        
        # print(lefts)
        # print(rights)

        results = [0] * n
        for i in range(n):
            left, right = lefts[i], rights[i]
            area = (right - left - 1) * heights[i]
            results[i] = area
        
        return max(results)
