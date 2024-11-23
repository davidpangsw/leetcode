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
                if box[i][j] == STONE:
                    result[bottom][m-1-i] = STONE
                    bottom -= 1
                elif box[i][j] == OBSTACLE:
                    result[j][m-1-i] = OBSTACLE
                    bottom = j - 1
        return result