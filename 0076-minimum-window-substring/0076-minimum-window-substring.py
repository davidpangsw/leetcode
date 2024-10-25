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

        queue = []
        qStart = 0

        result = None # (startInc, length)
        for i, c in enumerate(s):
            # print(i, c, counts)
            if c not in counts:
                continue

            queue.append((i, c))

            counts[c] -= 1
            if counts[c] == 0:
                matchedCount += 1
            
            
            # dequeue as much as possible
            while qStart < len(queue):
                _, frontC = queue[qStart]
                if counts[frontC] < 0:
                    # dequeue
                    counts[frontC] += 1
                    qStart += 1
                else:
                    break

            # if valid window, try to update the result
            if matchedCount == len(counts):
                frontI, _ = queue[qStart]
                backI, _ = queue[-1]
                if result is None or backI - frontI + 1 < result[1]:
                    result = frontI, backI + 1 - frontI
                    # print("updated", frontI, backI)

        if result is None:
            return ""
        else:
            return s[result[0]: result[0] + result[1]]



            



