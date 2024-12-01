class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjLists = [[] for _ in range(numCourses)]
        inDegrees  = [0] * numCourses

        for p in prerequisites:
            v, u = p
            adjLists[u].append(v)
            inDegrees[v] += 1
        
        # BFS
        q = deque()

        # find all nodes with inDegree=0 to be the start
        for i, x in enumerate(inDegrees):
            if x == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            numCourses -= 1
            for adj in adjLists[cur]:
                # "remove" the edge (just inDegree is enough)
                inDegrees[adj] -= 1
                if inDegrees[adj] == 0:
                    q.append(adj)
        return (numCourses == 0)