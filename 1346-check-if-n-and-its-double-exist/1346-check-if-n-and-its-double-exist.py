class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero = False
        data = set()
        for i, x in enumerate(arr):
            if x == 0:
                if zero:
                    return True
                zero = True
            else:
                data.add(x)

        for i, x in enumerate(arr):
            if (x << 1) in data or (x / 2) in data:
                return True
        return False