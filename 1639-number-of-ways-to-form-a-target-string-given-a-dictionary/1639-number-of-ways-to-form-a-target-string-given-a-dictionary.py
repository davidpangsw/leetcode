M = 10 ** 9 + 7
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        data = []
        for w in words:
            for i, x in enumerate(w):
                if i >= len(data):
                    data.append(defaultdict(int))
                data[i][x] += 1
        
        mem = [[None for _ in target] for _ in data]
        def f(cur: int, t: int):
            if t == len(target):
                return 1
            if cur == len(data):
                return 0
            
            if mem[cur][t] is None:
                mem[cur][t] = (data[cur][target[t]] * f(cur+1, t+1) + f(cur+1, t)) % M
            return mem[cur][t]
        return f(0, 0)
