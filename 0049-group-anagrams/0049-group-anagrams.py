class Solution:
    def hashcode(self, x):
        return str(sorted(x))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            h = self.hashcode(x)
            if h in d:
                d[h].append(x)
            else:
                d[h] = [x]
        
        # print(d.values())
        return list(d.values())