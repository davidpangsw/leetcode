class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, len(height)-1
        max1, max2 = 0, 0
        while left <= right:
            # print(height[left:right+1], max1, max2)
            if max1 <= max2:
                if max1 > height[left]:
                    total += max1 - height[left]
                else:
                    max1 = height[left]
                left += 1
            else:
                if max2 > height[right]:
                    total += max2 - height[right]
                else:
                    max2 = height[right]
                right -= 1
            # print(total)
        return total