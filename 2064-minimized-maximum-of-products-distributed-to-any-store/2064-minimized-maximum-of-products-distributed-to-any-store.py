class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high = 1, max(quantities)

        while low < high:
            mid = (low + high) // 2

            # math.ceil(q / mid)
            if n >= sum([(q + (mid-1)) // mid for q in quantities]):
                # enough stores, reduce the amount
                high = mid
            else:
                low = mid + 1
        
        return high


    def minimizedMaximum2(self, n: int, quantities: List[int]) -> int:
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
            # avg = q // s, but add one more if remainder not zero
            # or use math.ceil(q / s)
            avg = (q + (s-1)) // s
            heapq.heappush(data, (-avg, q, s))

        nAvg, q, s = heapq.heappop(data)
        return -nAvg
