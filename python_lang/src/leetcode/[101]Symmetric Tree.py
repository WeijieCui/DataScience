# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center).
#
#
#  Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 1000].
#  -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
#
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 15
# 118 👎 369
# leetcode submit region begin(Prohibit modification and deletion)
import queue
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif root.left is None or root.right is None:
            return root.left is None and root.right is None
        # options will be putted on the queue
        q = queue.Queue()
        q.put((root.left, root.right))
        # check all the options
        while not q.empty():
            left, right = q.get()
            # if the values of two nodes are different, return False
            if left.val != right.val:
                print('val not the same:', left.val, right.val)
                return False
            # check left.left and right.right
            if left.left is not None and right.right is not None:
                q.put((left.left, right.right))
            elif ((left.left is None and right.right is not None)
                  or (left.left is not None and right.right is None)):
                return False
            # check left.right and right.left
            if left.right is not None and right.left is not None:
                q.put((left.right, right.left))
            elif ((left.right is None and right.left is not None)
                  or (left.right is not None and right.left is None)):
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
