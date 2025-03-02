# Given the head of a singly linked list, sort the list using insertion sort,
# and return the sorted list's head.
#
#  The steps of the insertion sort algorithm:
#
#
#  Insertion sort iterates, consuming one input element each repetition and
# growing a sorted output list.
#  At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list and inserts it there.
#  It repeats until no input elements remain.
#
#
#  The following is a graphical example of the insertion sort algorithm. The
# partially sorted list (black) initially contains only the first element in the
# list. One element (red) is removed from the input data and inserted in-place into
# the sorted list with each iteration.
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
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [1, 5000].
#  -5000 <= Node.val <= 5000
#
#
#  Related Topics Linked List Sorting 👍 3091 👎 864


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre = head
        node = head.next
        while node:
            if node.val < pre.val:
                pre.next = node.next
                # node insert
                if node.val < head.val:
                    node.next = head
                    head = node
                else:
                    nnode = head
                    while nnode.next.val < node.val:
                        nnode = nnode.next
                    node.next = nnode.next
                    nnode.next = node
                node = pre.next
            else:
                pre = node
                node = node.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
