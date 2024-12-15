class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # p / n -> (p+1) / (n+1)
        # d * n(n+1) = (pn + n) - (pn + p) = n - p
        # d = (n-p) / (n * (n+1))

        arr = [(p/n - (p+1)/(n+1), p, n) for p, n in classes]
        # arr = [(-((p+1) / (n+1) - p / n), p, n) for p, n in classes]
        heapify(arr)
        for _ in range(extraStudents):
            _, p, n = heappop(arr)
            # print(p, n)
            # p, n = p+1, n+1
            # heappush(arr, (-(n-p) / (n * (n+1)), p, n))
            heappush(arr, ((p+1)/(n+1) - (p+2)/(n+2), p+1, n+1))
        # print(arr)
        return sum([p / n for _, p, n in arr]) / len(arr)


