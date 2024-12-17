class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        counts = sorted(counts.items())
        # print(counts)

        result = ""
        while counts:
            x, count = counts.pop()
            # print(x, count, result, x * count, result + x*count)
            if count <= repeatLimit:
                result += x * count
            else:
                result += x * repeatLimit

                # if no backup, done
                if not counts:
                    break
                
                # add one character of backup
                backup, backupCount = counts[-1]
                result += backup
                counts[-1] = (backup, backupCount - 1)

                # pop out the backup if used up
                if not counts[-1][1]:
                    counts.pop()
                
                # append back the character
                counts.append((x, count - repeatLimit))
            # print(result)
        return result
                

