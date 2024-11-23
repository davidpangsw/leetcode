class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev_x = None
        for i, x in enumerate(numbers):
            if x == prev_x:
                continue
            # if y < x: # impossible
            #     break
            j = bisect_left(numbers, target - x, lo=i+1)
            if j < len(numbers) and numbers[j] == target - x:
                return i+1, j+1
        
        raise "Answer not found"