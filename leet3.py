class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = 0
        for i in candies:
            if(i>max_candies):
                max_candies=i
        result = [i+extraCandies >= max_candies for i in candies]
        return result

        

obj = Solution()
print(obj.kidsWithCandies([2,3,5,1,3], 3))