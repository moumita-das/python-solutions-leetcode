class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(t)):
            if s=='':
                break
            if(t[i] == s[0]):
                s=s[1:]
            
        return (len(s)==0)

obj = Solution()
print(obj.isSubsequence("b","abc"))