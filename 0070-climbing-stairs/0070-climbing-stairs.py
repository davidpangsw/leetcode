# arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903]

SQRT5 = math.sqrt(5)
PHI = (1+SQRT5) / 2
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        # f(1) = 1
        # f(2) = 2
        # Fibonacci sequence
        return round(math.pow(PHI, n+1) / SQRT5)

        # return arr[n-1]