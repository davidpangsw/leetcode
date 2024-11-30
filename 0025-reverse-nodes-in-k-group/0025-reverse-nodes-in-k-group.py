# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def printList(l):
    while l:
        print(l.val, end=' -> ')
        l = l.next
    print()
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = ListNode()
        tail = result

        fast = slow = head
        while slow:
            # print(f"slow={slow.val} fast={fast.val}")
            done = False
            for i in range(k):
                if not fast:
                    done = True
                    break
                fast = fast.next
            if done:
                tail.next = slow
                break
            # print(f"slow={slow.val} fast={fast.val}")
            
            # (fast can be None)
            prev = None
            start = slow
            for i in range(k):
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            tail.next = prev
            tail = start
            # printList(result)
        # printList(result)
        return result.next


