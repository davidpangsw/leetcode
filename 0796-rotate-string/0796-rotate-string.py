class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ind = (goal + goal).find(s)
        return ind != -1 and len(s) <= len(goal)