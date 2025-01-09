from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr:
            return curr
        while curr.next:
            next_node = curr.next
            if next_node.val == curr.val:
                curr.next = next_node.next
            else:
                curr = curr.next
        return head

def create_list(arr):   
    head = ListNode(arr[0])
    prev_node = head
    for i in range(1,len(arr)):
        new_node = ListNode(arr[i])
        prev_node.next = new_node
        prev_node = new_node
    return head

def print_ll(head):
    curr = head
    arr = []
    while curr:
        arr.append(curr.val)
        curr = curr.next

    print(" -> ".join(list(map(str,arr))))
    

head = create_list([1,2,3,4,5,6, 6])
print_ll(head)

obj = Solution()
new_ll = obj.deleteDuplicates(head)
print_ll(new_ll)

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.