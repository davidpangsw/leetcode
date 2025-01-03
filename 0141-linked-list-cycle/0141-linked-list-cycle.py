# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycleConstantMemory(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        cur = head
        while cur:
            if cur.next == head:
                return True
            temp = cur.next
            cur.next = head
            cur = temp
            # cur, cur.next = cur.next, head
        return False

    def hasCycleNaive(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val is None:
                return True
            head.val = None # mark as visited
            head = head.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False