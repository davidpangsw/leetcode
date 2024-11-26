# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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

        # s = set()
        # while head:
        #     if head in s:
        #         return True
        #     s.add(head)
        #     head = head.next
        # return False