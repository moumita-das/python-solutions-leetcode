class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        t = "".join(sorted([ch for ch in t]))
        s = "".join(sorted([ch for ch in s]))
        return s==t

obj = Solution()
print(obj.isAnagram("anagram","nagaram"))

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 