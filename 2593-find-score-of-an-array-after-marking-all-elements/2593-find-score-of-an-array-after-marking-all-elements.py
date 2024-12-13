class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0

        visited = set()
        arr = [(x, i) for i, x in enumerate(nums)]
        heapify(arr)
        while arr:
            x, i = heappop(arr)
            if i in visited:
                continue

            score += x
            visited.add(i-1)
            visited.add(i+1)

        return score