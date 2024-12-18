class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]
        # left, right = 0, len(s) - 1
        # while left < right:
        #     if not s[left].isalnum():
        #         left +=1
        #         continue

        #     if not s[right].isalnum():
        #         right -= 1
        #         continue

        #     if s[left].lower() != s[right].lower():
        #         return False

        #     left, right = left + 1, right - 1
        return True