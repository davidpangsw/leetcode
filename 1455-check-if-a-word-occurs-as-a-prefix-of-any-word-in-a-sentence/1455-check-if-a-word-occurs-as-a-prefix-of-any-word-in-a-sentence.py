class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i = j = 0
        result = 1
        while i < len(sentence):
            # print(sentence[i], j, result)
            
            if sentence[i] == searchWord[j]:
                i += 1
                j += 1
                if j == len(searchWord):
                    return result
                continue
            
            # go to next word
            i += 1
            while i < len(sentence) and sentence[i-1] != " ":
                i += 1

            result += 1
            j = 0

        return -1