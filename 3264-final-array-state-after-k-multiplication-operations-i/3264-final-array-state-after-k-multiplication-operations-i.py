class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = [(x, i) for i, x in enumerate(nums)]
        heapify(arr)
        for _ in range(k):
            x, i = heappop(arr)
            nums[i] = x * multiplier
            heappush(arr, (x * multiplier, i))
        return nums