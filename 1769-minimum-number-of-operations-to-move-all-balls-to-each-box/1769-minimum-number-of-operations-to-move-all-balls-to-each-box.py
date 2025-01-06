class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        results = [0] * n
        for i in range(n):
            if boxes[i] == "1":
                for j in range(n):
                    results[j] += abs(j-i)
            # print(results)
        return results