VOWELS = ['a', 'e', 'i', 'o', 'u']
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_counts = [0]
        for w in words:
            if w[0] in VOWELS and w[-1] in VOWELS:
                prefix_counts.append(prefix_counts[-1] + 1)
            else:
                prefix_counts.append(prefix_counts[-1])
        
        result = []
        for l, r in queries:
            result.append(prefix_counts[r+1] - prefix_counts[l])
        return result