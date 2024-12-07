class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # binary search on penality
        # given a penality, we know the maxOperations
        left = 1
        right = max(nums)

        maxBags = len(nums) + maxOperations

        while left < right:
            mid = (left + right) // 2

            #
            bags = 0
            for x in nums:
                bags += ceil(x / mid)
                if bags > maxBags:
                    break
            # print(left, right, mid, bags)

            if bags > maxBags:
                left = mid + 1
            elif bags < maxBags:
                right = mid
            else:
                right = mid
        return left

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
            
