class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)

        # stores (index, left boundary)
        stack = []
        for i, x in enumerate(heights):
            while stack:
                j, left = stack[-1]
                if x < heights[j]:
                    # i would be the right boundary that heights[j] can extend
                    stack.pop()
                    heights[j] = (i - left - 1) * heights[j] # reuse heights to store the results
                elif x > heights[j]:
                    # the top item would be the left boundary that heights[i] can extend
                    stack.append([i, j])
                    break
                else:
                    # replace the top item
                    stack[-1][0] = i
                    break
            # print(i, myLeft)
            if not stack:
                stack.append([i, -1])
        return max(heights)