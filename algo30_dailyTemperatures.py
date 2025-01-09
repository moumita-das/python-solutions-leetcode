class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        max_temp = max(temperatures)
        index_arr = [0 for i in range(max_temp+1)]
        
        index_arr[temperatures[-1]] = len(temperatures) - 1
        result = [0]
        i = len(temperatures) - 2
        while i>=0:
            index_arr[temperatures[i]] = i
            result.append(0)
            # check if any item exists in temp array after this temp index position
            if(temperatures[i] + 1 > max_temp):
                i-=1
                continue
            slice_arr = [i for i in index_arr[temperatures[i] + 1:]  if i != 0] 
            if len(slice_arr)==0:
                i-=1
                continue
            min_right_index = min(slice_arr)
            result[-1]=min_right_index-i
            i-=1
        return result[::-1]        
obj = Solution()
print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))


# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100