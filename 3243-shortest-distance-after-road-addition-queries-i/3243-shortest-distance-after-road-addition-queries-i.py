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
        for query in queries:
            u, v = query
            edges[u].add(v)

            # BFS from 0
            # steps on or before u are not affected. But we need the queue
            # start from 0
            q = deque([0])
            step = 0
            while q:
                node = q.popleft()
                for dest in edges[node]:
                    if steps[node] + 1 <= steps[dest]:
                        steps[dest] = steps[node] + 1
                        q.append(dest)
            results.append(steps[n-1])
            # print(steps)

            #     qSize = len(q)
            #     for i in range(qSize):
            #         node = q.popleft()
            #         if visited[node]:
            #             continue
            #         visited[node] = True

            #         # print(cost, node)
            #         if node == n-1:
            #             results.append(step)
            #             q = None
            #             break

            #         for destNode in edges[node]:
            #             q.append(destNode)
            #     step += 1
       
        return results
