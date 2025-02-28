class Solution:
    # binary search on both pointers
    def twoSum(self, numbers: List[int], target: int, left: int) -> List[int]:
        # print(numbers, f"Find {target} in {numbers[left:]}")
        right = len(numbers)
        while left < right - 1:
            # print(left, right, numbers[left:right])

            # fix left, find right
            y = target - numbers[left]
            # print(f"fix left={numbers[left]}, find {y} in {numbers[left+1:right]}")
            ind = bisect_left(numbers, y, lo=left+1, hi=right)
            # if exact value is found, yield the pair
            if ind < right and numbers[ind] == y:
                yield left, ind
            right = ind
            # print(left, right, numbers[left:right])

            if left >= right - 1:
                break

            # fix right, find left
            y = target - numbers[right-1]
            # print(f"fix right={numbers[right-1]}, find {y} in {numbers[left:right-1]}")
            ind = bisect_right(numbers, y, lo=left, hi=right-1)
            # if exact value is found, yield the pair
            if ind > left and numbers[ind-1] == y:
                yield ind - 1, right - 1
            left = ind
        # print("twoSum exits")
        return

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prev_x = None
        for i, x in enumerate(nums):
            if x == prev_x:
                continue
            for pair in self.twoSum(nums, -x, i+1):
                # print(i, "found pair", pair)
                result.append([nums[i], nums[pair[0]], nums[pair[1]]])
            prev_x = x
        return result