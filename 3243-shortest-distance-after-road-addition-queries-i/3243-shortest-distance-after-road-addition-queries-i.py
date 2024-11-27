class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # dist = [[inf for j in range(n)] for i in range(n)]
        # for i in range(n):
        #     for j in range(i, n):
        #         dist[i][j] = j-i
        # [print(row) for row in dist]
        # print()
        edges = [set([i+1]) for i in range(n-1)]

        results = []
        for query in queries:
            # print(query)
            x, y = query
            edges[x].add(y)

            # BFS from 0
            q = deque([0])
            visited = [False for i in range(n)]
            result = inf
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
                        result = step
                        q = None
                        break
                    else:
                        for destNode in edges[node]:
                            q.append(destNode)
                step += 1
            results.append(result)

            # # update all a->x->y->b
            # This method is for dense graph
            # for a in range(0, x+1):
            #     for b in range(y, n):
            #         dist[a][b] = min(dist[a][b], dist[a][x] + 1 + dist[y][b])
            # result.append(dist[0][n-1])
       
        return results
