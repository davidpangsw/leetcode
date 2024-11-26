# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 10000
        while head:
            count -= 1
            if count < 0:
                return True
            head = head.next
        return False

        # s = set()
        # while head:
        #     if head in s:
        #         return True
        #     s.add(head)
        #     head = head.next
        # return False