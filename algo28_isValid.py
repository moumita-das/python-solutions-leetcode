class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        map_br = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for ch in s:
            if ch in map_br:
                stk.append(ch)
            else:
                if stk and map_br[stk[-1]] == ch:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        return True
    
obj = Solution()
print(obj.isValid("()"))


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true