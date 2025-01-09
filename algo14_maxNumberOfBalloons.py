class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = {
            'l':2,
            "o":2,
            "n":1,
            'b':1,
            'a':1,
        }
        count = 0
        dict = {}
        for ch in text:
            if ch not in dict:
                dict[ch]=1
            else:
                dict[ch]+=1
        for ch in balloon_dict:
            if ch not in dict:
                return 0
            occurances = dict[ch] // balloon_dict[ch]
            if occurances == 0:
                return 0
            if occurances<count or count==0:
                count=occurances
        return count
            


obj = Solution()
print(obj.maxNumberOfBalloons("leetcode"))



# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0