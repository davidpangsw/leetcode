# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        if not root.left:
            return root
        x, y = root.left, root.right
        root.left.val, root.right.val = root.right.val, root.left.val
        if not x.left:
            return root
        queue = [x.left, x.right, y.left, y.right]
        while True:
            print(queue)
            # currently we are in even layer
            # starting from middle, swap the children
            # and also store them into a deque
            if not queue[0].left:
                break
            n = len(queue)
            mid = (n-1) // 2
            children = deque()
            for i in range(mid, -1, -1):
                x, y = queue[i], queue[n-1-i]
                children.appendleft(x.right)
                children.appendleft(x.left)
                children.append(y.left)
                children.append(y.right)
                
                x.left.val, y.right.val = y.right.val, x.left.val
                x.right.val, y.left.val = y.left.val, x.right.val
            
            # we are in odd layer now
            if not children[0].left:
                break
            
            queue.clear()
            for x in children:
                queue.append(x.left)
                queue.append(x.right)

        return root
                

