class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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