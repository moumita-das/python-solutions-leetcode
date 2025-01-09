from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
        
class Solution:
    def invertTree(self, root) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        self.displayLevelOrder(root)
        
    
    def makeTree(self, root) -> Optional[TreeNode]:
        arr = root
        root = TreeNode(arr[0])
        dq = deque([root])
        i=1
        while i < len(arr):
            current = dq.popleft()
            if (i<len(arr)):
                current.left = TreeNode(arr[i])
                dq.append(current.left)
                i+=1
            if (i<len(arr)):
                current.right = TreeNode(arr[i])
                dq.append(current.right)
                i+=1
        self.displayLevelOrder(root)
        return root
    
    def displayLevelOrder(self, root) ->Optional[TreeNode]:
        dq = deque([root])
        res = []
        while dq:
            current = dq.popleft()
            res.append(current.val)
            if current.left:
                dq.append(current.left)
            if current.right:
                dq.append(current.right)
        print(" ".join(list(map(str,res))))
            
           

res = Solution()
root = res.makeTree([4,2,7,1,3,6,9])
root = res.invertTree(root)



# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100