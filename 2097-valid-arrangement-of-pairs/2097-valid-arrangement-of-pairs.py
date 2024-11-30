class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        E = len(pairs)

        # node -> [inDegree, adjList]
        data = {}
        for pair in pairs:
            u, v = pair
            if u not in data:
                data[u] = [0, []]
            if v not in data:
                data[v] = [0, []]
            data[v][0] += 1
            data[u][1].append(pair)
        

        # count degrees to find the start and end        
        start, end = None, None
        for key, value in data.items():
            inDegree, adjList = value
            if len(adjList) > inDegree:
                start = key
            elif inDegree > len(adjList):
                end = key

        # if all even points, take any point as the start and the end
        nodes = list(data.keys())
        if start is None:
            assert (end is None)
            start = nodes[0]
            end = nodes[0]
        # print("odd points", start, end)
        
        path = deque()
        path.append(start)

        # run a path from start to end first
        cur = start
        while True:
            # print(path)
            inDegree, adjList = data[cur]

            edge = adjList.pop()
            u, v = edge

            data[v][0] -= 1
            path.append(v)

            cur = v
            if cur == end:
                break

        # backtracking and add loops along the path
        result = []
        while path:
            # print(path)
            end = path[-1]
            inDegree, adjList = data[end]
            if not adjList:
                result.append(path.pop())
                continue
            
            # add a loop
            cur = end
            while True:
                inDegree, adjList = data[cur]

                u, v = adjList.pop()
                data[v][0] -= 1
                path.append(v)

                if cur == end:
                    break
        # print(result)
        return [[result[E-i], result[E-1-i]] for i in range(E)]




        