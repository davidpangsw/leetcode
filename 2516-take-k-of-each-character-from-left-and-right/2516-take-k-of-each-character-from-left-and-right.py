class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        counts = [0, 0, 0]
        for c in s:
            counts[ord(c) - ord("a")] += 1
        if counts[0] < k or counts[1] < k or counts[2] < k:
            return -1

        left = 0
        right = 0
        for right in range(n):
            # print(counts, s[right], left, right)
            counts[ord(s[right]) - ord("a")] -= 1
            if counts[0] < k or counts[1] < k or counts[2] < k:
                # We don't need to include the character back (which is not useful as it increases the length)
                # We just maintain the difference and see how far we can go
                counts[ord(s[left]) - ord("a")] += 1
                left += 1
        return left + (n-right)-1
