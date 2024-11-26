# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry, digit = s // 10, s % 10
            cur.next = ListNode(digit)
            l1, l2 = l1.next, l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        while carry:
            if cur.next:
                s = cur.next.val + carry
                carry, digit = s // 10, s % 10
                cur.next.val = digit
                cur = cur.next
            else:
                cur.next = ListNode(carry)
                carry = 0

        

        return dummy.next