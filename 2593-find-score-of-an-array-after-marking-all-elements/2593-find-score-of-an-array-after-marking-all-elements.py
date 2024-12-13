class Solution:
    def findScore(self, nums: List[int]) -> int:
        # O(n)
        # Observations:
        #   1. If an element is smaller than its neighbourhoods, then it will be eventually chosen
        #   2. If an element is chosen, then its neighbourhoods will not be chosen
        # Steps:
        #   1. Loop the elements, accumulate a decreasing subarray.
        #   2. Every time the subarray stops to be decreasing, it means that a local minimum, M, is identified
        #   3. Add all the elements on and before M alternatively
        #   4. Starting from the next of next element of M, repeat 1-3
        
        nums.append(inf)
        score = 0

        left = 0
        i = 1
        while i < len(nums):
            if nums[i] >= nums[i-1]:
                # print(nums[left: i])
                
                # now, nums[i-1] is a local minimum
                # score += sum(nums[i-1:left-1:-2])
                # print(i-1, left-1, nums[i-1:left-1:-2])
                for j in range(i-1, left-1, -2):
                    score += nums[j]
                
                left = i+1
                i += 2
            else:
                i += 1

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