class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # prefix sum
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i+1] = sums[i] + nums[i]
        # sums[i] = sum(nums[:i])
        # sums[i] - nums[j] = sum[i:j]
        # print(sums) 

        # "left" of the sliding windows
        q = deque()

        result = n+1
        for i in range(n+1):
            while q and sums[i] - sums[q[0]] >= k:
                result = min(result, i-q[0])
                q.popleft()
            
            # larger prefix sum => cannot be the left of the subarray
            while q and sums[q[-1]] >= sums[i]:
                q.pop()

            q.append(i)
            # for diff in range(1, min(result, n+1-i)):
            #     if sums[i+diff] - sums[i] >= k:
            #         result = diff
            #         break
        if result == n+1:
            return -1
        return result