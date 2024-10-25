class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # counts all character in t
        counts = {}
        for c in t:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
        matchedCount = 0
        # print("t: ", t, counts)

        # stores matched index (thus the char) in s
        # dequeue when the front item is not necessary
        queue = collections.deque()

        result = None # (startIndex, length)
        for i, c in enumerate(s):
            # print(i, c, counts)
            if c not in counts:
                continue

            # enqueue
            queue.append(i)
            c = s[i]

            # if JUST complete the count, inc the matchedCount
            counts[c] -= 1
            if counts[c] == 0:
                matchedCount += 1
            
            # dequeue as much as possible
            while queue:
                front = queue[0]
                frontC = s[front]
                if counts[frontC] < 0:
                    # dequeue
                    counts[frontC] += 1
                    queue.popleft()
                else:
                    break

            # if valid window, try to update the result
            if matchedCount == len(counts):
                frontI = queue[0]
                backI = queue[-1]
                if result is None or backI - frontI + 1 < result[1]:
                    result = frontI, backI + 1 - frontI
                    # print("updated", frontI, backI)

        if result is None:
            return ""
        else:
            return s[result[0]: result[0] + result[1]]



            



