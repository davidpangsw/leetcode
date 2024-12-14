class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left  = 0
        right = 0

        total = 0
        counts = defaultdict(int)
        while left < len(nums):
            # print(nums[left:right])
            if right < len(nums):
                # print(nums[right], counts)
                if counts.keys():
                    keys = list(counts.keys())
                    M = max(max(keys), nums[right])
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

        return total


