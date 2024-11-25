class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        curLevel = 0
        left, right = 0, len(height)-1

        while left < right:
            h1, h2 = height[left], height[right]

            # if both dirts are high, change the curLevel, include more water
            if min(h1, h2) > curLevel:
                newLevel = min(h1, h2)
                total += (right - left - 1) * (newLevel - curLevel)
            else:
                newLevel = curLevel

            # remove the water occupied by dirt
            # move the pointer
            if h1 <= h2:
                total -= min(height[left], curLevel)
                left += 1
            else:
                total -= min(height[right], curLevel)
                right -= 1

            curLevel = newLevel
        return total