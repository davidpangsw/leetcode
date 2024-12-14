class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left  = right = 0

        total = 0
        counts = defaultdict(int)
        while left < len(nums) and right < len(nums):
            # print(nums[left:right])
            # print(nums[right], counts)
            keys = counts.keys()
            if keys:
                M = max(*keys, nums[right])
                m = min(*keys, nums[right])
            else:
                M = m = nums[right]

            if M - m <= 2:
                # accept it into subarray
                counts[nums[right]] += 1
                right += 1
                continue
            
            # process the subarray
            total += (right - left)

            # pop out the left item
            if counts[nums[left]] == 1:
                del counts[nums[left]]
            else:
                counts[nums[left]] -= 1
            left += 1
        # process the subarray
        size = right - left
        total += (size + 1) * size // 2

        return total


