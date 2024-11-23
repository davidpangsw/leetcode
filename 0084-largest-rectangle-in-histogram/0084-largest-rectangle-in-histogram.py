class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        results = []
        stack = []
        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] > x:
                j = stack.pop()
                area = (i-j)* heights[j]
                results.append(area)
                # print(i, j, area)
            if not stack:
                stack.append(i)
            elif heights[stack[-1]] < x:
                stack.append(i)
            else:
                pass
        
        return max(results)
