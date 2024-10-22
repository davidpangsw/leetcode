# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        sums = []

        # bfs stores the sums
        queue = collections.deque()
        queue.append(root)

        count = 1
        while count > 0:
            s = 0
            newCount = 0
            for _ in range(count):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                    newCount += 1
                
                if node.right:
                    queue.append(node.right)
                    newCount += 1
            
            heapq.heappush(sums, -s)
            count = newCount

            # print(s)
            
        if len(sums) < k:
            return -1

        for _ in range(k):
            result = heapq.heappop(sums)

        return -result





        