class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i in range(len(word1)):
            if(i<len(word2)):
                result = result+word1[i]+word2[i]
            else:
                result+=word1[i]
        if(len(word2)>len(word1)):
            result+=word2[len(word1):]
        return result