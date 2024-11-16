class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        left = 1
        while left < n and arr[left] >= arr[left-1]:
            left += 1
        if left == n:
            return 0

        right = n
        while right > 0 and (right == n or arr[right-1] <= arr[right]) and arr[right-1] >= arr[left-1]:
            right -= 1
        # print("left, right=", left, right)

        result = right - left
        while right > 0 and (right == n or arr[right-1] <= arr[right]):
            right -= 1
            while left > 0 and arr[left-1] > arr[right]:
                left -= 1
            result = min(result, right - left)


        return result
        
        
        

        
        