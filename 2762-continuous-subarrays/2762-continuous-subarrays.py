class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total = 0
        left = 0
        curMax = curMin = nums[0]
        n = len(nums)
        for right in range(1, n):
            # print(nums[left:right], curMax, curMin)
            M = max(curMax, nums[right])
            m = min(curMin, nums[right])
            if M - m <= 2:
                # accept it into subarray
                curMax = M
                curMin = m
            else:
                # process the subarray
                total += (right - left + 1) * (right - left) // 2

                # reset the subarray
                left = right
                curMax = curMin = nums[right]
                while abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    curMax = max(curMax, nums[left])
                    curMin = min(curMin, nums[left])

                # minus back to avoid double-count
                total -= (right - left + 1) * (right - left) // 2
            # print(total)

        # print(nums[left:], curMax, curMin)

        # process the subarray
        total += (n - left + 1) * (n - left) // 2

        return total


