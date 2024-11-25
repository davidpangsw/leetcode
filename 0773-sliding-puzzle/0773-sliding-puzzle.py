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
        targetH = ""
        for row in target:
            for x in row:
                targetH += str(x)
        if initial == targetH:
            return 0

        q = deque([(initial, 5, 0)])

        visited = {}
        canMoveTo = [
            [1, 3], [0, 2, 4], [1, 5],
            [0, 4], [1, 3, 5], [2, 4],
        ]
        while q:
            current, pos, count = q.popleft()
            visited[current] = True

            for cell in canMoveTo[pos]:
                arr = [c for c in current]
                arr[pos], arr[cell] = arr[cell], arr[pos]

                newH = "".join(arr)
                if newH == targetH:
                    return count + 1
                if newH not in visited:
                    q.append((newH, cell, count + 1))
                arr[pos], arr[cell] = arr[cell], arr[pos]
        return -1