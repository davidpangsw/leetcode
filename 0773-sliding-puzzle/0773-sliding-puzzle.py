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

        q = deque([(initial, 5, 0)])
        visited = set()
        canMoveTo = [
            [1, 3], [0, 2, 4], [1, 5],
            [0, 4], [1, 3, 5], [2, 4],
        ]

        while q:
            current, pos, count = q.popleft()

            for cell in canMoveTo[pos]:
                # arr = [c for c in current]
                # arr[pos], arr[cell] = arr[cell], arr[pos]
                # newH = "".join(arr)
                # print(current, pos, cell)
                if pos <= cell:
                    newH = current[:pos] + current[cell] + current[pos+1:cell] + current[pos] + current[cell+1:]
                else:
                    newH = current[:cell] + current[pos] + current[cell+1:pos] + current[cell] + current[pos+1:]
                # print(newH)

                if newH == targetH:
                    return count + 1

                if newH not in visited:
                    q.append((newH, cell, count + 1))
                    visited.add(current)
        return -1