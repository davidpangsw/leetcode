class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        result = set(range(n))
        for e in edges:
            u, v = e
            result.discard(v)
        if len(result) == 1:
            return result.pop()
        else:
            return -1
