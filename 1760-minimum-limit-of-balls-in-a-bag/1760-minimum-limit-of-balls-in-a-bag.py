class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 10^5 * log (10^9)
        # binary search on penality
        # given a penality, we know the maxOperations (or maxBags)
        s = sum(nums)

        maxBags = len(nums) + maxOperations
        left = ceil(s / maxBags)
        right = 10**9 # max(nums)
        while left < right:
            mid = (left + right) // 2

            #
            bags = sum([ceil(x / mid) for x in nums])
            if bags > maxBags:
                left = mid + 1
            else:
                right = mid
        return left

        # 10^9 * log (10^5)
        # # (-avg, nBags, total)
        # nums = [(-x, 1, x) for x in nums]
        # heapify(nums)

        # while maxOperations > 0:
        #     p, nBags, total = heappop(nums)
        #     if nums:
        #         pNext, nBagsNext, totalNext = nums[0]
        #         addedBags = ceil(total // (-pNext)) - nBags
        #         if addedBags <= 0:
        #             addedBags = 1
        #     else:
        #         addedBags = maxOperations

        #     nBags += addedBags
        #     p = -ceil(total / nBags)
        #     heappush(nums, (p, nBags, total))

        #     maxOperations -= 1
        # return -nums[0][0]
            
