# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(val=0, next=head)
        stack = []
        while head:
            stack.append(head)
            head = head.next
        stack[-n-1].next = stack[-n].next
        return stack[0].next