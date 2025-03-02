# Given the head of a linked list and an integer val, remove all the nodes of 
# the linked list that has Node.val == val, and return the new head. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [], val = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [7,7,7,7], val = 7
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 10⁴]. 
#  1 <= Node.val <= 50 
#  0 <= val <= 50 
#  
# 
#  Related Topics Linked List Recursion 👍 8212 👎 236


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if head is None:
            return None
        node = head
        while node.next:
            if node.next.val == val:
                next = node.next
                while next and next.val == val:
                    next = next.next
                node.next = next
            if node.next:
                node = node.next
            else:
                break
        return head

# leetcode submit region end(Prohibit modification and deletion)
