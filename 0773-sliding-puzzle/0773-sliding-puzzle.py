# def hashValue(board):
    # result = []
    # for row in board:
    #     for x in row:
    #         result.append(x)
    # return tuple(result)

# def copy(board):
#     newBoard = []
#     for row in board:
#         newBoard.append([x for x in row])
#     return newBoard

canMoveTo = [
    [1, 3], [0, 2, 4], [1, 5],
    [0, 4], [1, 3, 5], [2, 4],
]

COMPLETED = "123450"
class Solution:
    def isSolvable(self, target):
        # check solvable:
        # If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
        # If N is even, puzzle instance is solvable if 
        #   the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is odd.
        #   the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is even.
        # For all other cases, the puzzle instance is not solvable.
        isOdd = False
        for i in range(6):
            if target[i] == "0": continue
            for j in range(i, 6):
                if target[j] == "0": continue
                if ord(target[i]) > ord(target[j]):
                    isOdd = not isOdd
        return not isOdd
    
    def bfs(self, target):
        answers = {}

        # use string to represent a board
        target = "".join(str(x) for row in target for x in row)
        if COMPLETED == target:
            return 0
        if not self.isSolvable(target):
            return -1

        q = deque([(COMPLETED, 5)])
        visited = {}
        count = 0
        while q:
            qSize = len(q)
            for _ in range(qSize):
                current, pos = q.popleft()
                print(current, count)

                for cell in canMoveTo[pos]:
                    # print(current, pos, cell)
                    arr = list(current)
                    arr[pos], arr[cell] = arr[cell], arr[pos]
                    newState = "".join(arr)
                    # print(newState)

                    # if newState == target:
                    #     return count + 1

                    if newState not in visited:
                        q.append((newState, cell))
                        visited[newState] = True
            count += 1
        return -1

    def aStarSearch(self, start):
        # use string to represent a board
        start = "".join(str(x) for row in start for x in row)
        current = start
        if start == COMPLETED:
            return 0
        if not self.isSolvable(start):
            return -1
        
        def heuristic(board):
            # f = g + h
            # where g = cost from the start to current node
            #       h = "heuristics", a smart guess from current node to the goal
            # if 0 <= h <= h* (the actual cost)
            # then we are guanrantee to achieve the shortest path
            # if h = 0, it is dijkastra (and slow)
            # if h = h*, it is fast
            # This function only calculates h, using taxicab (Manhatann) distance to the COMPLETED state
            total = 0
            for i, x in enumerate(board):
                x = ord(x) - ord("1")
                row, col = i // 3, i % 3
                if x == "0":
                    total += abs(row - 1) + abs(col - 2)
                else:
                    total += abs(row -  x // 3) + abs(col - x // 3)
            return total


        ind = current.index("0")
        # q = [(f=g+h, current, ind, g)]
        q = [(0 + heuristic(current), current, ind, 0)]

        visited = {}
        while q:
            f, current, pos, g = heappop(q)
            # print(f, current, pos, g)

            for cell in canMoveTo[pos]:
                # print(current, pos, cell)
                arr = list(current)
                arr[pos], arr[cell] = arr[cell], arr[pos]
                newState = "".join(arr)
                # print(newState)

                if newState == COMPLETED:
                    return g + 1

                if newState not in visited:
                    q.append(((g+1) + heuristic(newState), newState, cell, g+1))
                    visited[current] = True
        return -1

    def slidingPuzzle(self, target: List[List[int]]) -> int:
        return self.aStarSearch(target)