class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        E = len(pairs)

        inDegrees = {}
        adjLists = {}

        # node -> [inDegree, adjList]
        for pair in pairs:
            u, v = pair
            if u not in adjLists:
                adjLists[u] = []
                inDegrees[u] = 0
            if v not in adjLists:
                adjLists[v] = []
                inDegrees[v] = 0
            inDegrees[v] += 1
            adjLists[u].append(v)

        # count degrees to find the start and end        
        start, end = None, None
        for node in adjLists.keys():
            if len(adjLists[node]) > inDegrees[node]:
                start = node
            elif inDegrees[node] > len(adjLists[node]):
                end = node

        # if all nodes are "even"
        if start is None:
            # here, end must also be None
            # just take any node as start and end
            start = end = node 
        # print(f"{start} -> {end}")
        
        path = deque()
        path.append(start)

        # run a path from start to end
        cur = start
        while True:
            # print(path)
            v = adjLists[cur].pop()
            path.append(v)

            cur = v
            if cur == end:
                break

        # backtracking and add loops along the path
        result = []
        while path:
            # print(path)
            end = path[-1]
            adjList = adjLists[end]
            if not adjList:
                result.append(path.pop())
                continue
            
            # add a loop
            cur = end
            while True:
                path.append(adjList.pop())

                if cur == end:
                    break
                adjList = data[cur]

        # print(result)
        return [[result[E-i], result[E-1-i]] for i in range(E)]




        