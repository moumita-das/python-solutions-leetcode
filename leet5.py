class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = s
        vowels = ['a','e','i','o','u']
        i=0
        j=len(s)-1
        s=[]
        s[:] = string
        while(i<j):
            if(s[i].lower() not in vowels):
                i+=1
            if(s[j].lower() not in vowels):
                j-=1
            if( s[i].lower() in vowels and s[j].lower() in vowels):
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
        return "".join(s)


        
obj = Solution()
print(obj.reverseVowels("aA"))