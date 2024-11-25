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
        m, n = 2, 3

        # use string to represent a board
        initial = "123450"
        targetH = "".join(str(x) for row in target for x in row)
        if initial == targetH:
            return 0

        # priority queue with this distance function
        def calcDist(s):
            result = 0
            for i in range(m * n):
                if s[i] != '0':
                    num = ord(s[i]) - ord('1')
                    result += abs(i // n - num // n) + abs(i % n - num % n)
            return result

        q = [(0, initial, 5, 0)]
        visited = {}
        canMoveTo = [
            [1, 3], [0, 2, 4], [1, 5],
            [0, 4], [1, 3, 5], [2, 4],
        ]

        count = 0
        while q:
            dist, current, pos, count = heapq.heappop(q)

            for cell in canMoveTo[pos]:
                # print(current, pos, cell)
                arr = list(current)
                arr[pos], arr[cell] = arr[cell], arr[pos]
                newH = "".join(arr)
                # if pos <= cell:
                #     newH = current[:pos] + current[cell] + current[pos+1:cell] + current[pos] + current[cell+1:]
                # else:
                #     newH = current[:cell] + current[pos] + current[cell+1:pos] + current[cell] + current[pos+1:]
                # print(newH)

                if newH == targetH:
                    return count + 1

                if newH not in visited:
                    # print(newH, count+1)
                    heapq.heappush(q, (count + calcDist(newH), newH, cell, count + 1))
                    visited[current] = True
        return -1