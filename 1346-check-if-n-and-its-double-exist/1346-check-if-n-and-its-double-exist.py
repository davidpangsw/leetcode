class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero = False
        data = set()
        for i, x in enumerate(arr):
            data.add(x)
            if x == 0:
                if zero:
                    return True
                zero = True

        for i, x in enumerate(arr):
            if x == 0:
                continue
            if (x << 1) in data:
                return True
        return False