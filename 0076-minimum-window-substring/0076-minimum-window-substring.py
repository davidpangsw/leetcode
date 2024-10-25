class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # store all character in t into set
        counts = {}
        for c in t:
            if c not in counts:
                counts[c] = 0, 0
            count, expected = counts[c]
            counts[c] = 0, expected + 1
        # print("t: ", t, counts)

        total = len(counts)
        countMatched = 0

        queue = []
        qStart = 0

        result = 0, len(s)
        resultLength = None
        for i, c in enumerate(s):
            # print(i, c, counts)
            if c not in counts:
                continue

            queue.append((i, c))

            count, expected = counts[c]
            if count == expected - 1:
                countMatched += 1
            counts[c] = count + 1, expected
            
            # dequeue as much as possible
            while qStart < len(queue):
                frontI, frontC = queue[qStart]
                count, expected = counts[frontC]
                if count > expected:
                    # dequeue
                    counts[frontC] = count - 1, expected
                    qStart += 1
                else:
                    break

            if qStart >= len(queue):
                raise "Impossible!"


            if countMatched == total:
                frontI, frontC = queue[qStart]
                backI, backC = queue[-1]
                if resultLength is None or backI - frontI + 1 < resultLength:
                    result = frontI, backI + 1
                    resultLength = result[1] - result[0]
                    # print("updated", frontI, backI)

        if resultLength is None:
            return ""
        else:
            return s[result[0]: result[1]]



            



