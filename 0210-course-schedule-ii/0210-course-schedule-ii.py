class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjLists = [[] for _ in range(numCourses)]
        inDegrees = [0] * numCourses
        for v, u in prerequisites:
            adjLists[u].append(v)
            inDegrees[v] += 1
        
        q = deque()
        for i, x in enumerate(inDegrees):
            if x == 0:
                q.append(i)
        
        result = []
        while q:
            cur = q.popleft()
            result.append(cur)
            for adj in adjLists[cur]:
                inDegrees[adj] -= 1
                if inDegrees[adj] == 0:
                    q.append(adj)
        return result
            