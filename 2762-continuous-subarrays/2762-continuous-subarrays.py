class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = right = 0

        total = 0
        incQ = deque() # To manage the min (with the ability to update when we pop out leftmost item)
        decQ = deque() # To manage the max
        for right in range(len(nums)):
            # print(nums[left:right])
            while incQ and nums[incQ[-1]] > nums[right]:
                incQ.pop()
            incQ.append(right)
            
            while decQ and nums[decQ[-1]] < nums[right]:
                decQ.pop()
            decQ.append(right)
            
            while incQ and decQ and nums[decQ[0]] - nums[incQ[0]] > 2:
                # process the subarray
                # print(right - left, incQ, decQ)
                total += (right - left)

                # pop out the left item
                if left == incQ[0]:
                    incQ.popleft()
                elif left == decQ[0]:
                    decQ.popleft()
                left += 1
            

        # process the subarray
        total += (len(nums) - left + 1) * (len(nums) - left) // 2

        return total


