class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero = False
        data = {}
        for i, x in enumerate(arr):
            data[x] = i
            if x == 0:
                if zero:
                    return True
                zero = True

        for i, x in enumerate(arr):
            if x == 0:
                continue
            d = x << 1
            if d in data:
                return True
        return False