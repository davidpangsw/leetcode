class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = [-1] * (n-k+1)

        left, right = 0, 0
        while left < len(results):
            # suppose [left, right] forms a good subarray
            if right + 1 - left == k:
                results[left] = nums[right]
                left += 1
            else:
                if right + 1 < n and nums[right+1] == nums[right] + 1:
                    right += 1
                else:
                    left, right = right + 1, right + 1
        return results
