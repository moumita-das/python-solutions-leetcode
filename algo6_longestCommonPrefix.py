class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = list(set(strs))
        if '' in strs:
            return ''
        if(len(strs)==1):
            return strs[0]
        shortest_word = strs[0]
        for i in range(len(strs)):
            if(len(strs[i])<len(shortest_word)):
                shortest_word = strs[i]
        if shortest_word=='':
            return ''
        char_index=0
        for i in range(len(shortest_word)):
            for j in range(len(strs)):
                if(shortest_word[char_index]!=strs[j][i]):
                    if(char_index-1==0):
                        return shortest_word[0]
                    return shortest_word[0:char_index]
            char_index+=1
        return shortest_word[0:char_index]


obj = Solution()
print(obj.longestCommonPrefix(["dog","racecar","car"]))