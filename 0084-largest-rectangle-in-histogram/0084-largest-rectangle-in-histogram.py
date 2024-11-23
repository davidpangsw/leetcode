class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lefts = [-1] * n
        rights = [n] * n
        results = [0] * n

        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                rights[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                lefts[stack.pop()] = i
            stack.append(i)
        # return max(results)

        result = 0
        for i in range(n):
            # results[i] = (rights[i] - lefts[i] - 1) * heights[i]
            area = (rights[i] - lefts[i] - 1) * heights[i]
            if area > result:
                result = area
        
        return result
