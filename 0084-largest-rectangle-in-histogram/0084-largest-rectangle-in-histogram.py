class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)

        stack = []
        for i, x in enumerate(heights):
            myLeft = -1
            while stack:
                j, left = stack[-1]
                if x < heights[j]:
                    stack.pop()
                    heights[j] = (i - left - 1) * heights[j] # reuse heights to store the results
                elif x > heights[j]:
                    myLeft = j
                    stack.append([i, myLeft])
                    break
                else:
                    stack.pop()
                    myLeft = left
                    stack.append([i, myLeft])
                    break
            # print(i, myLeft)
            if not stack:
                stack.append([i, myLeft])
        return max(heights)