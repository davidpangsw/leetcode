class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        results = [0] * n

        balls = int(boxes[0]) # accumulated balls
        for i in range(1, n):
            results[i] = results[i-1] + balls
            if boxes[i] == "1":
                balls += 1
        # print(results)

        moves = 0
        balls = int(boxes[-1]) # accumulated balls
        for i in range(n-2, -1, -1):
            moves += balls
            results[i] += moves
            if boxes[i] == "1":
                balls += 1
        return results