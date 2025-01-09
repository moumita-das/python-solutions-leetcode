class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter_length = len(word1) if len(word1) < len(word2) else len(word2)
        output = ''
        for i in range(shorter_length):
            output='{output}{w1}{w2}'.format(output=output, w1=word1[i], w2=word2[i])

        print(shorter_length)
        if(len(word1)==shorter_length):
            output = output + word2[shorter_length:]
        else:
            output = output + word1[shorter_length:]
        return output
        
obj = Solution()
ans = obj.mergeAlternately('abc', 'def')
print(ans)
