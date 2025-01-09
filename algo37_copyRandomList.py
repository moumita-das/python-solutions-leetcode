from typing import Optional
# Definition for singly-linked list.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapp = {}
        curr = head
        while curr:
            if curr.random:
                mapp[curr.random] = curr.random
    
    
    def create_linked_list(self, arr):
        head = Node(arr[0])
        prev = head
        for i in range(1, (len(arr))):
            new_node = Node(arr[i][0], arr[i][1])
            prev.next = new_node
            prev = new_node
        return head
    
    def display_linked_list(self, head):
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        print(" -> ".join(list(map(str, arr))))


obj = Solution()
head = obj.create_linked_list( [[3,None],[3,0],[3,None]])
obj.display_linked_list(head)



# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:



# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]