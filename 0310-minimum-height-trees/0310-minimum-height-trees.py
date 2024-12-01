class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjLists = [set() for _ in range(n)]

        for u, v in edges:
            adjLists[u].add(v)
            adjLists[v].add(u)
        
        # BFS by levels
        # Kahn's Algorithm (Topo-sort)
        q = []
        for i, x in enumerate(adjLists):
            # if the degree is 1, it must be a leaf
            if len(x) == 1:
                q.append(i)

        # print(q)
        while q:
            newQ = []
            for cur in q:
                for adj in adjLists[cur]:
                    # remove the edge (just the degree)
                    adjLists[adj].remove(cur)
                    if len(adjLists[adj]) == 1:
                        newQ.append(adj)
            if not newQ: # this is why we kept prev queue
                return q
            elif len(newQ) == 1:
                return newQ
            else:
                q = newQ
            # print(q)
