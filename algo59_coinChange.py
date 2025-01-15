from typing import List

class Solution:
    def shorten_array(arr, target):
        r=len(arr)-1
        while(r>=0):
            if arr[r]>target:
                r-=1
            else:
                break
        if r<0:
            return -1
        arr = arr[0:r+1]
        return arr
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        l=0
        
        print(coins)
            

obj = Solution()
print(obj.coinChange([1,2,5,],11))

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104