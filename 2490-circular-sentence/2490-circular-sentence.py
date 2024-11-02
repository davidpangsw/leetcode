class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        spaceAt = sentence.find(' ', 1)
        while spaceAt != -1:
            if sentence[spaceAt-1] != sentence[spaceAt+1]:
                return False
            spaceAt = sentence.find(' ', spaceAt+1)
        return True
