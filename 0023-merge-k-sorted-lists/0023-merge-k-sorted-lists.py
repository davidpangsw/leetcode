# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # q = [(l.val, l) for l in lists]
        # q = [(lists[i].val, i) if lists[i] for i in range(len(lists))]
        q = []
        for i, x in enumerate(lists):
            if x:
                q.append((x.val, i))
        heapify(q)
        # print(q, lists)

        head = ListNode()
        tail = head

        while q:
            val, i = heappop(q)
            
            
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

        