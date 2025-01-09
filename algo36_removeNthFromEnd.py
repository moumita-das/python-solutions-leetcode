from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if fast:
            while fast and fast.next:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            
        else:
            head = head.next
        
        return head
            
                       
    
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
head = obj.create_linked_list([1,2])
obj.display_linked_list(head)
head = obj.removeNthFromEnd(head,1)
obj.display_linked_list(head)
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?