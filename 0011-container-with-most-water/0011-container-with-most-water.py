class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        left, right = 0, n-1
        while left < right:
            # if left > 0 and height[left] < height[left-1]:
            #     left += 1
            #     continue
            # if right < n-1 and height[right] < height[right+1]:
            #     right -= 1
            #     continue

            if height[left] < height[right]:
                result = max(result, height[left] * (right - left))
                left += 1
            elif height[left] > height[right]:
                result = max(result, height[right] * (right - left))
                right -= 1
            else:
                result = max(result, height[left] * (right - left))
                left += 1
                right -= 1

        return result