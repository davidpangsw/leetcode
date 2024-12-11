class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # consider the intervals [nums[i] - k, nums[i] + k]
        # the answer would be the maximum count of overlaps
        # use a queue to store all overlapping intervals (represented by two pointer)
        q = deque()
        heapify(nums)
        q.append(heappop(nums))
        result = 1
        while nums:
            x = heappop(nums)
            q.append(x)

            # dequeue all non-overlapping intervals
            # we don't need to dequeue all in practice, as it doesn't affect the maximum count
            while q[0] + k < x - k:
                q.popleft()

            # # binary search the left index
            # p = bisect_left(nums, nums[i] - 2 * k, lo=p, hi=i)

            # now, all intervals in queue are overlapping
            result = max(result, len(q))
        return result

