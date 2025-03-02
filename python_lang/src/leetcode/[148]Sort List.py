# Given the head of a linked list, return the list after sorting it in
# ascending order.
#
#
#  Example 1:
#
#
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
#
#  Example 2:
#
#
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
#
#  Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 5 * 10⁴].
#  -10⁵ <= Node.val <= 10⁵
#
#
#
#  Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.
# e. constant space)?
#
#  Related Topics Linked List Two Pointers Divide and Conquer Sorting Merge
# Sort 👍 11553 👎 345


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # extract all values to a list
        values = []
        while head:
            values.append(head.val)
            head = head.next
        # sorted value list by merge sort
        p_values = [[i] for i in values]
        while len(p_values) > 1:
            merge_values = []
            for i in range(int(len(p_values) / 2)):
                l1 = p_values[i * 2]
                l2 = p_values[i * 2 + 1]
                i1, i2 = 0, 0
                ml = []
                # merge sort
                while i1 < len(l1) and i2 < len(l2):
                    if l1[i1] < l2[i2]:
                        ml.append(l1[i1])
                        i1 += 1
                    else:
                        ml.append(l2[i2])
                        i2 += 1
                # merge rest
                if i1 < len(l1):
                    ml.extend(l1[i1:])
                if i2 < len(l2):
                    ml.extend(l2[i2:])
                merge_values.append(ml)
            # consider last single list
            if len(p_values) % 2 != 0:
                merge_values.append(p_values[-1])
            p_values = merge_values
        # wrap list to link list
        head = None
        for n in p_values[0][::-1]:
            head = ListNode(n, head)
        return head
# leetcode submit region end(Prohibit modification and deletion)
