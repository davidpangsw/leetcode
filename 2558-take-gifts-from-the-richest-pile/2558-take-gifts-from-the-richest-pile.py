class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        arr = [-gifts[i] for i in range(len(gifts))]
        heapify(arr)
        while k > 0:
            p = heappop(arr)
            heappush(arr, -floor(sqrt(-p)))
            k -= 1
        return -sum(arr)

