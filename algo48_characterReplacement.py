from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = max_val = maxx = 0
        dd = defaultdict(int)
        while(r<len(s)):
            dd[s[r]]+=1
            max_val = max(max_val, dd[s[r]])
            if r - l + 1 - max_val > k:
                dd[s[l]]-=1
                l+=1
            
            maxx = max(maxx, r-l+1)
            r+=1
            
        return maxx
            
            
    
obj = Solution()
res = obj.characterReplacement("ABBB", 2)
print(res)


# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length