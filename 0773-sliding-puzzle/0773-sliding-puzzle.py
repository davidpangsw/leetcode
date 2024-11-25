class Solution:
    def slidingPuzzle(self, target: List[List[int]]) -> int:
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


        initial = [[1, 2, 3], [4, 5, 0]]
        h = hashValue(initial)
        targetH = hashValue(target)
        if h == targetH:
            return 0
        q = deque()
        q.append((initial, h, 1, 2, 0))
        visited = {}
        while q:
            current, h, i, j, count = q.popleft()
            visited[h] = True
            # print(current)

            for di in [-1, 1]:
                I = i + di
                J = j
                if not (0 <= I < 2):
                    continue
                temp = current[I][J]
                current[I][J] = 0
                current[i][j] = temp

                newH = hashValue(current)
                if newH == targetH:
                    return count + 1
                if newH not in visited:
                    q.append((copy(current), hashValue(current), I, J, count + 1))

                temp = current[i][j]
                current[i][j] = 0
                current[I][J] = temp
            
            for dj in [-1, 1]:
                I = i
                J = j + dj
                if not (0 <= J < 3):
                    continue
                temp = current[I][J]
                current[I][J] = 0
                current[i][j] = temp

                newH = hashValue(current)
                if newH == targetH:
                    return count + 1
                if newH not in visited:
                    q.append((copy(current), hashValue(current), I, J, count + 1))

                temp = current[i][j]
                current[i][j] = 0
                current[I][J] = temp
        
        return -1