class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalpha():
                left +=1
                continue
            if not s[right].isalpha():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True