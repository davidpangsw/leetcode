class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        heights.append(-1)
        lefts = [-1] * n
        rights = [n] * n

        result = 0
        stack = []
        for i, x in enumerate(heights):
            myLeft = -1
            while stack:
                j, left = stack[-1]
                if x < heights[j]:
                    stack.pop()
                    area = (i - left - 1) * heights[j]
                    if area > result:
                        result = area
                elif x > heights[j]:
                    myLeft = j
                    break
                else:
                    myLeft = left
                    break
            # print(i, myLeft)
            stack.append((i, myLeft))
        return result