class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        n = len(boxes)
        results = [0] * n
        for i in range(n):
            if boxes[i] == "1":
                ones.append(i)
        for i in range(n):
            for j in ones:
                results[i] += abs(j-i)
            # print(results)
        return results