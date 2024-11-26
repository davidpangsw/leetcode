table = {x: (1 << x) for x in range(101)}
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        mask = table[n] - 1
        # print(bin(mask))
        # print(bin(result))

        for e in edges:
            result |= table[e[1]]
        # print(bin(result))

        result ^= mask
        # print("Result", bin(result))
        
        champ = None
        ind = 0
        while result:
            if result & 1 == 1:
                if champ is not None:
                    return -1
                champ = ind
                
            result >>= 1
            ind += 1
            # print(bin(result))
        return champ

    def findChampionBasic(self, n: int, edges: List[List[int]]) -> int:
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
