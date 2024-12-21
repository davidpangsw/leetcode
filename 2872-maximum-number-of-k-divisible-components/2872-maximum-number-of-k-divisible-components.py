class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # group up the edges
        adjLists = [set() for _ in range(n)]
        for u, v in edges:
            adjLists[u].add(v)
            adjLists[v].add(u)

        # starting from the leaves
        q = [u for u in range(n) if len(adjLists[u]) == 1]
        q = deque(q)

        # BFS
        result = 1
        while len(q) > 1:
            # print(q)
            leaf = q.popleft()
            if values[leaf] % k == 0:
                result += 1
            parent = adjLists[leaf].pop()
            adjLists[parent].remove(leaf)
            values[parent] = (values[parent] + values[leaf]) % k

            if len(adjLists[parent]) == 1:
                q.append(parent)
        return result