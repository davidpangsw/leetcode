class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # 100 bits => Four 25 bits integer
        q, r = n // 25, n % 25
        masks = [(1 << 25) - 1] * q
        result = [0] * q
        if r > 0:
            masks += [(1 << r) - 1]
            result += [0]
        # print(",".join([bin(x) for x in masks]))
        # print(",".join([bin(x) for x in result]))

        for e in edges:
            q, r = e[1] // 25, e[1] % 25
            result[q] |= (1 << r)
            # print(",".join([bin(x) for x in result]))
        
        q, r = None, None
        for i in range(len(result)):
            result[i] ^= masks[i]
            if not result[i]:
                continue
            if q is not None:
                return -1
            q = i
            print(",".join([bin(x) for x in result]))
        # print(q)

        ind = 0
        while result[q]:
            if result[q]&1 == 1:
                if r is not None:
                    return -1
                r = ind
                
            result[q] >>= 1
            ind += 1
            print(",".join([bin(x) for x in result]))
        # print(r)
        return q*25 + r

    def findChampionStandard(self, n: int, edges: List[List[int]]) -> int:
        result = [True] * n
        for e in edges:
            result[e[1]] = False
        
        champion = None
        for i, x in enumerate(result):
            if x:
                if champion is not None:
                    return -1
                champion = i

        return champion
