class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # counts all character in t
        counts = {}
        for c in t:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
        # print("t: ", t, counts)

        matchedCount = 0

        queue = collections.deque()

        result = None # (startInc, length)
        for i, c in enumerate(s):
            # print(i, c, counts)
            if c not in counts:
                continue

            # enqueue
            queue.append((i, c))

            # if JUST complete the count, inc the matchedCount
            counts[c] -= 1
            if counts[c] == 0:
                matchedCount += 1
            
            
            # dequeue as much as possible
            while queue:
                _, frontC = queue[0]
                if counts[frontC] < 0:
                    # dequeue
                    counts[frontC] += 1
                    queue.popleft()
                else:
                    break

            # if valid window, try to update the result
            if matchedCount == len(counts):
                frontI, _ = queue[0]
                backI, _ = queue[-1]
                if result is None or backI - frontI + 1 < result[1]:
                    result = frontI, backI + 1 - frontI
                    # print("updated", frontI, backI)

        if result is None:
            return ""
        else:
            return s[result[0]: result[0] + result[1]]



            



