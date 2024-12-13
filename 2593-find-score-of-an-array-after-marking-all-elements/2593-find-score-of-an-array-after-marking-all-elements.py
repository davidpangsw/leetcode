class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Observations:
        #   1. If an element is smaller than its neighbourhoods, than it must be chosen
        #   2. If an element is chosen, then its greater neighbourhoods must not be chosen
        # Loop the elements, every time a local minimum is identified, add all the elements on and before it alternatively
        # This can achieve O(n)
        score = 0
        n = len(nums)

        left = 0
        i = 1
        while i < n:
            if nums[i] < nums[i-1]:
                i += 1
                continue
            
            # print(nums[left: i])
            
            # now, nums[i-1] is a local minimum
            for j in range(i-1, left-1, -2):
                score += nums[j]
            
            left = i+1
            i += 2
        
        # print(nums[left: n])
        
        if left < n:
            # now, nums[i-1] is a local minimum
            for j in range(n-1, left-1, -2):
                score += nums[j]

        return score




    def findScoreSlow(self, nums: List[int]) -> int:
        score = 0

        arr = [(x, i) for i, x in enumerate(nums)]
        heapify(arr)
        while arr:
            x, i = heappop(arr)
            if not nums[i]:
                continue

            score += x
            if i > 0:
                nums[i-1] = None
            if i < len(nums) - 1:
                nums[i+1] = None

        return score