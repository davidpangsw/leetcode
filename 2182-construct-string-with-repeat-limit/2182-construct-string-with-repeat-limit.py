class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        counts = sorted(counts.items())
        
        result = ""
        while counts:
            x, count = counts[-1]
            if count <= repeatLimit:
                result += x * count
                counts.pop()
            else:
                result += x * count
                counts[-1][1] = (x, count - repeatLimit)

                # if no backup, done
                if not counts:
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
                

