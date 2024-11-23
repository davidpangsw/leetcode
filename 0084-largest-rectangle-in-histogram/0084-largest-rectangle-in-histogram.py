stack = [None] * 100000
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)

        # stores (i, left boundary (exclusive) that heights[i] can extend)
        # stack = []
        st_size = 0
        for i, x in enumerate(heights):
            while st_size > 0:
                # j, left = stack[-1]
                # j = stack[-1][0]
                j = stack[st_size - 1][0]
                if x < heights[j]:
                    # i would be the right boundary that heights[j] can extend
                    # results[j] = (i - stack[-1][1] - 1) * heights[j] # reuse heights to store the results
                    # heights[j] *= (i - stack[-1][1] - 1) # reuse heights to store the results
                    # stack.pop()
                    st_size -= 1
                    heights[j] *= (i - stack[st_size][1] - 1) # reuse heights to store the results
                elif x > heights[j]:
                    # j would be the left boundary that heights[i] can extend
                    # stack.append([i, j])
                    stack[st_size] = [i, j]
                    st_size += 1
                    break
                else:
                    # replace the top item
                    # stack[-1][0] = i
                    stack[st_size-1][0] = i
                    break
            # print(i, myLeft)
            # if not stack:
            #     stack.append([i, -1])
            if st_size == 0:
                stack[st_size] = [i, -1]
                st_size += 1
        return max(heights)