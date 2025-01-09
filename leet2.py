class Solution:
    def computeGCD(self, x, y):
        while(y):
            x, y = y, x % y
        return abs(x)
            
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (len(str1) > len(str2)):
            str1, str2 = str2, str1
        gcd = self.computeGCD(len(str1), len(str2))
        if(str1[0:gcd] * (len(str1)//gcd))==str1 and (str1[0:gcd] * (len(str2)//gcd)) == str2:
            return str1[0: gcd]
        else:
            return ""        

obj = Solution()
ans = obj.gcdOfStrings('leet', 'code')
print(ans)