class Solution:

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        for i in range(1, len(items)):
            items[i][1] = max(items[i-1][1], items[i][1])
        
        results = []
        for q in queries:
            if q < items[0][0]:
                results.append(0)
            else:
                # q exists => rightmost duplicate
                # q not exists => just smaller
                results.append(items[bisect_right(items, q, key=lambda x : x[0]) - 1][1])
        
        return results