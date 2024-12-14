class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total = 0
        left = 0
        right = 1
        curMax = curMin = nums[0]
        while left < len(nums) and right < len(nums):
            # print(nums[left:right], curMax, curMin)
            M = max(curMax, nums[right])
            m = min(curMin, nums[right])
            if M - m <= 2:
                # accept it into subarray
                curMax = M
                curMin = m
            else:
                # process the subarray
                size = right - left
                total += (size + 1) * size // 2

                # reset the subarray
                left = right
                curMax = curMin = nums[right]
                while abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    curMax = max(curMax, nums[left])
                    curMin = min(curMin, nums[left])

                # minus back to avoid double-count
                size = right - left
                total -= (size + 1) * size // 2

            right += 1

        # print(nums[left:right], curMax, curMin)

        # process the subarray
        size = right - left
        total += (size + 1) * size // 2

        return total


