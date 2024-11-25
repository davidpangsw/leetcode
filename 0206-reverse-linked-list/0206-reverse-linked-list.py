# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        prev = None
        while head:
            result = head
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return result
