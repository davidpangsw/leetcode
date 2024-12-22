class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)

        # parents = [-1 for i in range(n)]
        # st = []
        # for i in range(n):
        #     while st and heights[st[-1]] < heights[i]:
        #         parents[st.pop()] = i
        #     st.append(i)
        # # print("parents", parents)

        results = [-1 for _ in queries]
        query_groups = [[] for _ in heights]
        for i, q in enumerate(queries):
            a, b = q
            if a > b:
                a, b = b, a

            if heights[a] < heights[b] or a == b:
                results[i] = b
            else:
                h = max(heights[a], heights[b])
                query_groups[b].append((h, i))
        
        pq = []
        for i, h in enumerate(heights):
            # answer the queries before i
            while pq and pq[0][0] < h:
                _, query_id = heappop(pq)
                results[query_id] = i
            for q in query_groups[i]:
                heappush(pq, q)
        return results




