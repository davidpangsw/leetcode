class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1, s2 = set(), set()
        n = len(A)
        results = [0] * n
        for i in range(n):
            s1.add(A[i])
            s2.add(B[i])
            
            if A[i] == B[i]:
                results[i] = results[i-1] + 1
            else:
                results[i] = results[i-1]
                if A[i] in s2:
                    results[i] += 1
                if B[i] in s1:
                    results[i] += 1
        return results



