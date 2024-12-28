class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        arr = [sum(nums[:k])]
        for i in range(1, len(nums)-k+1):
            arr.append(arr[-1] - nums[i-1] + nums[i-1+k])
        # print(arr)
        n = len(arr)
        
        # find max non-k-neighbouring 1-sum in arr
        prefixMax = [0] * n
        for i in range(1, n):
            prefixMax[i] = i if arr[i] > arr[prefixMax[i-1]] else prefixMax[i-1]
        # print(prefixMax)

        # find max non-k-neighbouring 2-sum in arr
        prefixMax2 = [(-1, -1, -1)] * n
        for i in range(k, n):
            j = prefixMax[i-k]
            prev = prefixMax2[i-1]
            if arr[i] + arr[j] > prev[0]:
                prefixMax2[i] = arr[i] + arr[j], j, i
            else:
                prefixMax2[i] = prev
        # print(prefixMax2)

        # find max non-k-neighbouring 3-sum in arr
        result = (-1, [-1, -1, -1])
        for i in range(k, n):
            a = arr[i]
            b, x, y = prefixMax2[i-k]
            if a + b > result[0]:
                result = a + b, [x, y, i]
        return result[1]
