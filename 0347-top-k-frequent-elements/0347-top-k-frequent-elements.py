class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1

        arr = [(-counts[x], x) for x in counts]
        heapq.heapify(arr)

        return [heapq.heappop(arr)[1] for _ in range(k)]
