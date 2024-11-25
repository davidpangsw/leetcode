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

class Solution:
    def slidingPuzzle(self, target: List[List[int]]) -> int:
        # use string to represent a board
        initial = "123450"
        targetH = "".join(str(x) for row in target for x in row)
        if initial == targetH:
            return 0
        
        # check solvable
        isOdd = False
        for i in range(6):
            if targetH[i] == "0": continue
            for j in range(i, 6):
                if targetH[j] == "0": continue

                if ord(targetH[i]) > ord(targetH[j]):
                    isOdd = not isOdd
        if isOdd:
            return -1

        q = deque([(initial, 5)])
        visited = {}
        canMoveTo = [
            [1, 3], [0, 2, 4], [1, 5],
            [0, 4], [1, 3, 5], [2, 4],
        ]

        count = 0
        while q:
            qSize = len(q)
            for _ in range(qSize):
                current, pos = q.popleft()

                for cell in canMoveTo[pos]:
                    # print(current, pos, cell)
                    # arr = list(current)
                    # arr[pos], arr[cell] = arr[cell], arr[pos]
                    # newH = "".join(arr)
                    if pos <= cell:
                        newH = current[:pos] + current[cell] + current[pos+1:cell] + current[pos] + current[cell+1:]
                    else:
                        newH = current[:cell] + current[pos] + current[cell+1:pos] + current[cell] + current[pos+1:]
                    # print(newH)

                    if newH == targetH:
                        return count + 1

                    if newH not in visited:
                        q.append((newH, cell))
                        visited[current] = True
            count += 1
        return -1