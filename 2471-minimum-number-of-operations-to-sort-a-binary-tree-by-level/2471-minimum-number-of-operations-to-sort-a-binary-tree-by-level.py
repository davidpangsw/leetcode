# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def countSwaps(nodes):
            n = len(nodes)
            visited = [False] * n
            s = sorted([(x.val, i) for i, x in enumerate(nodes)])

            count = 0
            # print(s)

            for i in range(n):
                if visited[i]:
                    continue

                # starting at i, count the cycle length
                cur = i

                cycleLen = 0
                visited[i] = True
                while s[cur][1] != i:
                    cur = s[cur][1]
                    cycleLen += 1
                    visited[cur] = True
                
                count += cycleLen 
            return count
                




        q = deque([root])
        result = 0
        while q:
            size = len(q)
            result += countSwaps(q)
            for _ in range(size):
                u = q.popleft()
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
        return result