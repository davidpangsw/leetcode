class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = [set([i+1]) for i in range(n-1)]
        edges.append(set())

        results = []

        # remember steps to each node
        steps = list(range(n))
        # print(steps)

        for u, v in queries:
            edges[u].add(v)
            if steps[u] + 1 < steps[v]:
                steps[v] = steps[u] + 1

                # BFS starting from v
                q = deque([v])
                while q:
                    node = q.popleft()
                    for dest in edges[node]:
                        if steps[node] + 1 <= steps[dest]:
                            steps[dest] = steps[node] + 1
                            q.append(dest)
            results.append(steps[n-1])
            # print(steps)
       
        return results
