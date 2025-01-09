
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            if not left_balanced or not right_balanced:
                return 0, False
            
            # Check the current node's balance condition
            if abs(left_height - right_height) > 1:
                return 0, False
            
            # If balanced, return the height of the current node
            height = 1 + max(left_height, right_height)
            print(node.val, left_height, right_height)
            
            return height, True 
        _, balanced = check_balance(root)
        return balanced
    
    def makeTree(self, arr) -> Optional[TreeNode]:
        root = TreeNode(arr[0])
        dq = deque([root])
        
        i=1
        while(i<len(arr)):
            current = dq.popleft()
            if i < len(arr):
                current.left = TreeNode(arr[i]) or None
                dq.append(current.left)
                i+=1
            if i < len(arr):
                current.right = TreeNode(arr[i]) or None
                dq.append(current.right)
                i+=1
        self.displayLevelOrder(root)
        return root
    
    def displayLevelOrder(self, root: Optional[True]):
        dq = deque([root])
        arr = []
        while dq:
            current = dq.popleft()
            if current:
                arr.append(current.val)
                dq.append(current.left)
                dq.append(current.right)                
        
        print(" ".join(list(map(str, arr))))
        
res = Solution()
root = res.makeTree([1,2,2,3,3,None,None,4,4])
print(res.isBalanced(root))
# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104