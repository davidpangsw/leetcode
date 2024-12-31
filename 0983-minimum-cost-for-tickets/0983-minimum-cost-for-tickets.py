class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(cur: int, today: int):
            while cur < len(days) and days[cur] < today:
                cur += 1
            if cur == len(days):
                return 0

            day = days[cur]
            return min(
                costs[0] + dfs(cur+1, day+1),
                costs[1] + dfs(cur+1, day+7),
                costs[2] + dfs(cur+1, day+30),
            )
        return dfs(0, 1)