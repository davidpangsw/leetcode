VOWELS = ['a', 'e', 'i', 'o', 'u']
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix_counts = [0] * (n+1)
        for i in range(1, n+1):
            if words[i-1][0] in VOWELS and words[i-1][-1] in VOWELS:
                prefix_counts[i] = prefix_counts[i-1] + 1
            else:
                prefix_counts[i] = prefix_counts[i-1]
        
        result = []
        for l, r in queries:
            result.append(prefix_counts[r+1] - prefix_counts[l])
        return result