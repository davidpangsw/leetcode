class Solution:
    result = 0
    def backtracking(self, s: str, ind: int, pendingFrom: int, groupsDict: dict[str, bool]):
        """
        Use dict (deletion is O(1)), not set.
        """
        # if we are at the end, update the split count, return
        if ind == len(s):
            # push the last pending
            pending = s[pendingFrom:ind]
            if pending in groupsDict:
                return

            # print("Add group: " + pending)
            groupsDict[pending] = True
            self.result = max(self.result, len(groupsDict))
            # print("Remove group: " + pending)
            del groupsDict[pending]

            return
        
        # We have two choices
        # 1. Append current character to pending group (need ind < len(s))
        # 2. Check the pending group causes a conflict first, then set current character as a new pending group 

        # 1. Append this character to pending group
        self.backtracking(s, ind + 1, pendingFrom, groupsDict)

        # 2. Check the pending group causes a conflict first, then set current character as a new pending group
        pending = s[pendingFrom:ind]
        if pending in groupsDict:
            return

        # print("Add group: " + pending)
        groupsDict[pending] = True
        self.backtracking(s, ind + 1, ind, groupsDict)
        # print("Remove group: " + pending)
        del groupsDict[pending] # backtrack

    def maxUniqueSplit(self, s: str) -> int:
        self.backtracking(s, 1, 0, {})
        return self.result