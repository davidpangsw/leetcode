class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""

        prev = None
        count = 0
        for x in s:
            if x == prev:
                if count >= 2:
                    continue
                count += 1
                result += x
            else:
                prev = x
                count = 1
                result += x
        
        return result