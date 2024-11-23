class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)
        while True:
            # print(left, right)

            # fix left, find right
            x = numbers[left]
            y = target - x
            newRight = bisect_left(numbers, y, lo=left+1, hi=right)
            if newRight < len(numbers) and numbers[newRight] == y:
                return left+1, newRight+1
            right = newRight - 1
            # print(left, right)

            # fix right, find left
            x = numbers[right]
            y = target - x
            newLeft = bisect_left(numbers, y, lo=left, hi=right-1)
            if numbers[newLeft] == y:
                return newLeft+1, right+1
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