# You are given the root of a binary search tree (BST), where the values of
# exactly two nodes of the tree were swapped by mistake. Recover the tree without
# changing its structure.
#
#
#  Example 1:
#
#
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3
# makes the BST valid.
#
#
#  Example 2:
#
#
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2
# and 3 makes the BST valid.
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [2, 1000].
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#
# Follow up: A solution using
# O(n) space is pretty straight-forward. Could you devise a constant
# O(1) space solution?
#
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 7846
#  👎 256


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
from typing import Optional, List
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 1 3 2 4 | 1 5 3 4 2
        # extract ordered values to a list
        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        vals = inorder(root)
        # detect the disorder values
        x = None
        y = None
        for i in range(1, len(vals)):
            if vals[i - 1] > vals[i]:
                y = vals[i]
                if x is None:
                    x = vals[i - 1]
                else:
                    break
        # search nodes of value x and y and replace values
        count = 0
        q = queue.Queue()
        q.put(root)
        while(not q.empty()):
            n = q.get()
            if n.val == x:
                n.val = y
                count += 1
            elif n.val == y:
                n.val = x
                count += 1
            if count >= 2:
                break
            if n.left:
                q.put(n.left)
            if n.right:
                q.put(n.right)

# leetcode submit region end(Prohibit modification and deletion)
