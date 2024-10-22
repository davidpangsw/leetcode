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
        queue = []
        queue.append((root, 0))

        s = 0
        curLevel = 0
        ind = 0
        n = 1
        while ind < n:
            node, level = queue[ind]
            # print(node.val, level)
            if level == curLevel:
                s += node.val
            else:
                sums.append(s)
                s = node.val
                curLevel = level

            if node.left:
                queue.append((node.left, level + 1))
                n += 1
            
            if node.right:
                queue.append((node.right, level + 1))
                n += 1
            ind += 1
            
        sums.append(s)

        if len(sums) < k:
            return -1

        sums.sort()

        # print(sums)
        return sums[-k]





        