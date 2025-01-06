class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves = 0

        # number of balls on the left / right
        left, right = 0, 0

        # calculate for i = 0
        for i, x in enumerate(boxes):
            if x == '1':
                moves += i
                right += 1
        
        answer = []
        for i, x in enumerate(boxes):
            answer.append(moves)
            if x == '1':
                left += 1
                right -= 1
            moves = moves + left - right

        return answer