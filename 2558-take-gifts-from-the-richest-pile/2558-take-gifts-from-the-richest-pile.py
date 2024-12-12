class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        arr = [-gifts[i] for i in range(len(gifts))]
        heapify(arr)
        for i in range(k):
            p = heappop(arr)
            heappush(arr, -int(sqrt(-p)))
        return -sum(arr)

