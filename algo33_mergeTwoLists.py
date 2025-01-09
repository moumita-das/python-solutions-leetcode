from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        
        list1 = self.create_linked_list(list1)
        self.display_linked_list(list1)
        list2 = self.create_linked_list(list2)
        self.display_linked_list(list2)
        
    
        if list1.val <= list2.val :
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        curr = head
        
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                curr.next = list1
                list1 = list1.next 
            else:
                curr.next = list2
                list2 = list2.next 
            curr = curr.next
        
        self.display_linked_list(head)
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
res = obj.mergeTwoLists([1], [2])

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.