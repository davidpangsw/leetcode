# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSame(x, y):
    if x is None and y is None:
        return True
    elif x is not None and y is not None:
        return x.val == y.val
    else:
        return False

def isEquiv(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None and root1.val == root2.val:
        if isSame(root1.left , root2.left) and isSame(root1.right, root2.right):
            return isEquiv(root1.left, root2.left) and isEquiv(root1.right, root2.right)
        elif isSame(root1.left, root2.right) and isSame(root1.right, root2.left):
            return isEquiv(root1.left, root2.right) and isEquiv(root1.right, root2.left)
        else:
            return False
    else:
        return False
        



class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return isEquiv(root1, root2)