# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
#
#  A valid BST is defined as follows:
#
#
#  The left subtree of a node contains only nodes with keys less than the
# node's key.
#  The right subtree of a node contains only nodes with keys greater than the
# node's key.
#  Both the left and right subtrees must also be binary search trees.
#
#
#
#  Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
#  Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 10⁴].
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 1669
# 3 👎 1364


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #                         15
        #          5
        #      3       7
        #    2   4   6    8
        # 1                 9
        q = queue.Queue()
        q.put((root, None, None))
        while not q.empty():
            node, min_val, max_val = q.get()
            if node.left is not None:
                # compare the value of left node and parent limit
                if min_val is not None and min_val >= node.left.val:
                    return False
                # compare the value of left node and current value
                if node.left.val >= node.val:
                    return False
                q.put((node.left, min_val, node.val))
            if node.right is not None:
                # compare the value of right node and parent limit
                if max_val is not None and max_val <= node.right.val:
                    return False
                # compare the value of right node and current value
                if node.right.val <= node.val:
                    return False
                q.put((node.right, node.val, max_val))
        return True
# runtime:54 ms
# memory:18.3 MB

# leetcode submit region end(Prohibit modification and deletion)
