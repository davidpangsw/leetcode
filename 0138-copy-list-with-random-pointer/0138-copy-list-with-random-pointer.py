"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # make a copy of list
        # and make original.next points to the copy, using dict
        oldToNew = {None: None}

        dummy = Node(0)
        prev = dummy
        while head:
            node = Node(head.val, None, head.random)
            prev.next = node
            prev = node
            
            oldToNew[head] = node
            head = head.next
        
        head = dummy.next
        while head:
            head.random = oldToNew[head.random]
            head = head.next
        return dummy.next