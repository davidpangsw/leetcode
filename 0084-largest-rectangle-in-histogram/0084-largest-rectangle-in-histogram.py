class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)

        # stores (index, left boundary)
        stack = []
        for i, x in enumerate(heights):
            while stack:
                j, left = stack[-1]
                if x < heights[j]:
                    stack.pop()
                    heights[j] = (i - left - 1) * heights[j] # reuse heights to store the results
                elif x > heights[j]:
                    stack.append([i, j])
                    break
                else:
                    stack[-1][0] = i
                    break
            # print(i, myLeft)
            if not stack:
                stack.append([i, -1])
        return max(heights)