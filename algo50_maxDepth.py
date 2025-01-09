from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stk = [root]
        height = 1
        while stk:
            current = stk.pop()
            height+= max(self.maxDepth(current.left), self.maxDepth(current.right))
        return height 
        
    def makeTree(self, arr):
        root = TreeNode(arr[0])
        dq = deque([root])
        i = 1
        while i < len(arr):
            current = dq.popleft()
            if i < len(arr):
                current.left = TreeNode(arr[i]) or None
                dq.append(current.left)
                i+=1
                
            if i < len(arr):
                current.right = TreeNode(arr[i]) or None
                dq.append(current.right)
                i+=1
            
        return root
    
    def displayLevelOrder(self, root : Optional[TreeNode]):
        arr = []
        dq = deque([root])
        while dq:
            current = dq.popleft()
            arr.append(current.val or None)
            if current.left:
                dq.append(current.left)
            if current.right:
                dq.append(current.right)
        print(arr)        
        
res = Solution()
root = res.makeTree([1,2,3,4,None,None,5])
res.displayLevelOrder(root)  
print(res.maxDepth(root))      



# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100