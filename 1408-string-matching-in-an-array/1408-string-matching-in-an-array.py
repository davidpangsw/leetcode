class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # KMP algorithm
        # Examples:
        #              1         2  
        # m: 01234567890123456789012
        # S: ABC ABCDAB ABCDABCDABDE
        # W: ABCDABD
        #

        # W[3] mismatched S[3]
        # => reset to W[0] and S[3] => mismatch
        # => reset to W[0] and S[4]
        #              1         2  
        # m: 01234567890123456789012
        # S: ABC ABCDAB ABCDABCDABDE
        # W:     ABCDABD
        # starting at S[4], W[6] mismatched S[4+6]
        # reset to W[2] and S[4+6-(6-2)], but how do we know?

        # LPS: [1, 0, 0, 0, 1, 2, 0]
        # LPS[i] = length of longest proper prefix of W[0..i]
        #              which is also a suffix of W[0..i].

        results = []
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if i == j:
                    continue
                if x in y:
                    results.append(x)
                    break
        return results