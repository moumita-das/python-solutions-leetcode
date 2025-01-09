class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict = {}
        for jewel in jewels:
            jewels_dict[jewel] = 1
        stones = [a for a in stones]
        count = 0
        for stone in stones:
            if stone in jewels_dict:
                count+=1
        return count
    
obj = Solution()
print(obj.numJewelsInStones("z","ZZ"))



# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0