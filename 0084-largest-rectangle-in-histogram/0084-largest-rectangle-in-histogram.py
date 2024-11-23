class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)

        # result = 0
        stack = []
        for i, x in enumerate(heights):
            myLeft = -1
            while stack:
                j, left = stack[-1]
                if x < heights[j]:
                    stack.pop()
                    heights[j] = (i - left - 1) * heights[j]
                    # result = max(result, (i - left - 1) * heights[j])
                    # area = (i - left - 1) * heights[j]
                    # if area > result:
                    #     result = area
                elif x > heights[j]:
                    myLeft = j
                    break
                else:
                    stack.pop()
                    myLeft = left
                    break
            # print(i, myLeft)
            stack.append((i, myLeft))
        # return result
        return max(heights)