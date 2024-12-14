class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = right = 0

        total = 0
        incQ = deque()
        decQ = deque()
        while left < len(nums) and right < len(nums):
            # print(nums[left:right])
            while incQ and nums[incQ[-1]] > nums[right]:
                incQ.pop()
            if not incQ or incQ[-1] != right:
                incQ.append(right)
            
            while decQ and nums[decQ[-1]] < nums[right]:
                decQ.pop()
            if not decQ or decQ[-1] != right:
                decQ.append(right)
            
            if nums[decQ[0]] - nums[incQ[0]] <= 2:
                right += 1
                continue
            
            # process the subarray
            # print(right - left, incQ, decQ)
            total += (right - left)

            # pop out the left item
            if left == incQ[0]:
                incQ.popleft()
            if left == decQ[0]:
                decQ.popleft()

            left += 1

        # process the subarray
        total += (right - left + 1) * (right - left) // 2

        return total


