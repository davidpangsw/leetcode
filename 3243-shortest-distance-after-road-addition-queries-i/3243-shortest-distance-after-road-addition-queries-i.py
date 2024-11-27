class Solution:
    def shortestDistanceAfterQueriesDP(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = [set([i+1]) for i in range(n-1)]
        dist = [n-1-i for i in range(n)]

        results = []
        for query in queries:
            x, y = query
            edges[x].add(y)
            dist[x] = min(dist[x], 1 + dist[y])
            for node in range(x - 1, -1, -1):
                for dest in edges[node]:
                    if dest > x:
                        continue
                    dist[node] = min(dist[node], 1 + dist[dest])
            results.append(dist[0])
        return results



    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = [set([i+1]) for i in range(n-1)]
        edges.append(set())

        results = []
        steps = [i for i in range(n)]
        # print(steps)

        # remember the q state after processing a node
        qs = [[i+1] for i in range(n-1)]
        qs.append([])

        for query in queries:
            u, v = query
            edges[u].add(v)

            # BFS from 0
            # steps on or before u are not affected.
            q = deque([v])
            # q = deque(qs[u])
            # if steps[u] + 1 <= steps[v]:
            #     q.append(v)
            #     steps[v] = steps[u] + 1

            while q:
                node = q.popleft()
                for dest in edges[node]:
                    if steps[node] + 1 <= steps[dest]:
                        steps[dest] = steps[node] + 1
                        q.append(dest)
                        # qs[node] = list(q)
            results.append(steps[n-1])
            # print(steps)
       
        return results
