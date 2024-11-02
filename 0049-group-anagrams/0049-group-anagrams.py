class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for x in strs:
            h = str(sorted(x)) # "hashcode" of x
            d[h].append(x)
            # if h in d:
            #     d[h].append(x)
            # else:
            #     d[h] = [x]
        
        # print(d.values())
        return list(d.values())