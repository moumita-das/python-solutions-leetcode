class Solution:
    def trap(self, height: list[int]) -> int:
        rain = 0
        if(height == sorted(height) or height == sorted(height, reverse=True)):
            return 0
        for i in range(1,len(height)-1):
             left_max_height = max(height[:i])
             right_max_height = max(height[i+1:])
             min_height_at_curr_pos = min(left_max_height,right_max_height)
             rain += min_height_at_curr_pos - height[i] if min_height_at_curr_pos > height[i] else 0
        return rain
            
            
            
a= [3,2,1]
b = sorted(a, reverse=True)
print(b)
print(a==b)
obj = Solution()
print(obj.trap([4,2,0,3,2,5]))


# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9