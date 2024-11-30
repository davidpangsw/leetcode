# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # q = [(l.val, l) for l in lists]
        q = [(lists[i].val, i) if lists[i] else (inf, None) for i in range(len(lists))]
        heapify(q)
        # print(q, lists)

        head = ListNode()
        tail = head

        while q:
            val, i = heappop(q)
            if i is None or lists[i] is None:
                continue
            
            
            l = lists[i]
            temp = l.next
            l.next = None
            lists[i] = temp
            
            tail.next = l
            tail = tail.next

            if lists[i]:
                heappush(q, (lists[i].val, i))
            # print(q, head, tail)
        
        return head.next

        