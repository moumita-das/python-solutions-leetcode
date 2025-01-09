class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        i = 0
        arr=[]
        for item in s:
            if item!="":
                arr.append(item)
        while(i<len(arr)//2):
            arr[i], arr[(len(arr)-i)-1] = arr[(len(arr)-i)-1], arr[i]
            i+=1
        return " ".join(arr)

obj = Solution()
print(obj.reverseWords("  hello world  "))