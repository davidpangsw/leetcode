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
        
        # Let c = cycle length
        # Let x = answer = length before the cycle entry
        # Then, 
        # f - x = s - x (mod c)

        # Since f = 2s, f = s = 0 (mod c)
        # f + l = 0 + l (mod c)
        
        s = head
        while f != s:
            f = f.next
            s = s.next
        
        return s