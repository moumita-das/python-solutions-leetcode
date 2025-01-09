from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.create_linked_list(head)
        self.display_linked_list(head)
        if not head:
            return head
        prev = head
        curr = next = head.next
        head.next = None
        while next:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
        self.display_linked_list(prev)    
        return prev
            
    
   
    def create_linked_list(self, arr):
        head = ListNode(arr[0])
        prev = head
        for i in range(1, (len(arr))):
            new_node = ListNode(arr[i])
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
res = obj.reverseList([1,2,3,4,5])

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000