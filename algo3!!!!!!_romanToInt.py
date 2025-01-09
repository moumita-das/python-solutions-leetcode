class Solution:
    def romanToInt(self, s: str) -> int:
        chars = {
            'I':1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        counter=0
        for i in range(len(s)):
            ch = s[i]
            if(ch == 'I'):
                if(counter<3):
                    counter+=1
                    continue

obj = Solution()
print(obj.romanToInt('III'))