from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_list =[matrix[i][0] for i in range(len(matrix))]
        l = 0
        r = len(matrix) - 1
        while l < r:
            m = l + (r - l)//2
            if row_list[m] == target:
                l = m
                break
            if row_list[r] == target:
                l = r
                break
            if target > row_list[m]:
                l = m
            else:
                r = m
            if l+1 == r:
                break
        arr = matrix[l]
        l = 0
        r = len(arr)-1
        # print(arr)
        while (l<=r):
            m = l + (r-l)//2
            if arr[m]== target:
                return True
            elif target>arr[m]:
                l = m+1
            else:
                r = m-1
        return False
                

obj = Solution()
res = obj.searchMatrix([[1],[3]], 3)
print(res)

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false