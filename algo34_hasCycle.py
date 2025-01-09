from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        if not head:
            return False
        fast = slow = head
        while fast and fast.next:
            if(fast.next == slow):
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False
    
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
head = obj.create_linked_list([1,2,3,4,5])
obj.display_linked_list(head)
print(obj.hasCycle(head))


# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?