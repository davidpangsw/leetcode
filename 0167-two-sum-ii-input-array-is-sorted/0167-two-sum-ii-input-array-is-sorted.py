class Solution:
    # binary search on both pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)
        while True:
            # print(left, right)

            # fix left, find right
            y = target - numbers[left]
            newRight = bisect_left(numbers, y, lo=left+1, hi=right)
            if newRight < len(numbers) and numbers[newRight] == y:
                return left+1, newRight+1
            right = newRight - 1
            # print(left, right)

            # fix right, find left
            y = target - numbers[right]
            newLeft = bisect_right(numbers, y, lo=left, hi=right-1)
            if numbers[newLeft] == y:
                return newLeft+1, right+1
            left = newLeft - 1
            

    
    def twoSumStandard(self, numbers: List[int], target: int) -> List[int]:
        prev_x = None
        for i, x in enumerate(numbers):
            if x == prev_x:
                continue
            y = target - x
            j = bisect_left(numbers, y, lo=i+1)
            if j < len(numbers) and numbers[j] == y:
                return i+1, j+1
            prev_x = x
        
        raise "Answer not found"