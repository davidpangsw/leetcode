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
        # use an array to implement the deque
        # q = deque()
        q = list(range(n+1))
        q_from, q_to = 0, 0


        result = n+1
        for i in range(n+1):
            while q_to - q_from > 0 and sums[i] - sums[q[q_from]] >= k:
                result = min(result, i-q[q_from])
                q_from += 1
            
            # larger prefix sum => cannot be the left of the subarray
            while q_to - q_from > 0 and sums[q[q_to-1]] >= sums[i]:
                q_to -= 1
            # use binary search as q is monotone
            ind = bisect_left(q, sums[i], lo=q_from, hi=q_to)

            q[q_to] = i
            q_to += 1
            # for diff in range(1, min(result, n+1-i)):
            #     if sums[i+diff] - sums[i] >= k:
            #         result = diff
            #         break
        if result == n+1:
            return -1
        return result