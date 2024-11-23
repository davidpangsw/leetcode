class Solution:
    # binary search on both pointers
    def twoSum(self, numbers: List[int], target: int, left: int) -> List[int]:
        print(numbers, f"Find {target} in {numbers[left:]}")
        right = len(numbers)
        while left < right-1:
            print(left, right, numbers[left:right])

            # fix left, find right
            y = target - numbers[left]
            print(f"fix left={numbers[left]}, find {y} in {numbers[left+1:right]}")
            newRight = bisect_left(numbers, y, lo=left+1, hi=right)
            if newRight < len(numbers) and numbers[newRight] == y:
                yield left, newRight
            right = newRight
            print(left, right, numbers[left:right])

            if left >= right:
                break

            # fix right, find left
            y = target - numbers[right-1]
            print(f"fix right={numbers[right-1]}, find {y} in {numbers[left:right-1]}")
            newLeft = bisect_right(numbers, y, lo=left, hi=right-1)
            if newLeft-1 >= left and numbers[newLeft-1] == y:
                yield newLeft - 1, right - 1
            left = newLeft
        # print("twoSum exits")
        return

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, x in enumerate(nums):
            if i >= 1 and nums[i-1] == nums[i]:
                continue
            for pair in self.twoSum(nums, -x, i+1):
                print(i, "found pair", pair)
                result.append([nums[i], nums[pair[0]], nums[pair[1]]])
        return result