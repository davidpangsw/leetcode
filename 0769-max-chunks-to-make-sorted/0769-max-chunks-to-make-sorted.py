class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        curChunkUntil = 0
        for i, x in enumerate(arr):
            if i > curChunkUntil:
                result += 1
                curChunkUntil = max(i, x)
            else:
                curChunkUntil = max(curChunkUntil, x)
        
        result += 1
        return result
