class Solution:
    def checkListValid(self, tile: list[str]):
        return len(tile)==len(set(tile))

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check for rows
        for i in range(len(board)):
            tile = "".join(board[i])
            tile = tile.replace('.','')
            isValid =self.checkListValid([num for num in tile])
            if not isValid:
                return False
            
        # check for cols
        for i in range(len(board)):
            tile=''
            for j in range(len(board[i])):
                tile+=board[j][i]
            tile = tile.replace('.','')
            isValid =self.checkListValid([num for num in tile])
            if not isValid:
                return False
        
        # check for 3x3
        l = len(board)
        i=1
        while(i < l):
            j=1
            while(j<l):
                tile = f'{board[i-1][j-1]}{board[i-1][j]}{board[i-1][j+1]}{board[i][j-1]}{board[i][j]}{board[i][j+1]}{board[i+1][j-1]}{board[i+1][j]}{board[i+1][j+1]}'
                tile = tile.replace('.','')
                isValid =self.checkListValid([num for num in tile])
                if not isValid:
                    return False
                j+=3
            i+=3


        return True
        



obj = Solution()
print(obj.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))


# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.