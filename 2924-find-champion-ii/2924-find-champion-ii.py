class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        result = set(range(n))
        for e in edges:
            result.discard(e[1])

        return result.pop() if len(result) == 1 else -1
