STONE = '#'
OBSTACLE = "*"
EMPTY = "."
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        result = [[EMPTY for _ in range(m)] for _ in range(n)]
        for i in range(m):
            stones = 0
            for j in range(n):
                x = box[i][j]
                if x == EMPTY:
                    continue
                elif x == STONE:
                    stones += 1
                elif x == OBSTACLE:
                    result[j][m-1-i] = OBSTACLE
                    J = j - 1
                    while stones > 0:
                        result[J][m-1-i] = STONE
                        J -= 1
                        stones -= 1
                else:
                    # impossible
                    pass
            # print(stones)
            J = n - 1
            while stones > 0:
                result[J][m-1-i] = STONE
                J -= 1
                stones -= 1
        return result