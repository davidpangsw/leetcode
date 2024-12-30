class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        result = 0
        # productToPair = defaultdict(list)
        counts = [[0] * 1001 for _ in range(1001)]
        n = len(nums)
        for q in range(n - 5, 1, -1):
            r = q + 2
            for s in range(q+4, n):
                f = gcd(nums[r], nums[s])
                counts[nums[r] // f][nums[s] // f] += 1
            for p in range(q-1):
                f = gcd(nums[p], nums[q])
                result += counts[nums[q] // f][nums[p] // f]
        return result
                
        return result
