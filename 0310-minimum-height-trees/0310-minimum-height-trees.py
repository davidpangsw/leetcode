class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjLists = [set() for _ in range(n)]

        for u, v in edges:
            adjLists[u].add(v)
            adjLists[v].add(u)
        
        # BFS
        # Kahn's Algorithm (Topo-sort)
        # start with leaves (degree = 1)
        q = [i for i, x in enumerate(adjLists) if len(x) == 1]

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

        # only happens there is no "leaves"
        # which mean only 1 node
        return [0]