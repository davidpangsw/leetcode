class Solution:
    def new21Game(self, n: int, k: int, m: int) -> float:
        # recursive relation:
        # given m = maxPts
        # P(n, k) = (1/m) * [ P(n-1, k-1) + P(n-2, k-2) + ... + P(n-m, k-m) ]
        # where:
        #     P(n, k) = 0 for n < 0
        #     P(n, k) = 1 for k <= 0 and n >= 0

        # (Suppose n >= k)
        # Starting from P(0, k-n), keep the sum of previous m items, get the next by sum / m

        total = 0
        q = deque()
        # print(f"P({0}, {k-n}) = {1}")
        for i in range(0, n+1):
            if k-n+i <= 0:
                cur = 1
            else:
                cur = total / m

            # print(f"P({i}, {k-n+i}) = {cur}")

            if len(q) == m:
                total -= q.popleft()
            total += cur
            q.append(cur)
        return q[-1]

