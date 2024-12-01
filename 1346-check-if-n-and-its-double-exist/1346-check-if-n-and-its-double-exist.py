class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i, x in enumerate(arr):
            d = (x << 1)

            if x > 0:
                ind = bisect_left(arr, d, i)
            elif x < 0:
                ind = bisect_left(arr, d, 0, i)
            else:
                if i > 0:
                    ind = i - 1
                else:
                    ind = i
            if ind == len(arr):
                break
            if arr[ind] == d:
                return True
        return False