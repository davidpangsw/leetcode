class Solution:
    def new21Game(self, n: int, k: int, m: int) -> float:
        # recursive relation:
        # given m = maxPts
        # P(n, k) = (1/m) * [ P(n-1, k-1) + P(n-2, k-2) + ... + P(n-m, k-m) ]
        # where:
        #     P(n, k) = 0 for n < 0
        #     P(n, k) = 1 for k <= 0 and n >= 0

        # Starting from P(0, k-n), keep the sum of previous m items, get the next by sum / m

        # total = 0.0

        # q = deque()
        # for i in range(0, n-k+1):
        #     q.append(1)
        #     # print(f"P({i}, {k-n+i}) = {cur}")

        #     if len(q) > m:
        #         total -= q.popleft()
        #     total += q[-1]
        size = min(m, n-k+1)
        q = [1]*size
        q = deque(q)
        total = size

        for i in range(n-k+1, n+1):
            q.append(total / m)
            # print(f"P({i}, {k-n+i}) = {cur}")

            if len(q) > m:
                total -= q.popleft()
            total += q[-1]
        return q[-1]

