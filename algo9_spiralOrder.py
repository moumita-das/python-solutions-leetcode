class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        i = 0
        j = 0
        # while len(matrix) * len(matrix[0])>len(result):
        #     if matrix[i][j] not in result:
        #         result.append(matrix[i][j])
        #         if j+1 < len(matrix[i]) and matrix[i][j+1] not in result:
        #             j+=1
        #         elif j+1 == len(matrix[i]) and i+1 < len(matrix) and matrix[i+1][j] not in result:
        #             i+=1
        #         elif i+1 == len(matrix) and matrix[i][j-1] not in result:
        #             j-=1
        #         elif j-1==-1 and matrix[i-1][j] not in result:
        #             i-=1

        while len(matrix) * len(matrix[0])>len(result):
            while(j<len(matrix[i])):
                if(matrix[i][j] not in result):
                    result.append(matrix[i][j])
                else:
                    break
                j+=1
            while(i<len(matrix)):
                if(matrix[i][j] not in result):
                    result.append(matrix[i][j])
                else:
                    break
                i+=1
            while(j>=0):
                if(matrix[i][j] not in result):
                    result.append(matrix[i][j])
                else:
                    break
                j-=1
            while(i>=0):
                if(matrix[i][j] not in result):
                    result.append(matrix[i][j])
                else:
                    break
                i-=1

        return result

obj = Solution()
print(obj.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]))





# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 