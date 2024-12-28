class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        arr = []
        arr.append(sum(nums[:k]))
        # arr.append((-sum(nums[:k]), 0))
        for i in range(1, len(nums)-k+1):
            # nS, _ = arr[-1]
            # s = -nS - nums[i-1] + nums[i-1+k]
            # arr.append((-s, i))
            s = arr[-1]
            s = s - nums[i-1] + nums[i-1+k]
            arr.append(s)
        # print(arr)
        
        # arr.sort()
        # heapify(arr)
        total = -1
        result = []
        nums = arr

        # find max non-k-neighbouring 3-sum in arr
        n = len(nums)

        prefixMax = [(nums[0], 0)] + [None] * (n-1)
        for i in range(1, n):
            s, j = prefixMax[i-1]
            if nums[i] > s:
                prefixMax[i] = nums[i], i
            else:
                prefixMax[i] = s, j
        # print(prefixMax)

        prefixMax2 = [(-1, -1, -1)] * n
        for i in range(k, n):
            a = nums[i]
            b, j = prefixMax[i-k]
            prev = prefixMax2[i-1]
            if a+b > prev[0]:
                prefixMax2[i] = a+b, j, i
            else:
                prefixMax2[i] = prev
        # print(prefixMax2)

        result = (-1, [-1, -1, -1])
        for i in range(k, n):
            a = nums[i]
            b, x, y = prefixMax2[i-k]
            if a + b > result[0]:
                result = a+b, [x, y, i]
        return result[1]
