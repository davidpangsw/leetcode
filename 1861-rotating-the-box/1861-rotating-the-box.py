STONE = '#'
OBSTACLE = "*"
EMPTY = "."
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        result = [[EMPTY] * m for _ in range(n)]
        for i in range(m):
            bottom = n-1
            for j in range(n-1, -1, -1):
                match box[i][j]:
                    case str(STONE):
                        result[bottom][m-1-i] = STONE
                        bottom -= 1
                    case str(OBSTACLE):
                        result[j][m-1-i] = OBSTACLE
                        bottom = j - 1
        return result