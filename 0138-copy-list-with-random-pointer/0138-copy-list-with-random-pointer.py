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
        # and make original.next points to the copy (or use dict if you don't want any change?)
        dummy = Node(0)
        prev = dummy
        while head:
            node = Node(head.val, None, head.random)
            prev.next = node
            prev = node
            
            temp = head.next
            head.next = node
            head = temp
        print("cloned")
        
        head = dummy.next
        while head:
            if head.random:
                head.random = head.random.next
            head = head.next
        return dummy.next