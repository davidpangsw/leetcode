class Solution:
    def new21Game(self, n: int, k: int, m: int) -> float:
        # recursive relation:
        # given m = maxPts
        # P(n, k) = (1/m) * [ P(n-1, k-1) + P(n-2, k-2) + ... + P(n-m, k-m) ]
        # where:
        #     P(n, k) = 0 for n < 0
        #     P(n, k) = 1 for k <= 0 and n >= 0

        # Starting from P(0, k-n), keep the sum of previous m items, get the next by sum / m


        q = deque([1] * min(m, n-k+1))
        total = len(q)

        for _ in range(0, k):
            q.append(total / m)
            # print(f"P({_+n+1-k}, {_+1}) = {cur}")

            if len(q) > m:
                total -= q.popleft()
            total += q[-1]
        return q[-1]

