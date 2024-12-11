class Solution:
    def new21Game(self, n: int, k: int, m: int) -> float:
        # recursive relation:
        # given m = maxPts
        # P(n, k) = (1/m) * [ P(n-1, k-1) + P(n-2, k-2) + ... + P(n-m, k-m) ]
        # where:
        #     P(n, k) = 0 for n < 0
        #     P(n, k) = 1 for k <= 0 and n >= 0

        # Starting from P(0, k-n), keep the sum of previous m items, get the next by sum / m

        total = 0.0
        # q = deque()
        q = []
        left = 0
        for i in range(0, n+1):
            if i <= n-k:
                q.append(1)
            else:
                q.append(total / m)
            # print(f"P({i}, {k-n+i}) = {cur}")

            if len(q) - left > m:
                # total -= q.popleft()
                total -= q[left]
                left += 1
            total += q[-1]
        return q[-1]

