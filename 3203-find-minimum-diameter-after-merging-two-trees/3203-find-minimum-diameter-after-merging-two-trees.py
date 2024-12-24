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
            while len(q) > 1:
                # print(q)
                size = len(q)
                for _ in range(size):
                    u = q.popleft()
                    if len(adjLists[u]) == 0:
                        continue
                    v = adjLists[u].pop()
                    # adjLists[u].remove(v)
                    adjLists[v].remove(u)
                    if len(adjLists[v]) == 1:
                        q.append(v)
                result += 1
            if len(q) == 1: # even diameter
                result *= 2
            else:
                result = result * 2 - 1

            # print(result)
            return result

        d1 = getDiameter(edges1)
        d2 = getDiameter(edges2)
        return max(d1, d2, (d1+1)//2 + (d2+1)//2 + 1)
        