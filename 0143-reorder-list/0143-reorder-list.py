# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            if not fast:
                break
            slow = slow.next
        # slow is pointing to the end of the first part

        temp = slow.next
        slow.next = None
        slow = temp

        # reverse the second part
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        head2 = prev

        tail1 = head
        while tail1 and head2:
            temp = tail1.next
            tail1.next = head2
            head2 = head2.next
            tail1.next.next = temp
            tail1 = temp
        