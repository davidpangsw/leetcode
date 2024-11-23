class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lefts = [-1] * n
        rights = [n] * n

        st1, st2 = [], []
        for i in range(n):
            while st1 and heights[i] < heights[st1[-1]]:
                rights[st1.pop()] = i
            st1.append(i)

            j = n-1-i
            while st2 and heights[j] < heights[st2[-1]]:
                lefts[st2.pop()] = j
            st2.append(j)
        # results = [0] * n
        # return max(results)

        result = 0
        for i in range(n):
            # results[i] = (rights[i] - lefts[i] - 1) * heights[i]
            area = (rights[i] - lefts[i] - 1) * heights[i]
            if area > result:
                result = area
        
        return result
