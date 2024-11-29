# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # f = 2s
        f = s = head
        while f:
            s = s.next
            f = f.next
            if f is None:
                return None

            f = f.next
            if f is None:
                return None
            
            if f == s:
                break
        
        s = head
        while f != s:
            f = f.next
            s = s.next
        
        return s