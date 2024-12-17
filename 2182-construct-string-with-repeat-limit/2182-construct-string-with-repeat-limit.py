class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = [0] * 26
        for x in s:
            counts[ord(x) - ord('a')] += 1
        
        stack = []
        for i, count in enumerate(counts):
            if count > 0:
                stack.append(i)

        
        result = ""
        while stack:
            x = stack.pop()
            if not counts[x]:
                continue
            
            k = min(repeatLimit, counts[x])
            result += chr(ord('a') + x) * k
            counts[x] -= k

            if counts[x]:
                # if no backup, done
                if not stack:
                    break
                
                # add one character of backup
                result += chr(ord('a') + stack[-1])
                counts[stack[-1]] -= 1

                # pop out the backup if no more left
                if not counts[stack[-1]]:
                    stack.pop()
                
                # append back the character
                stack.append(x)
            # print(result)
        return result
                

