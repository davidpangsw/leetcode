class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # store all character in t into set
        counts = {}
        for c in t:
            if c not in counts:
                counts[c] = 0
            expected = counts[c]
            counts[c] = expected + 1
        # print("t: ", t, counts)

        total = len(counts)
        countMatched = 0

        queue = []
        qStart = 0

        result = None # (startInc, length)
        for i, c in enumerate(s):
            # print(i, c, counts)
            if c not in counts:
                continue

            queue.append((i, c))

            expected = counts[c]
            if 0 == expected - 1:
                countMatched += 1
            counts[c] = expected - 1
            
            # dequeue as much as possible
            while qStart < len(queue):
                frontI, frontC = queue[qStart]
                expected = counts[frontC]
                if 0 > expected:
                    # dequeue
                    counts[frontC] = expected + 1
                    qStart += 1
                else:
                    break

            if countMatched == total:
                frontI, frontC = queue[qStart]
                backI, backC = queue[-1]
                if result is None or backI - frontI + 1 < result[1]:
                    result = frontI, backI + 1 - frontI
                    # print("updated", frontI, backI)

        if result is None:
            return ""
        else:
            return s[result[0]: result[0] + result[1]]



            



