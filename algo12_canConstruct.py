class Solution:
    def create_hash(self,string_val):
        dict = {}
        for note in string_val:
            if note in dict:
                dict[note] += 1
            else:
                dict[note] = 1
        return dict
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = self.create_hash(ransomNote)
        magazine_dict = self.create_hash(magazine)
        for note in ransom_dict:
            if(note not in magazine_dict or ransom_dict[note]>magazine_dict[note]):
                return False
            
        return True



obj = Solution()
print(obj.canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true