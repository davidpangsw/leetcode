class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left  = 0
        right = 0

        total = 0
        counts = defaultdict(int)
        while left < n:
            # print(nums[left:right])
            if right < n:
                # print(nums[right], counts)
                if counts.keys():
                    keys = list(counts.keys())
                    M = max(keys + [nums[right]])
                    m = min(keys + [nums[right]])
                else:
                    M = m = nums[right]

                if M - m <= 2:
                    # accept it into subarray
                    counts[nums[right]] += 1
                    right += 1
                    continue
            
            # process the subarray
            size = right - left
            total += size

            # pop out the left item
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            left += 1

        return total


