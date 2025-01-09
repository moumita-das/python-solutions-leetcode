class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if(smallest > prices[i]):
                smallest = prices[i]
            else:
                if(prices[i] - smallest > profit):
                    profit = prices[i] - smallest

        return profit
            


obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
print(obj.maxProfit([5,2,10,7,1,5,3,6,4]))
