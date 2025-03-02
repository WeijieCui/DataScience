# Given the root of a binary tree, return its maximum depth. 
# 
#  A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,2]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 12
# 640 👎 223


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        options = [(root, 1)]
        idx = 0
        while idx < len(options):
            node, d = options[idx]
            max_depth = max(max_depth, d)
            if node.left:
                options.append((node.left, d + 1))
            if node.right:
                options.append((node.right, d + 1))
            idx += 1
        return max_depth
# leetcode submit region end(Prohibit modification and deletion)
