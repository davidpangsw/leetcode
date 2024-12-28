class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        st = [values[0] + 0] # decreasing
        n = len(values)
        result = -1
        for j in range(1, n):
            result = max(result, values[j] - j + st[0])
            while st and st[-1] < values[j] + j:
                st.pop()
            st.append(values[j] + j)
        return result