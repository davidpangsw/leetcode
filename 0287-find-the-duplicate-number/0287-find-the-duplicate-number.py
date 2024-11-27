class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat nums as a linked list
        # where i is linked to nums[i], or (i, nums[i]) is a directed edge

        # get into the cycle of the linked list, using fast-slow pointer
        # let f = distance travelled by fast pointer
        # let s = distance travelled by slow pointer
        # If f = 2s, then both pointers will eventually meet in the cycle at some point (Their distance increases by 1 in each step)
        fast = slow = nums[0]
        while True:
            # print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Now, we want to find the entry of the cycle, because it is being pointed by 2 elements (in and out of the cycle)
        # let k = cycle size
        # Then, f - s is a multiple of k
        # Since f = 2s, s is a multiple of k

        # let l = position (in Linked List) of the entry of the cycle
        # let c = steps after s entried the cycle = s - l (or s = l + c)
        # then l + c = 0 (mod k)
        # if s goes l more steps, it will get back to the entry

        # let s' = 0, move s and s' together, they will meet at l
        # print("fast, slow = ", slow)
        result = nums[0]
        while True:
            # print(result, slow)
            if result == slow:
                return result
            result = nums[result]
            slow = nums[slow]


        
