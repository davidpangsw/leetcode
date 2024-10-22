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
        queue = [root]
        count = 1
        while queue:
            s = 0
            newQueue = []
            for node in queue:
                s += node.val
                if node.left: newQueue.append(node.left)
                if node.right: newQueue.append(node.right)
            sums.append(s)
            queue = newQueue

        if len(sums) < k:
            return -1

        sums.sort() # can use priority queue, but doesn't help much

        print(sums)
        return sums[-k]





        