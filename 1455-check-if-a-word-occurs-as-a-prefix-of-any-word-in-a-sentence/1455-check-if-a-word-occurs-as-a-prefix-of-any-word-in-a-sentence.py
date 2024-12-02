class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # for i, word in enumerate(sentence.split(' ')):
        #     if word.startswith(searchWord):
        #         return i + 1
        # return -1

        count = 0
        word = 1
        for x in sentence:
            if count != -1 and x == searchWord[count]:
                count += 1
                if count == len(searchWord):
                    return word
            elif x == ' ':
                count = 0
                word += 1
            else:
                count = -1
        return -1

        # i = j = 0
        # word = 1
        # while i < len(sentence):
        #     # print(sentence[i], j, result)
            
        #     if sentence[i] == searchWord[j]:
        #         i += 1
        #         j += 1
        #         if j == len(searchWord):
        #             return word
        #         continue
            
        #     # go to next word
        #     i += 1
        #     while i < len(sentence) and sentence[i-1] != " ":
        #         i += 1
        #     word += 1

        #     # reset the count
        #     j = 0

        # return -1