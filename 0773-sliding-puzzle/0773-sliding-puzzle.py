def hashValue(board):
    result = []
    for row in board:
        for x in row:
            result.append(x)
    return tuple(result)

def copy(board):
    newBoard = []
    for row in board:
        newBoard.append([x for x in row])
    return newBoard

class Solution:
    def slidingPuzzle(self, target: List[List[int]]) -> int:
        initial = [[1, 2, 3], [4, 5, 0]]
        h = hashValue(initial)

        targetH = hashValue(target)
        if h == targetH:
            return 0

        q = deque([(initial, h, 1, 2, 0)])

        visited = {}
        while q:
            current, h, i, j, count = q.popleft()
            visited[h] = True

            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                di, dj = d
                I, J = i + di, j + dj
                if not (0 <= I < 2 and 0 <= J < 3):
                    continue
                current[i][j], current[I][J] = current[I][J], current[i][j]

                newH = hashValue(current)
                if newH == targetH:
                    return count + 1
                if newH not in visited:
                    q.append((copy(current), hashValue(current), I, J, count + 1))
                current[i][j], current[I][J] = current[I][J], current[i][j]
        return -1