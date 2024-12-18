class Solution:
    # binary search on both pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)
        while True:
            print(left, right)

            # fix left, find right
            y = target - numbers[left]
            newRight = bisect_left(numbers, y, lo=left+1, hi=right)
            if newRight < right and numbers[newRight] == y:
                return left+1, newRight+1
            right = newRight
            print(left, right)

            # fix right, find left
            y = target - numbers[right-1]
            newLeft = bisect_right(numbers, y, lo=left, hi=right-2)
            if newLeft > left and numbers[newLeft-1] == y:
                return newLeft-1+1, right
            left = newLeft
            

    
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