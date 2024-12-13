class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0

        arr = [(x, i) for i, x in enumerate(nums)]
        heapify(arr)
        while arr:
            x, i = heappop(arr)
            if not nums[i]:
                continue

            score += x
            if i > 0:
                nums[i-1] = None
            if i < len(nums) - 1:
                nums[i+1] = None

        return score