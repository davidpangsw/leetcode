class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        E = len(pairs)

        # outDegree - inDegree
        degrees = defaultdict(int)
        adjLists = defaultdict(list)

        # node -> [inDegree, adjList]
        for pair in pairs:
            u, v = pair
            degrees[u] += 1
            degrees[v] -= 1
            adjLists[u].append(v)

        # count degrees to find the start  
        stack = []
        for node, degree in degrees.items():
            # print(node, len(adjLists[node]), inDegrees[node])
            if degree > 0:
                stack.append(node) # found starting point
                break

        # if all nodes are "even", just take any node as start
        if not stack:
            stack.append(node)
        
        # DFS
        path = []
        while stack:
            cur = stack[-1]
            if adjLists[cur]:
                v = adjLists[cur].pop()
                stack.append(v)
            else:
                v = stack.pop()
                path.append(v)
        # print(path)
        return list(pairwise(path[::-1]))


        # path = []
        # def dfs(cur):
        #     while adjLists[cur]:
        #         v = adjLists[cur].pop()
        #         dfs(v)
        #         path.append((cur, v))
        # dfs(start)
        # # path supposed to be:
        # # [...[n1, n2],[n0, n1]]
        # return path[::-1]


        # # run a path from start to end
        # cur = start
        # while True:
        #     # print(path)
        #     # print(adjLists, cur, start, end)
        #     v = adjLists[cur].pop()
        #     path.append(v)

        #     cur = v
        #     if cur == end:
        #         break

        # # backtracking and add loops along the path
        # result = []
        # while path:
        #     # print(path)
        #     end = path[-1]
        #     adjList = adjLists[end]
        #     if not adjList:
        #         result.append(path.pop())
        #         continue
            
        #     # add a loop
        #     cur = end
        #     while True:
        #         path.append(adjList.pop())

        #         if cur == end:
        #             break
        #         adjList = data[cur]

        # # print(result)
        # return [[result[E-i], result[E-1-i]] for i in range(E)]




        