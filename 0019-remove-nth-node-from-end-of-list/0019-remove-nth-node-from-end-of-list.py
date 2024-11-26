# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(val=0, next=head)
        arr = []
        while head:
            arr.append(head)
            head = head.next
        arr[-n-1].next = arr[-n].next
        return arr[0].next