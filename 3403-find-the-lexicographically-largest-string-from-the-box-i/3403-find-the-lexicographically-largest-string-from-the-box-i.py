class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        arr = [[i, i-1] for i in range(n)]
        result = ""
        while len(arr) > 1:
            candidate = []
            curMaxChar = "a"
            for left, right in arr:
                right += 1
                if right >= n:
                    continue
                c = word[right]
                if c > curMaxChar:
                    curMaxChar = c
                    candidate = [[left, right]]
                elif c == curMaxChar:
                    candidate.append([left, right])
                else:
                    pass
                # print(candidate)
            arr = candidate
            # print(arr)
        left, _ = arr.pop()
        maxSize = n - (numFriends - 1)
        return word[left:left+maxSize]


            
