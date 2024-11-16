class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # maximize the minimum number of stores assigned to each product

        # stores[i] = number of stores assigned to the i-th product type
        # at least one for each type
        m = len(quantities)

        # (-avg, q, s)
        # average items per store, total quantities, stores assigned
        data = [(-q, q, 1) for q in quantities]
        heapq.heapify(data)

        # for each store
        for i in range(n - m):
            # take the product type with maximum average items
            # assign the store to that type
            nAvg, q, s = heapq.heappop(data)
            s += 1

            # 11, 3 => 4
            # 10, 3 => 4
            # 9, 3 => 3
            # 8, 3 => 3
            avg = (q + (s-1)) // s
            heapq.heappush(data, (-avg, q, s))

        nAvg, q, s = heapq.heappop(data)
        return -nAvg
