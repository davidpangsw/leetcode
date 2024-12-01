class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjLists = [[] for _ in range(n)]
        degrees = [0] * n

        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            adjLists[u].append(v)
            adjLists[v].append(u)
        
        # BFS by levels
        # Kahn's Algorithm (Topo-sort)
        q = []
        for i, x in enumerate(degrees):
            if x == 1:
                q.append(i)

        # print(q)
        while q:
            newQ = []
            for cur in q:
                for adj in adjLists[cur]:
                    # remove the edge
                    degrees[adj] -= 1
                    if degrees[adj] == 1:
                        newQ.append(adj)
            if not newQ:
                return q
            elif len(newQ) == 1:
                return newQ
            else:
                q = newQ
            # print(q)
