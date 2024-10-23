# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        queue = [root]
        
        while queue:
            newQueue = []

            # sum all nodes in the same level (next)
            s = 0
            for node in queue:
                if node.left and node.right:
                    inc = node.left.val + node.right.val
                    node.left.val = inc
                    node.right.val = inc
                    newQueue.append(node.left)
                    newQueue.append(node.right)
                    s += inc
                elif node.left:
                    inc = node.left.val
                    newQueue.append(node.left)
                    s += inc
                elif node.right:
                    inc = node.right.val
                    newQueue.append(node.right)
                    s += inc
            
            for node in newQueue:
                node.val = s - node.val

            queue = newQueue
        
        return root