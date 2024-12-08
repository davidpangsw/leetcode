class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        n = len(events)
        suffix_max = []

        m = -1
        data = [0] * n
        for i in range(n-1, -1, -1):
            _, _, v = events[i]
            m = max(m, v)
            data[i] = m
        

        result = -1
        for s, e, v in events:
            if events[n-1][0] <= e:
                m = 0
                # print((s, e, v), None)
            else:
                # perform binary search
                # m = bisect_left(events, v)
                left, right = 0, n-1
                while left < right:
                    # print(left, right)
                    mid = (left + right) // 2
                    s1, e1, v1 = events[mid]
                    if s1 > e:
                        right = mid
                    else:
                        left = mid + 1
                m = data[left]
                # print((s, e, v), events[left])

            result = max(result, v + m)
        return result
        
        

