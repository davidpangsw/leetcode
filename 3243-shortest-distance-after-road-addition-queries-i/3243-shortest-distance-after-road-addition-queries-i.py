class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = [set([i+1]) for i in range(n-1)]

        results = []
        for query in queries:
            edges[query[0]].add(query[1])

            # BFS from 0
            q = deque([0])
            visited = [False] * n
            step = 0
            while q:
                qSize = len(q)
                for i in range(qSize):
                    node = q.popleft()
                    if visited[node]:
                        continue
                    visited[node] = True

                    # print(cost, node)
                    if node == n-1:
                        results.append(step)
                        q = None
                        break

                    for destNode in edges[node]:
                        q.append(destNode)
                step += 1
       
        return results
