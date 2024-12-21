class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = [False] * len(s)

        def dfs(i: int):
            # print(i)
            if visited[i]:
                return False

            visited[i] = True
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and (j == len(s) or dfs(j)):
                    return True
            return False
        return dfs(0)
