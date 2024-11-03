class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return (goal + goal).find(s) != -1 and len(s) <= len(goal)