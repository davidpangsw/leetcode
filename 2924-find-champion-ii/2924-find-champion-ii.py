class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        result = [True] * n
        for e in edges:
            result[e[1]] = False
        
        champion = None
        for i, x in enumerate(result):
            if x:
                if champion is not None:
                    return -1
                champion = i

        return champion
