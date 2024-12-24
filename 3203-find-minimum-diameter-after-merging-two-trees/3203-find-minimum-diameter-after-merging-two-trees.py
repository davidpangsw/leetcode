class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def getDiameter(edges):
            adjLists = defaultdict(set)
            for u, v in edges:
                adjLists[u].add(v)
                adjLists[v].add(u)
            
            # BFS starting from leaves
            q = deque([u for u in adjLists if len(adjLists[u]) == 1])
            result = 0
            size = len(q)
            while size > 1:
                # print(q)
                for _ in range(size):
                    u = q.popleft()
                    if adjLists[u]:
                        v = adjLists[u].pop()
                        # adjLists[u].remove(v)
                        adjLists[v].remove(u)
                        if len(adjLists[v]) == 1:
                            q.append(v)
                result += 2
                size = len(q)

            return result + size - 1

        d1 = getDiameter(edges1)
        d2 = getDiameter(edges2)
        return max(d1, d2, (d1+1)//2 + (d2+1)//2 + 1)
        