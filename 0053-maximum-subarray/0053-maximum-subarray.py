class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # queue = new Queue([nums[0]])
        left = 0
        right = 0
        
        s = nums[0]
        result = nums[0]

        i = 1
        while i < n:
            if s <= 0 and left <= right: # queue is not empty:
                # a = queue.dequeue()
                # s -= a
                s -= nums[left]
                left += 1
                continue
            
            s += nums[i]
            # queue.enqueue(nums[i])
            right += 1
            result = max(result, s)

            i += 1

        return result
        