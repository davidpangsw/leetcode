class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # group up the edges
        adjLists = [[] for _ in range(n)]
        for u, v in edges:
            adjLists[u].append(v)
            adjLists[v].append(u)
        
        result = 0

        # dfs starting from any point
        def dfs(u, fromNode):
            for v in adjLists[u]:
                if v == fromNode:
                    continue
                values[u] = (values[u] + dfs(v, u)) % k

            nonlocal result
            if values[u] % k == 0:
                result += 1

            return values[u]
        dfs(0, -1)
        return result
                


    def maxKDivisibleComponentsBFS(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # group up the edges
        adjLists = [set() for _ in range(n)]
        for u, v in edges:
            adjLists[u].add(v)
            adjLists[v].add(u)

        # starting from the leaves
        q = [u for u in range(n) if len(adjLists[u]) == 1]
        q = deque(q)

        # BFS from leaves (Toposort / Kahn's algorithm)
        result = 1 # last node must be a component itself
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